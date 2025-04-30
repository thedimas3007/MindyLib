from enum import Flag, Enum, auto

from .point2 import Point2
from .block import Block

class TileRotation(Flag):
    RIGHT = 0
    UP = auto()
    LEFT = auto()
    BOTTOM = auto()

    @staticmethod
    def from_int(i):
        if i == 0:
            return TileRotation.RIGHT
        elif i == 1:
            return TileRotation.UP
        elif i == 2:
            return TileRotation.LEFT
        elif i == 3:
            return TileRotation.BOTTOM

class Direction(Enum):
    TOP = (0, -1)
    BOTTOM = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def offset(self) -> tuple[int, int]:
        return self.value

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def all() -> list["Direction"]:
        return list(Direction)

class Tile:
    def __init__(self, pos: Point2, block: Block, rot: TileRotation, config=None):
        self.pos = pos
        self.block = block
        self.rot = rot
        self.config = config

    @property
    def x(self):
        return self.pos.x

    @property
    def y(self):
        return self.pos.y

    def __str__(self):
        return f"Tile({self.pos}, \"{self.block.name}\", {self.rot}, {repr(self.config)})"

    def __repr__(self):
        return self.__str__()

class GhostTile(Tile):
    """
    Represents a tile that is part of a multi-tile (2x2 or larger) block structure.
    Used to simplify neighbor detection.
    Not rendered. Only for internal use!
    """
    def __str__(self):
        return f"GhostTile({self.pos}, \"{self.block.name}\", {self.rot}, {repr(self.config)})"

    def __repr__(self):
        return self.__str__()
