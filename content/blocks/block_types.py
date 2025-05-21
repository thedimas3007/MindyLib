from g_types.block import Block, BlockOutput, BlockOutputDirection

_sharded_color = (0xff, 0xd2, 0x7e)

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
