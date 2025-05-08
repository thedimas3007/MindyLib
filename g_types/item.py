from string_utils import space_to_kebab


class Item:
    def __init__(self, name: str, color: int):
        self.id = space_to_kebab(name)
        self.name = name
        self.color = color

    @property
    def tuple_color(self) -> tuple[int, int, int, int]:
        return self.color >> 16, self.color >> 8 & 0xff, self.color & 0xff, 255

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"Item(id=\"{self.id}\", name=\"{self.name}\", color=0x{self.color:06X})"

    def __repr__(self):
        return self.__str__()