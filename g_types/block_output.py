from enum import Flag, auto

class BlockOutput(Flag):
    NONE = 0
    ITEM = auto()
    LIQUID = auto()
    PAYLOAD = auto()
    ALL = ITEM | LIQUID | PAYLOAD

class BlockOutputDirection(Flag):
    NONE = 0
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    ALL = UP | DOWN | LEFT | RIGHT