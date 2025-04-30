from g_types.block import Block, BlockOutput, BlockOutputDirection
from .. import items

drill_category = "drills"
prod_category = "production"

class Drill(Block):
    def __init__(self, name, size, cost, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.0):
        super().__init__(name, drill_category, size, cost, output, output_direction, power_consumption)

mechanical_drill = Drill("Mechanical Drill", 2, {
    items.copper: 12
})

pneumatic_drill = Drill("Pneumatic Drill", 2, {
    items.copper: 18,
    items.graphite: 10
})

laser_drill = Drill("Laser Drill", 3, {
    items.copper: 35,
    items.graphite: 30,
    items.silicon: 30,
    items.titanium: 20
}, power_consumption=1.1)

blast_drill = Drill("Blast Drill", 4, {
    items.copper: 65,
    items.silicon: 60,
    items.titanium: 50,
    items.thorium: 75
}, power_consumption=3.0)

water_extractor = Drill("Water Extractor", 2, {
    items.metaglass: 30,
    items.graphite: 30,
    items.lead: 30
}, output=BlockOutput.LIQUID, power_consumption=1.5)

cultivator = Block("Cultivator", prod_category, 2, {
    items.copper: 25,
    items.lead: 25,
    items.silicon: 10
}, power_consumption=0.9)

oil_extractor = Drill("Oil Extractor", 3, {
    items.copper: 150,
    items.graphite: 175,
    items.lead: 115,
    items.thorium: 115,
    items.silicon: 75
}, power_consumption=3.0)

vent_condenser = Block("Vent Condenser", prod_category, 3, {
    items.graphite: 20,
    items.beryllium: 60
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.5)

cliff_crusher = Drill("Cliff Crusher", 2, {
    items.graphite: 25,
    items.beryllium: 20
}, power_consumption=11/60)

plasma_bore = Drill("Plasma Bore", 2, {
    items.beryllium: 40
}, power_consumption=0.15)

large_plasma_bore = Drill("Large Plasma Bore", 3, {
    items.silicon: 100,
    items.oxide: 25,
    items.beryllium: 100,
    items.tungsten: 70
}, power_consumption=0.8)

impact_drill = Drill("Impact Drill", 4, {
    items.silicon: 70,
    items.beryllium: 90,
    items.graphite: 60
}, power_consumption=160/60)

eruption_drill = Drill("Eruption Drill", 5, {
    items.silicon: 200,
    items.oxide: 20,
    items.tungsten: 200,
    items.thorium: 120
}, power_consumption=6)

production_blocks = [
    mechanical_drill, pneumatic_drill, laser_drill, blast_drill,
    water_extractor, oil_extractor,
    plasma_bore, large_plasma_bore, impact_drill, eruption_drill,
    cliff_crusher, cultivator, vent_condenser
]
