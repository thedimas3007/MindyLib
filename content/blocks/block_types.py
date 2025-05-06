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
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, power_consumption=0.0, strict=False):
        super().__init__(name, "distribution/conveyors", size, cost, output, output_direction, power_consumption)
        self.strict = strict

    def sprite(self, schematic, tile) -> Image.Image:
        BOD = BlockOutputDirection
        inputs = schematic.rotated_inputs(tile.pos, Conveyor if self.strict else None)
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
        if flip:
            img = img.transpose(flip)
        return img.rotate(tile.rot.value * 90)

class StackConveyor(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, power_consumption=0.0):
        super().__init__(name, "distribution/stack-conveyors", size, cost, output, output_direction, power_consumption)

    def sprite(self, schematic, tile) -> Image.Image:
        BOD = BlockOutputDirection
        inputs = schematic.rotated_inputs(tile.pos, StackConveyor)
        outputs = schematic.rotated_outputs(tile.pos, StackConveyor)
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

        img = Image.open(self._sprite_path(f"{self.id}-{n}")).convert("RGBA")
        edge = Image.open(self._sprite_path(f"{self.id}-edge")).convert("RGBA")

        all_inputs = schematic.rotated_inputs(tile.pos)
        for s in (BOD.TOP, BOD.RIGHT, BOD.BOTTOM, BOD.LEFT):
            if s == BOD.TOP and outputs & BOD.TOP:
                pass # Skip top if the conveyor isn't the last one
            elif not ((s & inputs) or (first and (s & all_inputs))):
                rotated = edge.rotate(angles[s])
                img.paste(rotated, (0,0), rotated)

        print(f"{tile.pos}\ti={inputs}\to={outputs}\tn={n}")
        return img.rotate(tile.rot.value * 90)


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
