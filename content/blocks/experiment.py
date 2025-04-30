from .defense import DefenseBlock
from .. import items

category = "defense" # All blocks used are defense ones

barrier_projector = DefenseBlock("Barrier Projector", 3, {
    items.surge_alloy: 100,
    items.silicon: 125
}, power_consumption=4)

shockwave_tower = DefenseBlock("Shockwave Tower", 3, {
    items.surge_alloy: 50,
    items.silicon: 150,
    items.oxide: 30,
    items.tungsten: 100
}, power_consumption=80/60)

shield_projector = DefenseBlock("Shield Projector", 3, {}, power_consumption=5)

large_shield_projector = DefenseBlock("Large Shield Projector", 4, {}, power_consumption=5)

experiment_blocks = [
    barrier_projector, shockwave_tower, shield_projector, large_shield_projector
]