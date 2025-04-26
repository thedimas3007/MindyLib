from g_types import BlockOutput, BlockOutputDirection
from utils import space_to_kebab

class Block:
    def __init__(self, name: str, category: str, size: int, output: BlockOutput = BlockOutput.NONE, output_direction: BlockOutputDirection = BlockOutputDirection.NONE, power_consumption: int = 0):
        self.id = space_to_kebab(name)
        self.name = name
        self.category = category
        self.size = size
        self.output = output
        self.output_direction = output_direction
        self.power_consumption = power_consumption

    @property
    def energy_usage(self) -> int:
        return self.power_consumption * 60