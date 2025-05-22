from os.path import exists
from PIL import Image

from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, Layer

_sharded_color = (0xff, 0xd2, 0x7e)

class Conveyor(LayeredBlock):
    pass

class Bridge(LayeredBlock):
    pass

class DirectionalBridge(LayeredBlock):
    def __init__(self, name, category, size, cost,
                 output = BlockOutput.NONE, output_direction = BlockOutputDirection.FRONT,
                 power_consumption = 0.0, max_range = 0, layers: list[Layer] = None):
        super().__init__(name, category, size, cost, output, output_direction, power_consumption, layers)
        self.max_range = max_range
    pass

class StackConveyor(LayeredBlock):
    pass

class Conduit(LayeredBlock):
    pass

# region Old types
#### SHOULD BE REMOVED ####
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
# endregion