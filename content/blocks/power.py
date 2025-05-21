from g_types.block import BlockOutput, BlockOutputDirection
from .block_types import PowerBlock, PowerGenerator
from .. import items

category = "power"

# TODO: battery type for Capacity field

power_node = PowerBlock("Power Node", 1, {
    items.copper: 1,
    items.lead: 3
})

power_node_large = PowerBlock("Power Node Large", 2, {
    items.titanium: 5,
    items.lead: 10,
    items.silicon: 3
})

surge_tower = PowerBlock("Surge Tower", 2, {
    items.titanium: 7,
    items.lead: 10,
    items.silicon: 15,
    items.surge_alloy: 15
})

diode = PowerBlock("Diode", 1, {
    items.silicon: 10,
    items.plastanium: 5,
    items.metaglass: 10
})

battery = PowerBlock("Battery", 1, {
    items.copper: 5,
    items.lead: 20
})

battery_large = PowerBlock("Battery Large", 3, {
    items.titanium: 20,
    items.lead: 40,
    items.silicon: 20
})

combustion_generator = PowerGenerator("Combustion Generator", 1, {
    items.copper: 25,
    items.lead: 15
}, power_generation=1)

thermal_generator = PowerGenerator("Thermal Generator", 2, {
    items.copper: 40,
    items.graphite: 35,
    items.lead: 50,
    items.silicon: 35,
    items.metaglass: 40
}, power_generation=1.8)

steam_generator = PowerGenerator("Steam Generator", 2, {
    items.copper: 35,
    items.graphite: 25,
    items.lead: 40,
    items.silicon: 30
}, power_generation=5.5)

differential_generator = PowerGenerator("Differential Generator", 3, {
    items.copper: 70,
    items.titanium: 50,
    items.lead: 100,
    items.silicon: 65,
    items.metaglass: 50
}, power_generation=18)

rtg_generator = PowerGenerator("RTG Generator", 2, {
    items.lead: 100,
    items.silicon: 75,
    items.phase_fabric: 25,
    items.plastanium: 75,
    items.thorium: 50
}, power_generation=4.5)

solar_panel = PowerGenerator("Solar Panel", 1, {
    items.lead: 10,
    items.silicon: 15
}, power_generation=0.1)

solar_panel_large = PowerGenerator("Solar Panel Large", 3, {
    items.lead: 80,
    items.silicon: 110,
    items.phase_fabric: 15
}, power_generation=1.3)

thorium_reactor = PowerGenerator("Thorium Reactor", 3, {
    items.lead: 300,
    items.silicon: 200,
    items.graphite: 150,
    items.thorium: 150,
    items.metaglass: 50
}, power_generation=15)

impact_reactor = PowerGenerator("Impact Reactor", 4, {
    items.lead: 500,
    items.silicon: 300,
    items.graphite: 400,
    items.thorium: 100,
    items.surge_alloy: 250,
    items.metaglass: 250
}, power_consumption=25, power_generation=130)

beam_node = PowerBlock("Beam Node", 1, {
    items.beryllium: 8
})

beam_tower = PowerBlock("Beam Tower", 3, {
    items.beryllium: 30,
    items.oxide: 20,
    items.silicon: 10
})

beam_link = PowerBlock("Beam Link", 3, { # V8 Beta contains requirements, while the game doesn't
    # items.beryllium: 250,
    # items.silicon: 250,
    # items.oxide: 150,
    # items.carbide: 75,
    # items.surge_alloy: 75,
    # items.phase_fabric: 75
})

turbine_condenser = PowerGenerator("Turbine Condenser", 3, {
    items.beryllium: 60
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_generation=1/3)

chemical_combustion_chamber = PowerGenerator("Chemical Combustion Chamber", 3, {
    items.graphite: 40,
    items.tungsten: 40,
    items.oxide: 40,
    items.silicon: 30
}, power_generation=10)

pyrolysis_generator = PowerGenerator("Pyrolysis Generator", 3, {
    items.graphite: 50,
    items.carbide: 50,
    items.oxide: 60,
    items.silicon: 50
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_generation=25)

flux_reactor = PowerGenerator("Flux Reactor", 5, {
    items.graphite: 300,
    items.carbide: 200,
    items.oxide: 100,
    items.silicon: 600,
    items.surge_alloy: 300
}, power_generation=120)

neoplasia_reactor = PowerGenerator("Neoplasia Reactor", 5, {
    items.tungsten: 1000,
    items.carbide: 300,
    items.oxide: 150,
    items.silicon: 500,
    items.phase_fabric: 300,
    items.surge_alloy: 200
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT, power_generation=140)

all_blocks = [
    power_node, power_node_large, surge_tower, diode,
    battery, battery_large, combustion_generator, thermal_generator,
    steam_generator, differential_generator, rtg_generator, solar_panel,
    solar_panel_large, thorium_reactor, impact_reactor, beam_node, beam_tower,
    beam_link, turbine_condenser, chemical_combustion_chamber,
    pyrolysis_generator, flux_reactor, neoplasia_reactor
]
