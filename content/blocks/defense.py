from g_types.block import Block
from .. import items

defense_category = "defense"
wall_category = "walls"

class DefenseBlock(Block):
    def __init__(self, name, size, cost, power_consumption=0.0, category=defense_category, **kwargs):
        super().__init__(name, category, size, cost, power_consumption=power_consumption, **kwargs)
    
class Wall(DefenseBlock):
    def __init__(self, name, size, cost, power_consumption=0.0, **kwargs):
        super().__init__(name, size, cost, power_consumption=power_consumption, category=wall_category, **kwargs)


copper_wall = Wall("Copper Wall", 1, {
    items.copper: 6
})

copper_wall_large = Wall("Copper Wall Large", 2, copper_wall.cost * 4)

titanium_wall = Wall("Titanium Wall", 1, {
    items.titanium: 6
})

titanium_wall_large = Wall("Titanium Wall Large", 2, titanium_wall.cost * 4)

plastanium_wall = Wall("Plastanium Wall", 1, {
    items.plastanium: 5,
    items.metaglass: 2
})

plastanium_wall_large = Wall("Plastanium Wall Large", 2, plastanium_wall.cost * 4)

thorium_wall = Wall("Thorium Wall", 1, {
    items.thorium: 6
})

thorium_wall_large = Wall("Thorium Wall Large", 2, thorium_wall.cost * 4)

phase_wall = Wall("Phase Wall", 1, {
    items.phase_fabric: 6
})

phase_wall_large = Wall("Phase Wall Large", 2, phase_wall.cost * 4)

surge_wall = Wall("Surge Wall", 1, {
    items.surge_alloy: 6
})

surge_wall_large = Wall("Surge Wall Large", 2, surge_wall.cost * 4)

door = Wall("Door", 1, {
    items.titanium: 6,
    items.silicon: 4
})

door_large = Wall("Door Large", 2, door.cost * 4)

scrap_wall = Wall("Scrap Wall", 1, {
    items.scrap: 6
})

scrap_wall_large = Wall("Scrap Wall Large", 2, scrap_wall.cost * 4)

scrap_wall_huge = Wall("Scrap Wall Huge", 3, surge_wall.cost * 9)

scrap_wall_gigantic = Wall("Scrap Wall Gigantic", 4, scrap_wall.cost * 16)

thruster = Wall("Thruster", 4, {
    items.scrap: 96
})

beryllium_wall = Wall("Beryllium Wall", 1, {
    items.beryllium: 6
})

beryllium_wall_large = Wall("Beryllium Wall Large", 4, beryllium_wall.cost * 4)

tungsten_wall = Wall("Tungsten Wall", 1, {
    items.tungsten: 6
})

tungsten_wall_large = Wall("Tungsten Wall Large", 2, tungsten_wall.cost * 4)

blast_door = Wall("Blast Door", 2, {
    items.tungsten: 24,
    items.silicon: 24
})

reinforced_surge_wall = Wall("Reinforced Surge Wall", 1, {
    items.surge_alloy: 6,
    items.tungsten: 2
})

reinforced_surge_wall_large = Wall("Reinforced Surge Wall Large", 2, reinforced_surge_wall.cost * 4)

carbide_wall = Wall("Carbide Wall", 1, {
    items.thorium: 6,
    items.carbide: 6
})

carbide_wall_large = Wall("Carbide Wall Large", 2, carbide_wall.cost * 4)

shielded_wall = Wall("Shielded Wall", 2, {
    items.phase_fabric: 20,
    items.surge_alloy: 12
}, power_consumption=3/60)

defense_blocks = [
    copper_wall, copper_wall_large, titanium_wall, titanium_wall_large,
    plastanium_wall, plastanium_wall_large, thorium_wall, thorium_wall_large,
    phase_wall, phase_wall_large, surge_wall, surge_wall_large,
    door, door_large, scrap_wall, scrap_wall_large, scrap_wall_huge, scrap_wall_gigantic,
    thruster, beryllium_wall, beryllium_wall_large, tungsten_wall, tungsten_wall_large,
    blast_door, reinforced_surge_wall, reinforced_surge_wall_large,
    carbide_wall, carbide_wall_large, shielded_wall
]
