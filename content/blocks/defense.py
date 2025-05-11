from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, Layer, RotatedLayer, ConditionalLayer
from .block_types import Wall
from .. import items

category = "walls"

copper_wall = LayeredBlock("Copper Wall", category, 1, {
    items.copper: 6
})

copper_wall_large = LayeredBlock("Copper Wall Large", category, 2, copper_wall.cost * 4)

titanium_wall = LayeredBlock("Titanium Wall", category, 1, {
    items.titanium: 6
})

titanium_wall_large = LayeredBlock("Titanium Wall Large", category, 2, titanium_wall.cost * 4)

plastanium_wall = LayeredBlock("Plastanium Wall", category, 1, {
    items.plastanium: 5,
    items.metaglass: 2
})

plastanium_wall_large = LayeredBlock("Plastanium Wall Large", category, 2, plastanium_wall.cost * 4)

thorium_wall = LayeredBlock("Thorium Wall", category, 1, {
    items.thorium: 6
})

thorium_wall_large = LayeredBlock("Thorium Wall Large", category, 2, thorium_wall.cost * 4)

phase_wall = LayeredBlock("Phase Wall", category, 1, {
    items.phase_fabric: 6
})

phase_wall_large = LayeredBlock("Phase Wall Large", category, 2, phase_wall.cost * 4)

surge_wall = LayeredBlock("Surge Wall", category, 1, {
    items.surge_alloy: 6
})

surge_wall_large = LayeredBlock("Surge Wall Large", category, 2, surge_wall.cost * 4)

door = LayeredBlock("Door", category, 1, {
    items.titanium: 6,
    items.silicon: 4
}, layers=[ConditionalLayer("@-open", "@")])

door_large = LayeredBlock("Door Large", category, 2, door.cost * 4, layers=[
    ConditionalLayer("@-open", "@")
])

scrap_wall = LayeredBlock("Scrap Wall", category, 1, {
    items.scrap: 6
})

scrap_wall_large = LayeredBlock("Scrap Wall Large", category, 2, scrap_wall.cost * 4)

scrap_wall_huge = LayeredBlock("Scrap Wall Huge", category, 3, surge_wall.cost * 9)

scrap_wall_gigantic = LayeredBlock("Scrap Wall Gigantic", category, 4, scrap_wall.cost * 16)

thruster = LayeredBlock("Thruster", category, 4, {
    items.scrap: 96
}, layers=[Layer(), RotatedLayer("@-top")])

beryllium_wall = LayeredBlock("Beryllium Wall", category, 1, {
    items.beryllium: 6
})

beryllium_wall_large = LayeredBlock("Beryllium Wall Large", category, 4, beryllium_wall.cost * 4)

tungsten_wall = LayeredBlock("Tungsten Wall", category, 1, {
    items.tungsten: 6
})

tungsten_wall_large = LayeredBlock("Tungsten Wall Large", category, 2, tungsten_wall.cost * 4)

blast_door = LayeredBlock("Blast Door", category, 2, {
    items.tungsten: 24,
    items.silicon: 24
}, layers=[ConditionalLayer("@-open", "@")])

reinforced_surge_wall = LayeredBlock("Reinforced Surge Wall", category, 1, {
    items.surge_alloy: 6,
    items.tungsten: 2
})

reinforced_surge_wall_large = LayeredBlock("Reinforced Surge Wall Large", category, 2, reinforced_surge_wall.cost * 4)

carbide_wall = LayeredBlock("Carbide Wall", category, 1, {
    items.thorium: 6,
    items.carbide: 6
})

carbide_wall_large = LayeredBlock("Carbide Wall Large", category, 2, carbide_wall.cost * 4)

shielded_wall = LayeredBlock("Shielded Wall", category, 2, {
    items.phase_fabric: 20,
    items.surge_alloy: 12
}, power_consumption=3/60)

all_blocks = [
    copper_wall, copper_wall_large, titanium_wall, titanium_wall_large,
    plastanium_wall, plastanium_wall_large, thorium_wall, thorium_wall_large,
    phase_wall, phase_wall_large, surge_wall, surge_wall_large,
    door, door_large, scrap_wall, scrap_wall_large, scrap_wall_huge, scrap_wall_gigantic,
    thruster, beryllium_wall, beryllium_wall_large, tungsten_wall, tungsten_wall_large,
    blast_door, reinforced_surge_wall, reinforced_surge_wall_large,
    carbide_wall, carbide_wall_large, shielded_wall
]
