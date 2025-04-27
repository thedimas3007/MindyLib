from content.items import all_items
from .item import Item

from content import items

class ItemCost:
    def __init__(self, cost: dict[Item, int]):
        self._cost = {k: cost[k] if k in cost else 0
                      for k in all_items}

    @property
    def cost(self):
        return self._cost.copy()

    def __getitem__(self, key: Item):
        if not isinstance(key, Item):
            raise TypeError("key must be of type Item")
        if key not in all_items:
            raise ValueError("key must be a valid item")
        return self._cost[key] if key in self._cost else 0

    def __setitem__(self, key: Item, value: int):
        if not isinstance(key, Item):
            raise TypeError("key must be of type Item")
        if not isinstance(value, int):
            raise TypeError("value must be of type int")
        if key not in all_items:
            raise ValueError("key must be a valid item")
        if value < 0:
            raise ValueError("value must be >= 0")
        self._cost[key] = value

    def __iter__(self):
        return iter(self._cost.items())

    def __str__(self):
        return f"ItemCost(price={self._cost})"

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    from rich.pretty import pprint
    from random import randint
    # cost = ItemCost({k:0 if randint(0, 1) else randint(0, 100) for k in all_items})
    cost = ItemCost({})
    pprint(cost)
    print(cost[items.copper])