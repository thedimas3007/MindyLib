from typing import Optional, TypeAlias, Union

from PIL import Image

import g_types # Not importing schematic directly in order to avoid circular import
from g_types import Item

# from content.blocks import block_types
from g_types.block import BlockOutputDirection, BlockOutput
from g_types.item_cost import ItemCost
from g_types.tile import Tile, TileRotation
from string_utils import space_to_kebab
from utils import get_sprite, tint_image, add_outline, parse_color, pack_color

LayerLike: TypeAlias = Union[str | tuple[str, str], Image.Image, "Layer"]

# Support for per-team rendering eventually?
team_colors = [0xffd37f, 0xeab678, 0xd4816b]

class Layer:
    def __init__(self, layer: LayerLike = "@") -> None:
        self.layer = layer

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        return Layer.convert(self.layer, schematic, tile)

    @staticmethod
    def convert(layer: LayerLike, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        if isinstance(layer, Image.Image):
            return layer
        elif isinstance(layer, Layer):
            return layer.render(schematic, tile)
        elif isinstance(layer, tuple):
            cat, name = layer
            name = name.replace("@", tile.block.id, 1)
            return get_sprite(cat, name)
        elif isinstance(layer, str):
            name = layer.replace("@", tile.block.id, 1)
            return get_sprite(tile.block.category, name)
        else:
            raise TypeError(f"unknown layer type: {type(layer)}")

class EmptyLayer(Layer):
    def __init__(self):
        super().__init__(Image.new("RGBA", (0, 0), (0, 0, 0, 0)))

class RotatedLayer(Layer):
    def __init__(self, light: LayerLike, dark: Optional[LayerLike] = None, shift: int = 0) -> None:
        super().__init__(light)
        self.dark = dark
        self.shift = shift

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        rotated = (tile.rot + self.shift)
        if rotated in [TileRotation.BOTTOM, TileRotation.LEFT] and self.dark is not None:
            return Layer.convert(self.dark, schematic, tile).rotate(rotated.value * 90)
        else:
            return Layer.convert(self.layer, schematic, tile).rotate(rotated.value * 90)

class ItemConfigLayer(Layer):
    def __init__(self):
        super().__init__(EmptyLayer())

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        if tile.config:
            return Image.new("RGBA", (32,32), tile.config.tuple_color)
        else:
            return get_sprite("distribution", "cross-full")

class ItemTintedLayer(Layer):
    def __init__(self, center: LayerLike, arrow: Optional[LayerLike] = None) -> None:
        super().__init__(center)
        self.arrow = arrow

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        if tile.config:
            img = Layer.convert(self.layer, schematic, tile)
            return tint_image(img, tile.config.tuple_color)
        else:
            if self.arrow:
                img = Layer.convert(self.arrow, schematic, tile).rotate(tile.rot.value * 90)
                return img
            else:
                return EmptyLayer().render(schematic, tile)

class OutlinedLayer(Layer):
    def __init__(self, layer: LayerLike, color: tuple[int, int, int] | int, thickness: int) -> None:
        super().__init__(layer)
        if isinstance(color, int):
            color = parse_color(color)
        self.color = color
        self.thickness = thickness

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        img = Layer.convert(self.layer, schematic, tile)
        return add_outline(img, self.color, self.thickness)

class TeamLayer(Layer):
    def __init__(self, layer: LayerLike = "@-team") -> None:
        super().__init__(layer)

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        img = Layer.convert(self.layer, schematic, tile)
        tinted = Image.new("RGBA", img.size, (0, 0, 0, 0))
        pixels = img.load()
        for y in range(img.height):
            for x in range(img.width):
                tint_color = pixels[x, y]
                r, g, b, a = pixels[x, y]
                color = pack_color(r, g, b)
                if color == 0xffffff:
                    tint_color = parse_color(team_colors[0])
                elif color in [0xdcc6c6, 0xdbc5c5]:
                    tint_color = parse_color(team_colors[1])
                elif color in [0x9d7f7f, 0x9e8080]:
                    tint_color = parse_color(team_colors[2])
                tinted.putpixel((x, y), tint_color)
        return tinted

class ConveyorLayer(Layer):
    def __init__(self, layer: LayerLike = "@-#-0", strict: bool = False) -> None:
        super().__init__(layer)
        self.strict = strict

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        if isinstance(self.layer, str):
            cat = tile.block.category
            name = self.layer
        elif isinstance(self.layer, tuple):
            cat, name = self.layer
        else:
            raise TypeError(f"unknown layer type: {type(self.layer)}")

        BOD = BlockOutputDirection
        inputs = schematic.rotated_inputs(tile.pos, type(tile.block) if self.strict else None)
        mask = (BOD.LEFT | BOD.BOTTOM | BOD.RIGHT)

        n = 0
        flip = None

        if inputs & BOD.LEFT:
            if inputs & BOD.RIGHT:
                if inputs & BOD.BOTTOM:
                    n = 3  # LEFT + RIGHT + BOTTOM
                else:
                    n = 4  # LEFT + RIGHT
            elif inputs & BOD.BOTTOM:
                n = 2
                flip = Image.FLIP_TOP_BOTTOM  # LEFT + BOTTOM
            else:
                n = 1  # LEFT only

        elif inputs & BOD.RIGHT:
            if inputs & BOD.BOTTOM:
                n = 2  # RIGHT + BOTTOM
            else:
                n = 1
                flip = Image.FLIP_TOP_BOTTOM  # RIGHT only

        elif (inputs & (BOD.LEFT | BOD.RIGHT)) == BOD.NONE:
            n = 0

        else:
            print(f"ERROR: No 'n' for {tile.pos}")

        name = name.replace("@", tile.block.id).replace("#", str(n))
        img = get_sprite(cat, name)
        if flip:
            img = img.transpose(flip)
        return img.rotate(tile.rot.value * 90)

class ConditionalLayer(Layer):
    def __init__(self, true: LayerLike, false: Optional[LayerLike] = None, inverted: bool = False) -> None:
        super().__init__(true)
        self.false = false or EmptyLayer()
        self.inverted = inverted

    def render(self, schematic: "g_types.schematic.Schematic", tile: Tile) -> Image.Image:
        if tile.config:
            return Layer.render(self.layer if not self.inverted else self.false, schematic, tile)
        else:
            return Layer.render(self.false if not self.inverted else self.layer, schematic, tile)


class LayeredBlock:
    def __init__(self, name: str, category: str, size: int, cost: dict[Item, int] | ItemCost,
                 output: BlockOutput = BlockOutput.NONE, output_direction: BlockOutputDirection = BlockOutputDirection.NONE,
                 power_consumption: float = 0.0, layers: list[Layer] = None):
        self.id = space_to_kebab(name)
        self.name = name
        self.category = category
        self.size = size
        self.cost = cost if isinstance(cost, ItemCost) else ItemCost(cost)
        self.output = output
        self.output_direction = output_direction
        self.power_consumption = power_consumption
        self.layers = layers or [Layer("@")]

    @property
    def energy_usage(self) -> float:
        return self.power_consumption * 60

    def sprite(self, schematic, tile) -> Image.Image: # TODO: rename to render
        if len(self.layers) == 0:
            return EmptyLayer().render(schematic, tile)
        base = self.layers[0].render(schematic, tile)
        for layer in self.layers:
            rendered = layer.render(schematic, tile)
            base.paste(rendered, (0, 0), rendered)
        return base

    def __str__(self):
        return f"LayeredBlock(\"{self.name}\", \"{self.category}\", {self.size}, {self.cost}, {self.output}, {self.output_direction}, {self.power_consumption})"

    def __repr__(self):
        return self.__str__()
