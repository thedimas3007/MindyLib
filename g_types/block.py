from enum import Flag, auto
from typing import Optional
from PIL import Image

from utils import get_sprite
from .item import Item
from .item_cost import ItemCost
# from .schematic import Schematic
# from .tile import Tile
from string_utils import space_to_kebab


class BlockOutput(Flag):
    NONE = 0
    ITEM = auto()
    LIQUID = auto()
    PAYLOAD = auto()
    ALL = ITEM | LIQUID | PAYLOAD

class BlockOutputDirection(Flag):
    NONE = 0
    TOP = FRONT = auto()
    RIGHT = auto()
    BOTTOM = REAR = auto()
    LEFT = auto()
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
    def energy_usage(self) -> float:
        return self.power_consumption * 60

    def sprite(self, schematic, tile) -> Image.Image:
        return get_sprite(self.category, self.id)

    def __str__(self):
        return f"Block(\"{self.name}\", \"{self.category}\", {self.size}, {self.cost}, {self.output}, {self.output_direction}, {self.power_consumption})"

    def __repr__(self):
        return self.__str__()
