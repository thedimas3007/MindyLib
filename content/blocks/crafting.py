from g_types.block import Block, BlockOutput, BlockOutputDirection
from .. import items

category = "production"

class GenericCrafter(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0):
        super().__init__(name, category, size, cost, output, output_direction, power_consumption)

graphite_press = GenericCrafter("Graphite Press", 2, {
    items.copper: 75,
    items.lead: 30
})

multi_press = GenericCrafter("Multi Press", 3, {
    items.titanium: 100,
    items.silicon: 25,
    items.lead: 100,
    items.graphite: 50
}, power_consumption=1.8)

silicon_smelter = GenericCrafter("Silicon Smelter", 2, {
    items.copper: 30,
    items.lead: 25
}, power_consumption=0.5)

silicon_crucible = GenericCrafter("Silicon Crucible", 3, {
    items.titanium: 120,
    items.metaglass: 80,
    items.plastanium: 35,
    items.silicon: 60
}, power_consumption=4.0)

kiln = GenericCrafter("Kiln", 2, {
    items.copper: 60,
    items.graphite: 30,
    items.lead: 30
}, power_consumption=0.6)

plastanium_compressor = GenericCrafter("Plastanium Compressor", 2, {
    items.silicon: 80,
    items.lead: 115,
    items.graphite: 60,
    items.titanium: 80
}, power_consumption=3.0)

phase_weaver = GenericCrafter("Phase Weaver", 2, {
    items.silicon: 130,
    items.lead: 120,
    items.thorium: 75
}, power_consumption=5.0)

surge_smelter = GenericCrafter("Surge Smelter", 3, {
    items.silicon: 80,
    items.lead: 80,
    items.thorium: 70
}, power_consumption=4.0)

cryofluid_mixer = GenericCrafter("Cryofluid Mixer", 2, {
    items.lead: 65,
    items.silicon: 40,
    items.titanium: 60
}, power_consumption=1.0, output=BlockOutput.LIQUID)

pyratite_mixer = GenericCrafter("Pyratite Mixer", 2, {
    items.copper: 50,
    items.lead: 25
}, power_consumption=0.2)

blast_mixer = GenericCrafter("Blast Mixer", 2, {
    items.lead: 30,
    items.titanium: 20
}, power_consumption=0.4)

melter = GenericCrafter("Melter", 1, {
    items.copper: 30,
    items.lead: 35,
    items.graphite: 45
}, power_consumption=1.0, output=BlockOutput.LIQUID)

separator = GenericCrafter("Separator", 2, {
    items.copper: 30,
    items.titanium: 25
}, power_consumption=1.1)

disassembler = GenericCrafter("Disassembler", 3, {
    items.plastanium: 40,
    items.titanium: 100,
    items.silicon: 150,
    items.thorium: 80
}, power_consumption=4)

spore_press = GenericCrafter("Spore Press", 2, {
    items.lead: 35,
    items.silicon: 30
}, power_consumption=0.7, output=BlockOutput.LIQUID)

pulverizer = GenericCrafter("Pulverizer", 1, {
    items.copper: 30,
    items.lead: 25
}, power_consumption=0.5)

coal_centrifuge = GenericCrafter("Coal Centrifuge", 2, {
    items.titanium: 20,
    items.graphite: 40,
    items.lead: 30
}, power_consumption=0.7)

incinerator = GenericCrafter("Incinerator", 1, {
    items.graphite: 5,
    items.lead: 15
}, power_consumption=0.5, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

silicon_arc_furnace = GenericCrafter("Silicon Arc Furnace", 3, {
    items.beryllium: 70,
    items.graphite: 80
}, power_consumption=6)

electrolyzer = GenericCrafter("Electrolyzer", 3, {
    items.silicon: 50,
    items.graphite: 40,
    items.beryllium: 130,
    items.tungsten: 80
}, power_consumption=1, output=BlockOutput.ITEM | BlockOutput.LIQUID)

atmospheric_concentrator = GenericCrafter("Atmospheric Concentrator", 3, {
    items.oxide: 60,
    items.beryllium: 180,
    items.silicon: 150
}, power_consumption=2, output=BlockOutput.LIQUID)

oxidation_chamber = GenericCrafter("Oxidation Chamber", 3, {
    items.tungsten: 120,
    items.graphite: 100,
    items.silicon: 100,
    items.beryllium: 120
}, power_consumption=0.5)

electric_heater = GenericCrafter("Electric Heater", 2, {
    items.tungsten: 30,
    items.oxide: 30
}, power_consumption=50/60, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

slag_heater = GenericCrafter("Slag Heater", 3, {
    items.tungsten: 50,
    items.oxide: 20,
    items.beryllium: 20
}, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

phase_heater = GenericCrafter("Phase Heater", 2, {
    items.oxide: 30,
    items.carbide: 30,
    items.beryllium: 30
}, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

heat_redirector = GenericCrafter("Heat Redirector", 3, {
    items.tungsten: 10,
    items.graphite: 10
}, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

heat_router = GenericCrafter("Heat Router", 3, {
    items.tungsten: 15,
    items.graphite: 10
}, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

slag_incinerator = GenericCrafter("Slag Incinerator", 1, {
    items.tungsten: 15
})

carbide_crucible = GenericCrafter("Carbide Crucible", 3, {
    items.tungsten: 110,
    items.thorium: 150,
    items.oxide: 60
}, power_consumption=2)

slag_centrifuge = GenericCrafter("Slag Centrifuge", 3, {
    items.carbide: 70,
    items.graphite: 60,
    items.silicon: 40,
    items.oxide: 40
}, power_consumption=2/60, output=BlockOutput.LIQUID)

surge_crucible = GenericCrafter("Surge Crucible", 3, {
    items.silicon: 100,
    items.graphite: 80,
    items.tungsten: 80,
    items.oxide: 80
}, power_consumption=2)

cyanogen_synthesizer = GenericCrafter("Cyanogen Synthesizer", 3, {
    items.carbide: 50,
    items.silicon: 80,
    items.beryllium: 90
}, power_consumption=2, output=BlockOutput.LIQUID)

phase_synthesizer = GenericCrafter("Phase Synthesizer", 3, {
    items.carbide: 90,
    items.silicon: 100,
    items.thorium: 100,
    items.tungsten: 200
}, power_consumption=8)

heat_reactor = GenericCrafter("Heat Reactor", 3, {
    items.oxide: 70,
    items.graphite: 20,
    items.carbide: 10,
    items.thorium: 80
})

crafting_blocks = [
    graphite_press, multi_press, silicon_smelter, silicon_crucible, kiln,
    plastanium_compressor, phase_weaver, surge_smelter, cryofluid_mixer,
    pyratite_mixer, blast_mixer, melter, separator, disassembler, spore_press,
    pulverizer, coal_centrifuge, incinerator, silicon_arc_furnace, electrolyzer,
    atmospheric_concentrator, oxidation_chamber, electric_heater, slag_heater,
    phase_heater, heat_redirector, heat_router, slag_incinerator, carbide_crucible,
    slag_centrifuge, surge_crucible, cyanogen_synthesizer, phase_synthesizer, heat_reactor
]
