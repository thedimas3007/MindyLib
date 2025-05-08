from enum import Flag, Enum, auto

from .point2 import Point2
from .block import Block, BlockOutputDirection, BlockOutput

class TileRotation(Flag):
    RIGHT = 0
    UP = 1
    LEFT = 2
    BOTTOM = 3

    def __add__(self, other):
        if isinstance(other, TileRotation):
            return TileRotation.from_int((self.value + other.value) % 4)
        elif isinstance(other, int):
            return TileRotation.from_int((self.value + other) % 4)
        else:
            raise TypeError("other must be of type TileRotation")

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
    TOP = (0, 1)
    BOTTOM = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @property
    def offset(self) -> tuple[int, int]:
        return self.value

    def __str__(self):
        return self.name.lower()

    def inverted(self):
        return {
            Direction.TOP: Direction.BOTTOM,
            Direction.BOTTOM: Direction.TOP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }[self]

    def is_horizontal(self) -> bool:
        return self in [Direction.LEFT, Direction.RIGHT]

    def is_vertical(self) -> bool:
        return self in [Direction.TOP, Direction.BOTTOM]

    @staticmethod
    def from_rotation(rotation: TileRotation):
        return {
            TileRotation.UP: Direction.TOP,
            TileRotation.BOTTOM: Direction.BOTTOM,
            TileRotation.LEFT: Direction.LEFT,
            TileRotation.RIGHT: Direction.RIGHT,
        }[rotation]

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

    def rotated_output(self) -> tuple[Direction]:
        if self.block.output == BlockOutput.NONE or self.block.output_direction == BlockOutputDirection.NONE:
            return tuple()
        output_directions = []

        if BlockOutputDirection.FRONT & self.block.output_direction:
            if self.rot == TileRotation.RIGHT:
                output_directions.append(Direction.RIGHT)
            elif self.rot == TileRotation.UP:
                output_directions.append(Direction.TOP)
            elif self.rot == TileRotation.LEFT:
                output_directions.append(Direction.LEFT)
            elif self.rot == TileRotation.BOTTOM:
                output_directions.append(Direction.BOTTOM)

        if BlockOutputDirection.RIGHT & self.block.output_direction:
            if self.rot == TileRotation.RIGHT:
                output_directions.append(Direction.BOTTOM)
            elif self.rot == TileRotation.UP:
                output_directions.append(Direction.RIGHT)
            elif self.rot == TileRotation.LEFT:
                output_directions.append(Direction.TOP)
            elif self.rot == TileRotation.BOTTOM:
                output_directions.append(Direction.LEFT)

        if BlockOutputDirection.REAR & self.block.output_direction:
            if self.rot == TileRotation.RIGHT:
                output_directions.append(Direction.LEFT)
            elif self.rot == TileRotation.UP:
                output_directions.append(Direction.BOTTOM)
            elif self.rot == TileRotation.LEFT:
                output_directions.append(Direction.RIGHT)
            elif self.rot == TileRotation.BOTTOM:
                output_directions.append(Direction.TOP)

        if BlockOutputDirection.LEFT & self.block.output_direction:
            if self.rot == TileRotation.RIGHT:
                output_directions.append(Direction.TOP)
            elif self.rot == TileRotation.UP:
                output_directions.append(Direction.LEFT)
            elif self.rot == TileRotation.LEFT:
                output_directions.append(Direction.BOTTOM)
            elif self.rot == TileRotation.BOTTOM:
                output_directions.append(Direction.RIGHT)

        return tuple(output_directions)

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
