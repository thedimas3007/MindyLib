from typing import Optional, TypeAlias, Union

from PIL import Image

import g_types # Not importing schematic directly in order to avoid circular import
from g_types.tile import Tile, TileRotation
from utils import get_sprite, tint_image, add_outline, parse_color

LayerLike: TypeAlias = Union[tuple[str, str], Image.Image, "Layer"]

class Layer:
    def __init__(self, layer: LayerLike) -> None:
        self.layer = layer

    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        return Layer.convert(self.layer, schematic, tile)

    @staticmethod
    def convert(layer: LayerLike, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        if isinstance(layer, Image.Image):
            return layer
        elif isinstance(layer, Layer):
            return layer.render(schematic, tile)
        cat, name = layer
        name = name.replace("%id%", tile.block.id)
        return get_sprite(cat, name)

class EmptyLayer(Layer):
    def __init__(self):
        super().__init__(Image.new("RGBA", (0, 0), (0, 0, 0, 0)))

class RotatedLayer(Layer):
    def __init__(self, light: LayerLike, dark: Optional[LayerLike] = None, shift: int = 0) -> None:
        super().__init__(light)
        self.dark = dark
        self.shift = shift

    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        rotated = (tile.rot + self.shift)
        if rotated in [TileRotation.BOTTOM, TileRotation.LEFT] and self.dark is not None:
            return Layer.convert(self.dark, schematic, tile).rotate(rotated.value * 90)
        else:
            return Layer.convert(self.layer, schematic, tile).rotate(rotated.value * 90)

class ItemConfigLayer(Layer):
    def __init__(self):
        super().__init__(EmptyLayer())

    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        if tile.config:
            return Image.new("RGBA", (32,32), tile.config.tuple_color)
        else:
            return get_sprite("distribution", "cross-full")

class ItemTintedLayer(Layer):
    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        if tile.config:
            img = Layer.convert(self.layer, schematic, tile)
            return tint_image(img, tile.config.tuple_color)
        else:
            return EmptyLayer().render(schematic, tile)

class OutlinedLayer(Layer):
    def __init__(self, layer: LayerLike, color: tuple[int, int, int] | int, thickness: int) -> None:
        super().__init__(layer)
        if isinstance(color, int):
            color = parse_color(color)
        self.color = color
        self.thickness = thickness

    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        img = Layer.convert(self.layer, schematic, tile)
        return add_outline(img, self.color, self.thickness)

class LayeredBlock:
    def __init__(self, layers: list[Layer]):
        self.layers = layers

    def render(self, schematic: g_types.schematic.Schematic, tile: Tile) -> Image.Image:
        if len(self.layers) == 0:
            return EmptyLayer().render(schematic, tile)
        base = self.layers[0].render(schematic, tile)
        for layer in self.layers:
            rendered = layer.render(schematic, tile)
            base.paste(rendered, (0, 0), rendered)
        return base

# TODO: ConveyorLayer ??

# mass_driver = LayeredBlock([
#     Layer(("distribution", "%id%-base")),
#     OutlinedLayer(("distribution", "%id%"), 0x3f3f3f, 3)
# ])
#
# sorter = LayeredBlock([
#     ItemConfigLayer(),
#     Layer(("distribution", "%id%")),
# ])
#
# uduct_unloader = LayeredBlock([
#     Layer(("distribution/ducts", "%id%")),
#     ItemTintedLayer(("distribution/ducts", f"%id%-center")),
#     RotatedLayer(("distribution/ducts", f"%id%-top"))
# ])

