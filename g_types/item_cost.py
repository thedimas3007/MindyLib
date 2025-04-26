from . import Item


class ItemCost:
    def __init__(self, price: dict[Item, int]):
        self.price = price

    def get_for(self, item: Item) -> int:
        return self.price[item] if item in self.price else 0

    def __str__(self):
        return f"ItemCost(price={self.price})"

    def __repr__(self):
        return self.__str__()