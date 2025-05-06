import json
import zlib
from base64 import b64decode
from functools import reduce
from io import BytesIO
from math import floor, ceil
from os import PathLike
from typing import IO, BinaryIO, Optional

from PIL import Image, ImageEnhance
from scipy.optimize import direct

from content.blocks import get_block
from content.blocks.block_types import PowerGenerator, Conveyor, StackConveyor, BridgeConveyor
from .block import BlockOutput, BlockOutputDirection
from .item_cost import ItemCost
from .tile import Tile, GhostTile, Direction
from .point2 import Point2
from .tile import TileRotation
from utils import JavaTypes, read_num, read_utf, read_obj, paste_opacity


class Schematic: # Read only for now
    def __init__(self, version: int, width: int, height: int, tags: dict[str, str], tiles: list[Tile | GhostTile]):
        # Maybe should add raw base64 here and/or decompressed data
        assert width > 0 and height > 0
        assert width <= 128 and height <= 128

        self._version = version
        self._width = width
        self._height = height
        self._tags = tags
        self._tiles = tiles
        self._update_stacked_convs()

    @property
    def version(self) -> int:
        return self._version

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def tags(self) -> dict[str, str]:
        return self._tags.copy()

    @property
    def name(self) -> str:
        return self._tags["name"]

    @property
    def description(self) -> str:
        return self._tags["description"]

    @property
    def labels(self) -> list[str]:
        if "labels" not in self._tags: return []
        try:
            return json.loads(self._tags["labels"])
        except Exception as e: # Log.debug mby
            return []

    @property
    def tiles(self) -> list[Tile | GhostTile]:
        return self._tiles.copy()

    @property
    def power_consumption(self) -> int:
        return round(sum(tile.block.power_consumption * 60 for tile in self._tiles))

    @property
    def power_generation(self) -> int:
        return round(sum(tile.block.power_generation * 60 for tile in self._tiles if isinstance(tile.block, PowerGenerator)))

    @property
    def power_balance(self) -> int:
        return self.power_generation - self.power_consumption

    @property
    def cost(self) -> ItemCost:
        return reduce(lambda a, b: a + b, (tile.block.cost for tile in self._tiles))

    def _connection_dirs(self, pos: Point2 | tuple[int, int], output_type: BlockOutput, only_type: Optional[type], incoming: bool):
        pos = Point2.convert(pos)
        if pos.x < 0 or pos.y < 0 or pos.x >= self.width or pos.y >= self.height:
            raise ValueError("pos is out of bounds")
        neighboring_directions = []

        for direction in Direction.all():
            neighbor_pos = pos + direction.offset
            if not self.within_bounds(neighbor_pos):
                continue

            neighbor_tile = self[neighbor_pos]
            if neighbor_tile is None:
                continue
            if output_type & neighbor_tile.block.output == BlockOutput.NONE:
                continue

            actual_dir = neighbor_tile.rotated_output()
            target_dir = direction.inverted() if incoming else direction
            if target_dir in actual_dir and (only_type is None or isinstance(neighbor_tile.block, only_type)):
                neighboring_directions.append(direction)

        return neighboring_directions

    def _rotated_dirs(self, pos: Point2 | tuple[int, int], only_type: Optional[type], incoming: bool):
        pos = Point2.convert(pos)
        if not self.within_bounds(pos):
            raise ValueError("pos is outside bounds")

        tile = self[pos]
        if tile is None:
            return BlockOutputDirection.NONE

        neighbors = self.input_dirs(pos, tile.block.output, only_type) if incoming \
            else self.output_dirs(pos, tile.block.output, only_type)
        directions = BlockOutputDirection.NONE

        for direction in neighbors:
            if tile.rot == TileRotation.RIGHT:
                if direction == Direction.TOP: directions |= BlockOutputDirection.LEFT
                elif direction == Direction.RIGHT: directions |= BlockOutputDirection.TOP
                elif direction == Direction.BOTTOM: directions |= BlockOutputDirection.RIGHT
                elif direction == Direction.LEFT: directions |= BlockOutputDirection.BOTTOM

            elif tile.rot == TileRotation.UP:
                if direction == Direction.TOP: directions |= BlockOutputDirection.TOP
                elif direction == Direction.RIGHT: directions |= BlockOutputDirection.RIGHT
                elif direction == Direction.BOTTOM: directions |= BlockOutputDirection.BOTTOM
                elif direction == Direction.LEFT: directions |= BlockOutputDirection.LEFT

            elif tile.rot == TileRotation.LEFT:
                if direction == Direction.TOP: directions |= BlockOutputDirection.RIGHT
                elif direction == Direction.RIGHT: directions |= BlockOutputDirection.BOTTOM
                elif direction == Direction.BOTTOM: directions |= BlockOutputDirection.LEFT
                elif direction == Direction.LEFT: directions |= BlockOutputDirection.TOP

            elif tile.rot == TileRotation.BOTTOM:
                if direction == Direction.TOP: directions |= BlockOutputDirection.BOTTOM
                elif direction == Direction.RIGHT: directions |= BlockOutputDirection.LEFT
                elif direction == Direction.BOTTOM: directions |= BlockOutputDirection.TOP
                elif direction == Direction.LEFT: directions |= BlockOutputDirection.RIGHT

        return directions

    def _update_stacked_convs(self):
        conveyors: list[Tile] = list(filter(lambda t: isinstance(t.block, StackConveyor), self._tiles))
        for conv in conveyors:
            outputs = self.rotated_outputs(conv.pos, StackConveyor)
            if not outputs & BlockOutputDirection.TOP: # No frontal outputs - last block of the chain
                conv.block.output_direction = BlockOutputDirection.ALL

    def _render_bridges(self, image: Image.Image, opacity=0.8):
        bridges: list[Tile] = list(filter(lambda t: isinstance(t.block, BridgeConveyor), self._tiles))

        for bridge in bridges:
            pos = Point2.convert(bridge.config)
            target_x = bridge.x + pos.x
            target_y = bridge.y + pos.y

            if (pos.x != 0 and pos.y != 0) or (pos.x == 0 and pos.y == 0):
                continue

            dist = max(abs(pos.x), abs(pos.y)) - 1
            if dist <= 0:
                continue

            step_x = 1 if pos.x > 0 else -1 if pos.x < 0 else 0
            step_y = 1 if pos.y > 0 else -1 if pos.y < 0 else 0

            bridge_img = Image.open(f"sprites/blocks/distribution/{bridge.block.id}-bridge.png").convert("RGBA")
            pos = Point2(bridge.x + step_x, bridge.y + step_y)

            for i in range(dist):
                if self.within_bounds(pos):
                    paste_opacity(image, bridge_img, (pos.x * 32, (self._height - pos.y) * 32 - bridge_img.height), opacity)

                pos = Point2(pos.x + step_x, pos.y + step_y)

    def within_bounds(self, pos: Point2 | tuple[int, int]) -> bool:
        pos = Point2.convert(pos)
        return 0 <= pos.x < self._width and 0 <= pos.y < self._height

    def save_preview(self, filename: str = "preview.png") -> None:
        preview = Image.new("RGBA", (self.width*32, self.height*32), (0, 0, 0, 0))
        for tile in self._tiles:
            if isinstance(tile, GhostTile):
                continue
            block_img = tile.block.sprite(self, tile)
            # block_img = block_img.rotate(tile.rot.value * 90)
            tile_width = block_img.width // 32
            tile_height = block_img.height // 32

            x_offset = (tile_width - 1) // 2
            y_offset = (tile_height - 1) // 2

            x_pos = (tile.x - x_offset) * 32
            flipped_y = (self.height - tile.y - tile_height + y_offset) * 32

            preview.paste(block_img, (x_pos, flipped_y))
        self._render_bridges(preview)
        preview.save(filename)

    def render_canvases(self) -> None:
        # Used Java code from Mindustry sources to decode canvas config
        bpp = 3
        pixels = 12*12

        def get_byte(arr, offset):
            result = 0
            for i in range(bpp):
                word = i + offset >> 3
                result |= ((0 if (arr[word] & (1 << (i + offset & 7))) == 0 else 1) << i)
            return result

        colors = [0x362944, 0xc45d9f, 0xe39aac, 0xf0dab1, 0x6461c2, 0x2ba9b4, 0x93d4b5, 0xf0f6e8]
        n_canvas = 0
        for tile in self._tiles:
            if tile.block.id == "canvas":
                img = Image.new("RGB", (12, 12), (0, 0, 0))
                for i in range(pixels):
                    offset = i * bpp
                    index = get_byte(tile.config, offset)
                    color = colors[index]
                    img.putpixel((i % 12, i // 12), (color >> 16, (color >> 8) & 0xFF, color & 0xFF)) # hex is BGR whilst PIL uses RGB
                img.save(f"canvas-{n_canvas}.png")
                n_canvas += 1

    def render_debug(self) -> None:
        """
        Used for rendering debug images of GhostTiles.
        For internal use.
        """
        img = Image.new("RGB", (self.width, self.height), (0, 0, 0))
        print(f"Size: {self.width}x{self.height}")
        for tile in self._tiles:
            print(tile)
            if len(list(filter(lambda t: t.x == tile.x and t.y == tile.y, self._tiles))) > 1: # intersection
                img.putpixel((tile.x, self.height - tile.y - 1), (0, 128, 255))
            elif isinstance(tile, GhostTile):
                img.putpixel((tile.x, self.height - tile.y - 1), (255, 0, 0))
            else:
                img.putpixel((tile.x, self.height - tile.y - 1), (0, 255, 0))
        img.save("debug.png")

    def adjacent_tiles(self, pos: Point2 | tuple[int, int]) -> list[tuple[Direction, Tile | GhostTile]]: # TODO: for blocks bigger than 1x1
        if not (isinstance(pos, Point2) or isinstance(pos, tuple)):
            raise TypeError("pos must be of type Point2 or tuple[int, int]")
        if isinstance(pos, tuple):
            pos = Point2(*pos)
        if not self.within_bounds(pos):
            raise ValueError("pos is outside bounds")

        tiles = []
        for direction in Direction.all():
            new_pos = pos + direction.offset
            if new_pos in self:
                if not self[new_pos]:
                    continue
                tiles.append((direction, self[new_pos]))
        return tiles

    def input_dirs(self, pos: Point2 | tuple[int, int], output_type: BlockOutput, only_type: Optional[type] = None) -> list[Direction]:
        return self._connection_dirs(pos, output_type, only_type, True)

    def output_dirs(self, pos: Point2 | tuple[int, int], output_type: BlockOutput, only_type: Optional[type] = None) -> list[Direction]:
        return self._connection_dirs(pos, output_type, only_type, False)

    def rotated_inputs(self, pos: Point2 | tuple[int, int], only_type: Optional[type] = None) -> BlockOutputDirection:
        return self._rotated_dirs(pos, only_type, True)

    def rotated_outputs(self, pos: Point2 | tuple[int, int], only_type: Optional[type] = None) -> BlockOutputDirection:
        return self._rotated_dirs(pos, only_type, False)

    def __getitem__(self, item: Point2 | tuple[int, int]) -> Optional[Tile | GhostTile]:
        item = Point2.convert(item)
        if not self.within_bounds(item):
            raise ValueError("item is outside bounds")

        return next((tile for tile in self._tiles if tile.pos == item), None)

    def __contains__(self, item: Point2 | tuple[int, int]) -> bool:
        item = Point2.convert(item)
        return self.within_bounds(item)

    @staticmethod
    def from_file(file: str | PathLike | BinaryIO) -> "Schematic":
        if isinstance(file, PathLike) or isinstance(file, str):
            file = open(file, "rb")
        if file.read(4) != b"msch":
            raise Exception("Not a schematics file")
        ver = read_num(file, JavaTypes.BYTE)
        decom = BytesIO(zlib.decompress(file.read()))
        width = read_num(decom, JavaTypes.SHORT)
        height = read_num(decom, JavaTypes.SHORT)

        total_tags = read_num(decom, JavaTypes.BYTE)
        tags = {}
        for _ in range(total_tags):
            name = read_utf(decom)
            value = read_utf(decom)
            tags[name] = value

        blocks_used = read_num(decom, JavaTypes.BYTE)
        blocks = []
        for _ in range(blocks_used):
            name = read_utf(decom)
            block = get_block(name)
            if block is None:
                raise Exception(f"Unknown block {name}")
            blocks.append(block)

        total_blocks = read_num(decom, JavaTypes.INT)
        tiles: list[Tile] = []
        for _ in range(total_blocks):
            index = read_num(decom, JavaTypes.BYTE)
            point = Point2.unpack(read_num(decom, JavaTypes.INT))
            cfg = read_obj(decom)
            rot = read_num(decom, JavaTypes.BYTE) % 4
            rot_obj = TileRotation.from_int(rot)
            block = blocks[index]
            tiles.append(Tile(point, block, rot_obj, cfg))

            if block.size > 1:
                lower = -floor(block.size/2) + (1-block.size%2)
                upper = floor(block.size/2)
                for y in range(lower, upper + 1):
                    for x in range(lower, upper + 1):
                        if x == 0 and y == 0:
                            continue
                        new_point = Point2(point.x + x, point.y + y)
                        tiles.append(GhostTile(new_point, block, rot_obj, cfg))
        file.close()
        return Schematic(ver, width, height, tags, tiles)

    @staticmethod
    def from_b64(b64: str) -> "Schematic":
        return Schematic.from_file(BytesIO(b64decode(bytes(b64, "utf-8"))))
