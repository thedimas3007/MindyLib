import json
import zlib
from base64 import b64decode
from functools import reduce
from io import BytesIO
from math import floor, ceil
from os import PathLike
from typing import IO, BinaryIO, Optional

from PIL import Image

from content.blocks import get_block
from content.blocks.block_types import PowerGenerator
from g_types.item_cost import ItemCost
from .tile import Tile, GhostTile
from .point2 import Point2
from .block import Block
from .tile import TileRotation
from utils import JavaTypes, read_num, read_utf, read_obj


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

    def __getitem__(self, item: Point2 | tuple[int, int]) -> Optional[Tile | GhostTile]:
        if not (isinstance(item, Point2) or isinstance(item, tuple)):
            raise TypeError("item must be of type Point2 or tuple[int, int]")
        if isinstance(item, tuple):
            item = Point2(*item)
        if item.x < 0 or item.y < 0:
            raise ValueError("item.x and item.y must be >= 0")
        if item.x >= self.width or item.y >= self.height:
            raise ValueError("item.x and item.y must be < width and height respectively")

        return next((tile for tile in self._tiles if tile.pos == item), None)

    def save_preview(self, filename: str = "preview.png") -> None:
        preview = Image.new("RGBA", (self.width*32, self.height*32), (0, 0, 0, 0))
        for tile in self._tiles:
            if isinstance(tile, GhostTile):
                continue
            block_img = Image.open(f"sprites/block-{tile.block.id}-ui.png")
            block_img = block_img.rotate(tile.rot.value * 90)
            tile_width = block_img.width // 32
            tile_height = block_img.height // 32

            x_offset = (tile_width - 1) // 2
            y_offset = (tile_height - 1) // 2

            x_pos = (tile.x - x_offset) * 32
            flipped_y = (self.height - tile.y - tile_height + y_offset) * 32

            preview.paste(block_img, (x_pos, flipped_y))
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


if __name__ == "__main__":
    from rich import print
    print("== Fancy Schematic Parser ==")
    print("Loading [yellow]test.msch[/]")
    f = open("samples/turrets.msch", "rb")
    s = Schematic.from_file(f)
    # s.save_preview()
    # s.render_debug()
    # print("-- Schematic info --")
    # print(f"Size: [yellow]{s.width}x{s.height}[/]")
    # print(f"Name: [yellow]{s.name.strip()}[/]")
    # if s.description != "":
    #     print(f"Description: [yellow]{s.description}[/]")
    # print(f"Items:")
    # for i,a in {i: a for i,a in s.cost if a > 0}.items():
    #     print(f"  {i.name}: [yellow]{a}[/]")
    # print(f"Power: [{'green' if s.power_balance >= 0 else 'red'}]{s.power_balance}[/]")
