from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import DefenseBlock, StorageBlock
from .. import items

category = "storage"

mender = DefenseBlock("Mender", 1, {
    items.lead: 30,
    items.copper: 25
}, power_consumption=0.3)

mend_projector = DefenseBlock("Mend Projector", 2, {
    items.lead: 100,
    items.titanium: 25,
    items.silicon: 40
}, power_consumption=1.5)

overdrive_projector = DefenseBlock("Overdrive Projector", 2, {
    items.lead: 100,
    items.titanium: 75,
    items.silicon: 75,
    items.plastanium: 30
}, power_consumption=3.5)

overdrive_dome = DefenseBlock("Overdrive Dome", 3, {
    items.lead: 200,
    items.titanium: 130,
    items.silicon: 130,
    items.plastanium: 80,
    items.surge_alloy: 120
}, power_consumption=10.0)

force_projector = DefenseBlock("Force Projector", 3, {
    items.lead: 100,
    items.titanium: 75,
    items.silicon: 125
}, power_consumption=4.0)

shock_mine = DefenseBlock("Shock Mine", 1, {
    items.lead: 25,
    items.silicon: 12
})

radar = DefenseBlock("Radar", 1, {
    items.silicon: 60,
    items.graphite: 50,
    items.beryllium: 10
}, power_consumption=0.6)

build_tower = DefenseBlock("Build Tower", 3, {
    items.silicon: 150,
    items.oxide: 40,
    items.thorium: 60
}, power_consumption=3)

regen_projector = DefenseBlock("Regen Projector", 3, {
    items.silicon: 80,
    items.tungsten: 60,
    items.oxide: 40,
    items.beryllium: 80
}, power_consumption=1)

illuminator = Block("Illuminator", "power", 1, {
    items.lead: 8,
    items.graphite: 12,
    items.silicon: 8
}, power_consumption=0.05)

core_shard = StorageBlock("Core Shard", 3, {
    items.copper: 1000,
    items.lead: 800
})

core_foundation = StorageBlock("Core Foundation", 4, {
    items.copper: 3000,
    items.lead: 3000,
    items.silicon: 2000
})

core_nucleus = StorageBlock("Core Nucleus", 5, {
    items.copper: 8000,
    items.lead: 8000,
    items.silicon: 5000,
    items.thorium: 4000
})

core_bastion = StorageBlock("Core Bastion", 4, {
    items.graphite: 1000,
    items.silicon: 1000,
    items.beryllium: 800
})

core_citadel = StorageBlock("Core Citadel", 5, {
    items.silicon: 7000,
    items.beryllium: 7000,
    items.tungsten: 4000,
    items.oxide: 2500
})

core_acropolis = StorageBlock("Core Acropolis", 6, {
    items.beryllium: 12000,
    items.silicon: 11000,
    items.tungsten: 9000,
    items.carbide: 10000,
    items.oxide: 8000
})

container = StorageBlock("Container", 2, {
    items.titanium: 100
})

vault = StorageBlock("Vault", 3, {
    items.titanium: 250,
    items.thorium: 125
})

unloader = Block("Unloader", category, 1, {
    items.titanium: 25,
    items.silicon: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

reinforced_container = StorageBlock("Reinforced Container", 2, {
    items.tungsten: 30,
    items.graphite: 40
})

reinforced_vault = StorageBlock("Reinforced Vault", 3, {
    items.tungsten: 125,
    items.thorium: 70,
    items.beryllium: 100
})

all_blocks = [
    mender, mend_projector, overdrive_projector, overdrive_dome,
    force_projector, shock_mine, radar, build_tower, regen_projector,
    core_shard, core_foundation, core_nucleus,
    core_bastion, core_citadel, core_acropolis,
    container, vault, unloader, reinforced_container, reinforced_vault,
    illuminator
]