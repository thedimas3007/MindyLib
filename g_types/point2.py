from typing import Union


class Point2: # TODO: floats
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def cast_to_int(x):
        return x - (1 << 16) if x >= (1 << 15) else x

    @staticmethod
    def x(pos):
        return Point2.cast_to_int(pos >> 16)

    @staticmethod
    def y(pos):
        return Point2.cast_to_int(pos & 0xFFFF)

    @staticmethod
    def pack(x, y):
        return (x << 16) | (y & 0xFFFF)

    @staticmethod
    def unpack(point):
        return Point2(Point2.x(point), Point2.y(point))

    def pack_self(self):
        return Point2.pack(self.x, self.y)

    @staticmethod
    def convert(t) -> "Point2":
        if not (isinstance(t, Point2) or isinstance(t, tuple)):
            raise TypeError("parameter must be of type Point2 or tuple[int, int]")
        if isinstance(t, tuple):
            if len(t) != 2 or not all(isinstance(i, int) for i in t):
                raise TypeError("tuple must contain exactly two integers")
            t = Point2(*t)
        return t

    def __str__(self):
        return f"Point2({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Union["Point2", tuple[int, int]]):
        other = Point2.convert(other)
        return self.x == other.x and self.y == other.y

    def __gt__(self, other: Union["Point2", tuple[int, int]]):
        other = Point2.convert(other)
        return self.x > other.x and self.y > other.y

    def __lt__(self, other: Union["Point2", tuple[int, int]]):
        other = Point2.convert(other)
        return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        other = Point2.convert(other)
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        other = Point2.convert(other)
        return self.x <= other.x and self.y <= other.y

    def __add__(self, other):
        other = Point2.convert(other)
        return Point2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union["Point2", tuple[int, int]]):
        other = Point2.convert(other)
        return Point2(self.x - other.x, self.y - other.y)

    # def __mul__(self, other): # TODO: implement or remove
    #     if not(isinstance(other, int) or isinstance(other, float)):
    #         raise TypeError("other must be of type int or float")
    #     return Point2(round(self.x * other, self.y * other)