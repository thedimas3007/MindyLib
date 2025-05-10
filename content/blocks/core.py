from g_types import BlockOutput, BlockOutputDirection
from g_types.layers import Layer, TeamLayer, ItemTintedLayer, LayeredBlock
from .. import items

category = "storage"
defense_category = "defense"

mender = LayeredBlock("Mender", defense_category, 1, {
    items.lead: 30,
    items.copper: 25
}, power_consumption=0.3)

mend_projector = LayeredBlock("Mend Projector", defense_category, 2, {
    items.lead: 100,
    items.titanium: 25,
    items.silicon: 40
}, power_consumption=1.5)

overdrive_projector = LayeredBlock("Overdrive Projector", defense_category, 2, {
    items.lead: 100,
    items.titanium: 75,
    items.silicon: 75,
    items.plastanium: 30
}, power_consumption=3.5)

overdrive_dome = LayeredBlock("Overdrive Dome", defense_category, 3, {
    items.lead: 200,
    items.titanium: 130,
    items.silicon: 130,
    items.plastanium: 80,
    items.surge_alloy: 120
}, power_consumption=10.0)

force_projector = LayeredBlock("Force Projector", defense_category, 3, {
    items.lead: 100,
    items.titanium: 75,
    items.silicon: 125
}, power_consumption=4.0, layers=[
    Layer(),
    TeamLayer(),
])

shock_mine = LayeredBlock("Shock Mine", defense_category, 1, {
    items.lead: 25,
    items.silicon: 12
})

radar = LayeredBlock("Radar", defense_category, 1, {
    items.silicon: 60,
    items.graphite: 50,
    items.beryllium: 10
}, power_consumption=0.6, layers=[
    Layer("@-base"),
    Layer()
])

build_tower = LayeredBlock("Build Tower", defense_category, 3, {
    items.silicon: 150,
    items.oxide: 40,
    items.thorium: 60
}, power_consumption=3, layers=[
    Layer("@-base"),
    Layer()
])

regen_projector = LayeredBlock("Regen Projector", defense_category, 3, {
    items.silicon: 80,
    items.tungsten: 60,
    items.oxide: 40,
    items.beryllium: 80
}, power_consumption=1, layers=[
    Layer("@-bottom"),
    Layer()
])

illuminator = LayeredBlock("Illuminator", "power", 1, {
    items.lead: 8,
    items.graphite: 12,
    items.silicon: 8
}, power_consumption=0.05)

core_shard = LayeredBlock("Core Shard", category, 3,{
    items.copper: 1000,
    items.lead: 800
}, layers=[
    Layer(),
    TeamLayer()
])

core_foundation = LayeredBlock("Core Foundation", category, 4, {
    items.copper: 3000,
    items.lead: 3000,
    items.silicon: 2000
}, layers=core_shard.layers)

core_nucleus = LayeredBlock("Core Nucleus", category, 5, {
    items.copper: 8000,
    items.lead: 8000,
    items.silicon: 5000,
    items.thorium: 4000
}, layers=core_shard.layers)

core_bastion = LayeredBlock("Core Bastion", category, 4, {
    items.graphite: 1000,
    items.silicon: 1000,
    items.beryllium: 800
}, layers=core_shard.layers)

core_citadel = LayeredBlock("Core Citadel", category, 5, {
    items.silicon: 7000,
    items.beryllium: 7000,
    items.tungsten: 4000,
    items.oxide: 2500
}, layers=core_shard.layers)

core_acropolis = LayeredBlock("Core Acropolis", category, 6, {
    items.beryllium: 12000,
    items.silicon: 11000,
    items.tungsten: 9000,
    items.carbide: 10000,
    items.oxide: 8000
}, layers=core_shard.layers)

container = LayeredBlock("Container", category, 2, {
    items.titanium: 100
}, layers=core_shard.layers)

vault = LayeredBlock("Vault", category, 3, {
    items.titanium: 250,
    items.thorium: 125
}, layers=core_shard.layers)

unloader = LayeredBlock("Unloader", category, 1, {
    items.titanium: 25,
    items.silicon: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[
    Layer(),
    ItemTintedLayer()
])

reinforced_container = LayeredBlock("Reinforced Container", category, 2, {
    items.tungsten: 30,
    items.graphite: 40
}, layers=core_shard.layers)

reinforced_vault = LayeredBlock("Reinforced Vault", category, 3, {
    items.tungsten: 125,
    items.thorium: 70,
    items.beryllium: 100
}, layers=core_shard.layers)

all_blocks = [
    mender, mend_projector, overdrive_projector, overdrive_dome,
    force_projector, shock_mine, radar, build_tower, regen_projector,
    core_shard, core_foundation, core_nucleus,
    core_bastion, core_citadel, core_acropolis,
    container, vault, unloader, reinforced_container, reinforced_vault,
    illuminator
]