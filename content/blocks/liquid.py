from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import Pump
from .. import items

category = "liquid"
conduit_category = f"{category}/conduits"

mechanical_pump = Pump("Mechanical Pump", 1, {
    items.copper: 15,
    items.metaglass: 10
})

rotary_pump = Pump("Rotary Pump", 2, {
    items.copper: 70,
    items.metaglass: 50,
    items.silicon: 20,
    items.titanium: 35
}, power_consumption=0.3)

impulse_pump = Pump("Impulse Pump", 3, {
    items.copper: 80,
    items.metaglass: 90,
    items.silicon: 30,
    items.titanium: 40,
    items.thorium: 35
}, power_consumption=1.3)

reinforced_pump = Pump("Reinforced Pump", 2, {
    items.beryllium: 40,
    items.tungsten: 30,
    items.silicon: 20
})

conduit = Block("Conduit", conduit_category, 1, {
    items.metaglass: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT)

pulse_conduit = Block("Pulse Conduit", conduit_category, 1, {
    items.titanium: 2,
    items.metaglass: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT)

plated_conduit = Block("Plated Conduit", conduit_category, 1, {
    items.thorium: 2,
    items.metaglass: 1,
    items.plastanium: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT)

liquid_router = Block("Liquid Router", category, 1, {
    items.graphite: 4,
    items.metaglass: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

liquid_container = Block("Liquid Container", category, 2, {
    items.titanium: 10,
    items.metaglass: 15
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

liquid_tank = Block("Liquid Tank", category, 3, {
    items.titanium: 30,
    items.metaglass: 40
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

liquid_junction = Block("Liquid Junction", category, 1, {
    items.graphite: 2,
    items.metaglass: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

bridge_conduit = Block("Bridge Conduit", category, 1, {
    items.graphite: 4,
    items.metaglass: 8
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

phase_conduit = Block("Phase Conduit", category, 1, {
    items.phase_fabric: 5,
    items.silicon: 7,
    items.metaglass: 20,
    items.titanium: 10
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.3)

reinforced_conduit = Block("Reinforced Conduit", conduit_category, 1, {
    items.beryllium: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT)

reinforced_liquid_junction = Block("Reinforced Liquid Junction", category, 1, {
    items.graphite: 4,
    items.beryllium: 8
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

reinforced_bridge_conduit = Block("Reinforced Bridge Conduit", category, 1, {
    items.graphite: 8,
    items.beryllium: 20
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT)

reinforced_liquid_router = Block("Reinforced Liquid Router", category, 1, {
    items.graphite: 8,
    items.beryllium: 4
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

reinforced_liquid_container = Block("Reinforced Liquid Container", category, 2, {
    items.tungsten: 10,
    items.beryllium: 16
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

reinforced_liquid_tank = Block("Reinforced Liquid Tank", category, 3, {
    items.tungsten: 40,
    items.beryllium: 50
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

all_blocks = [
    mechanical_pump, rotary_pump, impulse_pump, reinforced_pump,
    conduit, pulse_conduit, plated_conduit,
    liquid_router, liquid_container, liquid_tank, liquid_junction,
    bridge_conduit, phase_conduit, reinforced_conduit,
    reinforced_liquid_junction, reinforced_bridge_conduit,
    reinforced_liquid_router, reinforced_liquid_container, reinforced_liquid_tank
]
