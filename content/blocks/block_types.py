from PIL import Image

from g_types.tile import TileRotation
from g_types.block import Block, BlockOutput, BlockOutputDirection
from utils import add_outline, get_sprite, tint_image

_sharded_color = (0xff, 0xd2, 0x7e)

class StackConveyor(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, power_consumption=0.0):
        super().__init__(name, "distribution/stack-conveyors", size, cost, output, output_direction, power_consumption)

    def sprite(self, schematic, tile) -> Image.Image:
        BOD = BlockOutputDirection
        inputs = schematic.rotated_inputs(tile.pos, StackConveyor)
        outputs = schematic.rotated_outputs(tile.pos, StackConveyor, True)

        input_mask = (BOD.LEFT | BOD.BOTTOM | BOD.RIGHT)
        output_mask = (BOD.LEFT | BOD.TOP | BOD.RIGHT)
        n = 0

        first = False
        if not outputs & BOD.TOP: # No frontal outputs - last block of the chain
            n = 2
        elif inputs & input_mask: # Any input - middle block
            n = 0
        elif inputs & input_mask == BOD.NONE: # No input - start block
            n = 1
            first = True
        else: # No match - fallback
            print(f"ERROR: No 'n' for {tile.pos}")
            n = 1

        angles = {
            BOD.TOP: 0,
            BOD.LEFT: 90,
            BOD.BOTTOM: 180,
            BOD.RIGHT: 270
        }

        img = get_sprite(self.category, f"{self.id}-{n}")
        edge = get_sprite(self.category, f"{self.id}-edge")

        all_inputs = schematic.rotated_inputs(tile.pos)
        for s in (BOD.TOP, BOD.RIGHT, BOD.BOTTOM, BOD.LEFT):
            if s == BOD.TOP and outputs & BOD.TOP:
                pass # Skip top if the conveyor isn't the last one
            elif not ((s & inputs) or (first and (s & all_inputs))):
                rotated = edge.rotate(angles[s])
                img.paste(rotated, (0,0), rotated)

        # print(f"{tile.pos}\ti={inputs}\to={outputs}\tn={n}")
        return img.rotate(tile.rot.value * 90)

class BridgeConveyor(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "distribution", size, cost, output, output_direction, power_consumption)

class DuctBridge(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, power_consumption=0.0, max_range=0):
        super().__init__(name, "distribution/ducts", size, cost, output, output_direction, power_consumption)
        self.max_range = max_range

    def sprite(self, schematic, tile) -> Image.Image:
        img = get_sprite(self.category, self.id)
        top = get_sprite(self.category, f"{self.id}-dir")
        top = top.rotate(tile.rot.value * 90)
        img.paste(top, (0,0), top)
        return img

class Pump(Block):
    def __init__(self, name, size, cost, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, "liquid", size, cost, output, output_direction, power_consumption)

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
