from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import Turret
from .. import items

category = "turrets"
defense_category = "defense"

duo = Turret("Duo", 1, {
    items.copper: 35,
})

scatter = Turret("Scatter", 2, {
    items.copper: 85,
    items.lead: 45,
})

scorch = Turret("Scorch", 1, {
    items.copper: 25,
    items.graphite: 22,
})

hail = Turret("Hail", 1, {
    items.copper: 40,
    items.graphite: 17,
})

wave = Turret("Wave", 2, {
    items.metaglass: 45,
    items.lead: 75,
})

lancer = Turret("Lancer", 2, {
    items.copper: 60,
    items.lead: 70,
    items.silicon: 50,
})

arc = Turret("Arc", 1, {
    items.copper: 50,
    items.lead: 50,
})

parallax = Turret("Parallax", 2, {
    items.silicon: 120,
    items.titanium: 90,
    items.graphite: 30,
})

swarmer = Turret("Swarmer", 2, {
    items.graphite: 35,
    items.titanium: 35,
    items.plastanium: 45,
    items.silicon: 30,
})

salvo = Turret("Salvo", 2, {
    items.copper: 100,
    items.graphite: 80,
    items.titanium: 50,
})

segment = Turret("Segment", 2, {
    items.silicon: 130,
    items.thorium: 80,
    items.phase_fabric: 40,
})

tsunami = Turret("Tsunami", 3, {
    items.metaglass: 100,
    items.lead: 400,
    items.titanium: 250,
    items.thorium: 100,
})

fuse = Turret("Fuse", 3, {
    items.copper: 225,
    items.graphite: 225,
    items.thorium: 100,
})

ripple = Turret("Ripple", 3, {
    items.copper: 150,
    items.graphite: 135,
    items.titanium: 60,
})

cyclone = Turret("Cyclone", 3, {
    items.copper: 200,
    items.titanium: 125,
    items.plastanium: 80,
})

foreshadow = Turret("Foreshadow", 4, {
    items.copper: 1000,
    items.metaglass: 600,
    items.surge_alloy: 300,
    items.plastanium: 200,
    items.silicon: 600,
})

spectre = Turret("Spectre", 4, {
    items.copper: 900,
    items.graphite: 300,
    items.surge_alloy: 250,
    items.plastanium: 175,
    items.thorium: 250,
})

meltdown = Turret("Meltdown", 4, {
    items.copper: 1200,
    items.lead: 350,
    items.graphite: 300,
    items.surge_alloy: 325,
    items.silicon: 325,
})

breach = Turret("Breach", 3, {
    items.beryllium: 150,
    items.silicon: 150,
    items.graphite: 250,
}, reinforced=True)

diffuse = Turret("Diffuse", 3, {
    items.beryllium: 150,
    items.silicon: 200,
    items.graphite: 200,
    items.tungsten: 50,
}, reinforced=True)

sublimate = Turret("Sublimate", 3, {
    items.tungsten: 150,
    items.silicon: 200,
    items.oxide: 40,
    items.beryllium: 400,
}, reinforced=True)

titan = Turret("Titan", 4, {
    items.tungsten: 250,
    items.silicon: 300,
    items.thorium: 400,
}, reinforced=True)

disperse = Turret("Disperse", 4, {
    items.thorium: 50,
    items.oxide: 150,
    items.silicon: 200,
    items.beryllium: 350,
}, reinforced=True)

afflict = Turret("Afflict", 4, {
    items.surge_alloy: 100,
    items.silicon: 200,
    items.graphite: 250,
    items.oxide: 40,
}, power_consumption=2, reinforced=True)

lustre = Turret("Lustre", 4, {
    items.silicon: 250,
    items.graphite: 200,
    items.oxide: 50,
    items.carbide: 90,
}, reinforced=True)

scathe = Turret("Scathe", 4, {
    items.silicon: 300,
    items.graphite: 400,
    items.tungsten: 450,
    items.carbide: 250,
}, reinforced=True)

smite = Turret("Smite", 5, {
    items.oxide: 200,
    items.surge_alloy: 400,
    items.silicon: 800,
    items.carbide: 500,
    items.phase_fabric: 300,
}, reinforced=True)

malign = Turret("Malign", 5, {
    items.carbide: 400,
    items.beryllium: 2000,
    items.silicon: 800,
    items.graphite: 800,
    items.phase_fabric: 300,
}, power_consumption=5, reinforced=True)

all_blocks = [
    duo, scatter, scorch, hail, wave, lancer, arc, parallax, swarmer, salvo,
    segment, tsunami, fuse, ripple, cyclone, foreshadow, spectre, meltdown,
    breach, diffuse, sublimate, titan, disperse, afflict, lustre, scathe,
    smite, malign
]
