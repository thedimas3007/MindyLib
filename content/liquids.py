from typing import Optional

from g_types.liquid import Liquid

water = Liquid("Water", 0x596ab8)
slag = Liquid("Slag", 0xffa166)
oil = Liquid("Oil", 0x313131)
cryofluid = Liquid("Cryofluid", 0x6ecdec)
neoplasm = Liquid("Neoplasm", 0xc33e2b)
arkycite = Liquid("Arkycite", 0x84a94b)
gallium = Liquid("Gallium", 0x9a9dbf)
ozone = Liquid("Ozone", 0xfc81dd)
hydrogen = Liquid("Hydrogen", 0x9eabf7)
nitrogen = Liquid("Nitrogen", 0xefe3ff)
cyanogen = Liquid("Cyanogen", 0x89e8b6)

all_liquids = [
    water, slag, oil, cryofluid, neoplasm, arkycite, gallium, ozone, hydrogen, nitrogen, cyanogen
]

def get_liquid(id: str) -> Optional[Liquid]:
    return next((i for i in all_liquids if i.id == id), None)

def get_liquid_by_code(code: int) -> Optional[Liquid]:
    return all_liquids[code] if code < len(all_liquids) else None

if __name__ == "__main__":
    from rich.pretty import pprint
    pprint(all_liquids)