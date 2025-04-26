from utils import space_to_kebab

class Liquid:
    def __init__(self, name, color):
        self.id = space_to_kebab(name)
        self.name = name
        self.color = color

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"Liquid(id=\"{self.id}\", name=\"{self.name}\", color=0x{self.color:06X})"

    def __repr__(self):
        return self.__str__()
