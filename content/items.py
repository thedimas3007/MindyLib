from typing import Optional

from g_types.item import Item

copper = Item("Copper", 0xd99d73)
lead = Item("Lead", 0x8c7fa9)
metaglass = Item("Metaglass", 0xebeef5)
graphite = Item("Graphite", 0xb2c6d2)
sand = Item("Sand", 0xf7cba4)
coal = Item("Coal", 0x272727)
titanium = Item("Titanium", 0x8da1e3)
thorium = Item("Thorium", 0xf9a3c7)
scrap = Item("Scrap", 0x777777)
silicon = Item("Silicon", 0x53565c)
plastanium = Item("Plastanium", 0xcbd97f)
phase_fabric = Item("Phase Fabric", 0xf4ba6e)
surge_alloy = Item("Surge Alloy", 0xf3e979)
spore_pod = Item("Spore Pod", 0x7457ce)
blast_compound = Item("Blast Compound", 0xff795e)
pyratite = Item("Pyratite", 0xffaa5f)
beryllium = Item("Beryllium", 0x3a8f64)
tungsten = Item("Tungsten", 0x768a9a)
oxide = Item("Oxide", 0xe4ffd6)
carbide = Item("Carbide", 0x89769a)
fissile_matter = Item("Fissile Matter", 0x5e988d)
dormant_cyst = Item("Dormant Cyst", 0xdf824d)

serpulo_items = [
    copper, lead, metaglass, graphite, sand, coal, titanium, thorium, scrap,
    silicon, plastanium, phase_fabric, surge_alloy, spore_pod, blast_compound, pyratite
]

erekir_items = [
    graphite, thorium, silicon, phase_fabric, surge_alloy, sand,
    beryllium, tungsten, oxide, carbide, fissile_matter, dormant_cyst
]

all_items = serpulo_items + [i for i in erekir_items if i not in serpulo_items]

def get_item(name: str) -> Optional[Item]:
    return next((i for i in all_items if i.name == name), None)

def get_item_by_code(code: int) -> Optional[Item]:
    return all_items[code] if code < len(all_items) else None

if __name__ == "__main__":
    from rich.pretty import pprint
    pprint(all_items)