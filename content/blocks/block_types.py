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
        mask = (BOD.LEFT | BOD.BOTTOM | BOD.RIGHT).value

        n = 0
        if (inputs & (BOD.LEFT | BOD.RIGHT).value) == BOD.NONE.value:
            n = 0
        elif (inputs & mask) == BOD.LEFT.value:
            n = 1
        elif (inputs & mask) == (BOD.BOTTOM | BOD.RIGHT).value:
            n = 2
        elif (inputs & mask) == (BOD.LEFT | BOD.RIGHT | BOD.BOTTOM).value:
            n = 3
        elif (inputs & mask) == (BOD.LEFT | BOD.RIGHT).value:
            n = 4
        else:
            print(f"ERROR: No 'n' for {tile.pos}")
        # print(f"{tile.pos}:\ti={inputs:#06b}, m={mask:#06b}, m={n}")
        img = Image.open(self._sprite_path(f"{self.id}-{n}-0")) # second zero is just animation frame; GIFs anyone? :P
        if tile.rot == TileRotation.LEFT:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        return img

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
