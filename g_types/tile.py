from enum import Flag, auto

from g_types import Point2, Block

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
        return f"Tile({self.pos}, \"{self.block.name}\", {self.rot}, {self.config})"

    def __repr__(self):
        return self.__str__()