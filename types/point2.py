class Point2:
    def __init__(self, x, y):
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

    @staticmethod
    def from_point(point):
        return Point2(Point2.x(point), Point2.y(point))

    def pack_self(self):
        return Point2.pack(self.x, self.y)

    def __str__(self):
        return f"Point2({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()
