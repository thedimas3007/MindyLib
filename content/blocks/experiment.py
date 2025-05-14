from g_types.layers import LayeredBlock, TeamLayer, Layer
from .. import items

category = "defense" # All blocks used are defense ones

barrier_projector = LayeredBlock("Barrier Projector", category, 3, {
    items.surge_alloy: 100,
    items.silicon: 125
}, power_consumption=4, layers=[
    Layer(),
    TeamLayer()
])

shockwave_tower = LayeredBlock("Shockwave Tower", category, 3, {
    items.surge_alloy: 50,
    items.silicon: 150,
    items.oxide: 30,
    items.tungsten: 100
}, power_consumption=80/60)

shield_projector = LayeredBlock("Shield Projector", category, 3, {}, power_consumption=5, layers=[
    Layer(),
    TeamLayer()
])

large_shield_projector = LayeredBlock("Large Shield Projector", category,4, {}, power_consumption=5, layers=[
    Layer(),
    TeamLayer()
])

all_blocks = [
    barrier_projector, shockwave_tower, shield_projector, large_shield_projector
]