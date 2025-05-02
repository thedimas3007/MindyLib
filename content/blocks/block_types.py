from PIL import Image

from g_types.tile import TileRotation
from g_types.block import Block, BlockOutput, BlockOutputDirection

class Pad(Block):
    def __init__(self, name, size, cost, power_consumption=0.0):
        super().__init__(name, "campaign", size, cost, power_consumption=power_consumption)

class StorageBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0):
        super().__init__(name, "storage", size, cost, output, output_direction, power_consumption)

class GenericCrafter(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0):
        super().__init__(name, "production", size, cost, output, output_direction, power_consumption)

class DefenseBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0, category="defense"):
        super().__init__(name, category, size, cost, output, output_direction, power_consumption)

class Wall(DefenseBlock):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0):
        super().__init__(name, size, cost, output, output_direction, power_consumption, "walls")

class TransportBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "distribution", size, cost, output, output_direction, power_consumption)

class Conveyor(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "distribution/conveyors", size, cost, output, output_direction, power_consumption)

    def sprite(self, schematic, tile) -> Image.Image:
        BOD = BlockOutputDirection
        inputs = schematic.get_relative_inputs(tile.pos)
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
        print(f"{tile.pos}:\ti={inputs}\tn={n}")
        img = Image.open(self._sprite_path(f"{self.id}-{n}-0")) # second zero is just animation frame; GIFs anyone? :P
        if tile.rot == TileRotation.LEFT:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        if flip:
            img = img.transpose(flip)
        return img.rotate(tile.rot.value * 90, expand=True)

class Sorter(TransportBlock):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, size, cost, output, output_direction, power_consumption)

    def sprite(self, schematic, tile) -> Image.Image:
        config = Image.open(self._sprite_path(f"cross-full")) if not tile.config else \
            Image.new("RGBA", (32,32), tile.config.tuple_color)
        sprite = Image.open(self._sprite_path())
        config.paste(sprite, (0, 0), sprite)
        return config


class Pump(Block):
    def __init__(self, name, size, cost, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "liquid", size, cost, output, output_direction, power_consumption)

class LogicBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0):
        super().__init__(name, "logic", size, cost, output, output_direction, power_consumption)

class PayloadBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0):
        super().__init__(name, "payload", size, cost, output, output_direction, power_consumption)

class Factory(Block):
    def __init__(self, name, size, cost, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=0.0):
        super().__init__(name, "units", size, cost, output, output_direction, power_consumption)

class PowerBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0):
        super().__init__(name, "power", size, cost, output, output_direction, power_consumption)

class PowerGenerator(PowerBlock):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0, power_generation=0.0):
        super().__init__(name, size, cost, output, output_direction, power_consumption)
        self.power_generation = power_generation

class Drill(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "drills", size, cost, output, output_direction, power_consumption)

class Turret(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0, reinforced=False):
        super().__init__(name, "turrets", size, cost, output, output_direction, power_consumption)
        self.reinforced = reinforced
