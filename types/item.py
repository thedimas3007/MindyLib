from utils import space_to_kebab

class Item:
    def __init__(self, name: str, color: int):
        self.id = space_to_kebab(name)
        self.name = name
        self.color = color

    def __str__(self):
        return f"Item(id=\"{self.id}\", name=\"{self.name}\", color=0x{self.color:06X})"

    def __repr__(self):
        return self.__str__()