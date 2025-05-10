from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, Layer
from .block_types import GenericCrafter, PowerBlock
from .. import items

category = "production"

graphite_press = LayeredBlock("Graphite Press", category, 2, {
    items.copper: 75,
    items.lead: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

multi_press = LayeredBlock("Multi Press", category, 3, {
    items.titanium: 100,
    items.silicon: 25,
    items.lead: 100,
    items.graphite: 50
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=1.8)

silicon_smelter = LayeredBlock("Silicon Smelter", category, 2, {
    items.copper: 30,
    items.lead: 25
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.5)

silicon_crucible = LayeredBlock("Silicon Crucible", category, 3, {
    items.titanium: 120,
    items.metaglass: 80,
    items.plastanium: 35,
    items.silicon: 60
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=4.0)

kiln = LayeredBlock("Kiln", category, 2, {
    items.copper: 60,
    items.graphite: 30,
    items.lead: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.6)

plastanium_compressor = LayeredBlock("Plastanium Compressor", category, 2, {
    items.silicon: 80,
    items.lead: 115,
    items.graphite: 60,
    items.titanium: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=3.0)

phase_weaver = LayeredBlock("Phase Weaver", category, 2, {
    items.silicon: 130,
    items.lead: 120,
    items.thorium: 75
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=5.0, layers=[
    Layer("@-bottom"),
    Layer("@-weave"),
    Layer()
])

surge_smelter = LayeredBlock("Surge Smelter", category, 3, {
    items.silicon: 80,
    items.lead: 80,
    items.thorium: 70
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=4.0)

cryofluid_mixer = LayeredBlock("Cryofluid Mixer", category, 2, {
    items.lead: 65,
    items.silicon: 40,
    items.titanium: 60
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=1.0, layers=[
    Layer("@-bottom"),
    Layer(),
])

pyratite_mixer = LayeredBlock("Pyratite Mixer", category, 2, {
    items.copper: 50,
    items.lead: 25
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.2)

blast_mixer = LayeredBlock("Blast Mixer", category, 2, {
    items.lead: 30,
    items.titanium: 20
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.4)

melter = LayeredBlock("Melter", category, 1, {
    items.copper: 30,
    items.lead: 35,
    items.graphite: 45
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=1.0, layers=[
    Layer("@-bottom"),
    Layer(),
])

separator = LayeredBlock("Separator", category, 2, {
    items.copper: 30,
    items.titanium: 25
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=1.1, layers=[
    Layer("@-bottom"),
    Layer("@-spinner"),
    Layer(),
])

disassembler = LayeredBlock("Disassembler", category, 3, {
    items.plastanium: 40,
    items.titanium: 100,
    items.silicon: 150,
    items.thorium: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=4, layers=[
    Layer("@-bottom"),
    Layer("@-spinner"),
    Layer(),
])

spore_press = LayeredBlock("Spore Press", category, 2, {
    items.lead: 35,
    items.silicon: 30
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL,  power_consumption=0.7, layers=[
    Layer("@-bottom"),
    Layer("@-piston-icon"),
    Layer(),
    Layer("@-top")
])

pulverizer = LayeredBlock("Pulverizer", category, 1, {
    items.copper: 30,
    items.lead: 25
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.5, layers=[
    Layer(),
    Layer("@-rotator"),
    Layer("@-top"),
])

coal_centrifuge = LayeredBlock("Coal Centrifuge", category, 2, {
    items.titanium: 20,
    items.graphite: 40,
    items.lead: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.7)

incinerator = LayeredBlock("Incinerator", category, 1, {
    items.graphite: 5,
    items.lead: 15
}, power_consumption=0.5)

# TODO: continue from here

silicon_arc_furnace = GenericCrafter("Silicon Arc Furnace", 3, {
    items.beryllium: 70,
    items.graphite: 80
}, power_consumption=6)

electrolyzer = GenericCrafter("Electrolyzer", 3, {
    items.silicon: 50,
    items.graphite: 40,
    items.beryllium: 130,
    items.tungsten: 80
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.LEFT | BlockOutputDirection.RIGHT, power_consumption=1)

atmospheric_concentrator = GenericCrafter("Atmospheric Concentrator", 3, {
    items.oxide: 60,
    items.beryllium: 180,
    items.silicon: 150
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=2)

oxidation_chamber = GenericCrafter("Oxidation Chamber", 3, {
    items.tungsten: 120,
    items.graphite: 100,
    items.silicon: 100,
    items.beryllium: 120
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.5)

electric_heater = GenericCrafter("Electric Heater", 2, {
    items.tungsten: 30,
    items.oxide: 30
}, power_consumption=50/60)

slag_heater = GenericCrafter("Slag Heater", 3, {
    items.tungsten: 50,
    items.oxide: 20,
    items.beryllium: 20
}, )

phase_heater = GenericCrafter("Phase Heater", 2, {
    items.oxide: 30,
    items.carbide: 30,
    items.beryllium: 30
})

heat_redirector = GenericCrafter("Heat Redirector", 3, {
    items.tungsten: 10,
    items.graphite: 10
})

heat_router = GenericCrafter("Heat Router", 3, {
    items.tungsten: 15,
    items.graphite: 10
})

slag_incinerator = GenericCrafter("Slag Incinerator", 1, {
    items.tungsten: 15
})

carbide_crucible = GenericCrafter("Carbide Crucible", 3, {
    items.tungsten: 110,
    items.thorium: 150,
    items.oxide: 60
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=2)

slag_centrifuge = GenericCrafter("Slag Centrifuge", 3, {
    items.carbide: 70,
    items.graphite: 60,
    items.silicon: 40,
    items.oxide: 40
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=2/60)

surge_crucible = GenericCrafter("Surge Crucible", 3, {
    items.silicon: 100,
    items.graphite: 80,
    items.tungsten: 80,
    items.oxide: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=2)

cyanogen_synthesizer = GenericCrafter("Cyanogen Synthesizer", 3, {
    items.carbide: 50,
    items.silicon: 80,
    items.beryllium: 90
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=2)

phase_synthesizer = GenericCrafter("Phase Synthesizer", 3, {
    items.carbide: 90,
    items.silicon: 100,
    items.thorium: 100,
    items.tungsten: 200
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=8)

heat_reactor = GenericCrafter("Heat Reactor", 3, {
    items.oxide: 70,
    items.graphite: 20,
    items.carbide: 10,
    items.thorium: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

all_blocks = [
    graphite_press, multi_press, silicon_smelter, silicon_crucible, kiln,
    plastanium_compressor, phase_weaver, surge_smelter, cryofluid_mixer,
    pyratite_mixer, blast_mixer, melter, separator, disassembler, spore_press,
    pulverizer, coal_centrifuge, incinerator, silicon_arc_furnace, electrolyzer,
    atmospheric_concentrator, oxidation_chamber, electric_heater, slag_heater,
    phase_heater, heat_redirector, heat_router, slag_incinerator, carbide_crucible,
    slag_centrifuge, surge_crucible, cyanogen_synthesizer, phase_synthesizer, heat_reactor
]
