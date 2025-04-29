from .item import Item
from .item_cost import ItemCost
from string_utils import space_to_kebab

from enum import Flag, auto

class BlockOutput(Flag):
    NONE = 0
    ITEM = auto()
    LIQUID = auto()
    PAYLOAD = auto()
    ALL = ITEM | LIQUID | PAYLOAD

class BlockOutputDirection(Flag):
    NONE = 0
    FRONT = auto()
    REAR = auto()
    LEFT = auto()
    RIGHT = auto()
    ALL = FRONT | REAR | LEFT | RIGHT

class Block:
    def __init__(self, name: str, category: str, size: int, cost: dict[Item, int] | ItemCost, output: BlockOutput = BlockOutput.NONE, output_direction: BlockOutputDirection = BlockOutputDirection.NONE, power_consumption: float = 0.0):
        self.id = space_to_kebab(name)
        self.name = name
        self.category = category
        self.size = size
        self.cost = cost if isinstance(cost, ItemCost) else ItemCost(cost)
        self.output = output
        self.output_direction = output_direction
        self.power_consumption = power_consumption

    @property
    def energy_usage(self) -> int:
        return self.power_consumption * 60