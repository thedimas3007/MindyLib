import json
import zlib
from io import BytesIO
from os import PathLike
from typing import IO, BinaryIO

from PIL import Image

from .tile import Tile
from .point2 import Point2
from .block import Block
from .tile import TileRotation
from utils import read_num, JavaTypes, read_utf, read_obj


class Schematic: # Read only for now
    def __init__(self, version: int, width: int, height: int, tags: dict[str, str], tiles: list[Tile]):
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
    def tiles(self) -> list[Tile]:
        return self._tiles.copy()

    def save_preview(self, filename: str = "preview.png") -> None:
        preview = Image.new("RGBA", (self.width*32, self.height*32), (0, 0, 0, 0))
        for tile in self._tiles:
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
            blocks.append(name)

        game_blocks = {name: Block(name, "", 1) for name in blocks} # TODO: replace with actual blocks

        total_blocks = read_num(decom, JavaTypes.INT)
        tiles: list[Tile] = []
        for _ in range(total_blocks):
            index = read_num(decom, JavaTypes.BYTE)
            point = Point2.unpack(read_num(decom, JavaTypes.INT))
            cfg = read_obj(decom)
            rot = read_num(decom, JavaTypes.BYTE) % 4
            tiles.append(Tile(point, game_blocks[blocks[index]], TileRotation.from_int(rot), cfg))

        return Schematic(ver, width, height, tags, tiles)

    @staticmethod
    def from_b64(b64: str) -> "Schematic":
        return Schematic.from_file(BytesIO(bytes(b64, "utf-8")))

if __name__ == "__main__":
    from rich import inspect
    f = open("test.msch", "rb")
    s = Schematic.from_file(f)
    s.save_preview()
    inspect(s)