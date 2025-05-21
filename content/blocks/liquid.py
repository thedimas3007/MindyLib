from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, ConveyorLayer, TintedLayer, Layer, RotatedLayer
from .block_types import Conduit, Bridge, DirectionalBridge
from .. import items

category = "liquid"
conduit_category = f"{category}/conduits"

mechanical_pump = LayeredBlock("Mechanical Pump", category, 1, {
    items.copper: 15,
    items.metaglass: 10
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

rotary_pump = LayeredBlock("Rotary Pump", category,2, {
    items.copper: 70,
    items.metaglass: 50,
    items.silicon: 20,
    items.titanium: 35
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.3)

impulse_pump = LayeredBlock("Impulse Pump", category, 3, {
    items.copper: 80,
    items.metaglass: 90,
    items.silicon: 30,
    items.titanium: 40,
    items.thorium: 35
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=1.3)

reinforced_pump = LayeredBlock("Reinforced Pump", category, 2, {
    items.beryllium: 40,
    items.tungsten: 30,
    items.silicon: 20
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

conduit = Conduit("Conduit", conduit_category, 1, {
    items.metaglass: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT, layers=[
    TintedLayer(ConveyorLayer("@-bottom-#"), 0x565656),
    ConveyorLayer("@-top-#")
])

pulse_conduit = Conduit("Pulse Conduit", conduit_category, 1, {
    items.titanium: 2,
    items.metaglass: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT, layers=[
    TintedLayer(ConveyorLayer("@-bottom-#"), 0x565656),
    ConveyorLayer("@-top-#")
])

plated_conduit = Conduit("Plated Conduit", conduit_category, 1, {
    items.thorium: 2,
    items.metaglass: 1,
    items.plastanium: 1
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT, layers=[
    TintedLayer(ConveyorLayer("@-bottom-#", strict=True), 0x565656),
    ConveyorLayer("@-top-#", strict=True),
])

liquid_router = LayeredBlock("Liquid Router", category, 1, {
    items.graphite: 4,
    items.metaglass: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

liquid_container = LayeredBlock("Liquid Container", category, 2, {
    items.titanium: 10,
    items.metaglass: 15
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

liquid_tank = LayeredBlock("Liquid Tank", category, 3, {
    items.titanium: 30,
    items.metaglass: 40
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

liquid_junction = LayeredBlock("Liquid Junction", category, 1, {
    items.graphite: 2,
    items.metaglass: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

bridge_conduit = Bridge("Bridge Conduit", category, 1, {
    items.graphite: 4,
    items.metaglass: 8
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

phase_conduit = Bridge("Phase Conduit", category, 1, {
    items.phase_fabric: 5,
    items.silicon: 7,
    items.metaglass: 20,
    items.titanium: 10
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, power_consumption=0.3)

reinforced_conduit = Conduit("Reinforced Conduit", conduit_category, 1, {
    items.beryllium: 2
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.FRONT, layers=[
    TintedLayer(ConveyorLayer("@-bottom-#", strict=True), 0x38393f),
    ConveyorLayer("@-top-#", strict=True),
])
reinforced_liquid_junction = LayeredBlock("Reinforced Liquid Junction", category, 1, {
    items.graphite: 4,
    items.beryllium: 8
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)

reinforced_bridge_conduit = DirectionalBridge("Reinforced Bridge Conduit", category, 1, {
    items.graphite: 8,
    items.beryllium: 20
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, max_range=4, layers=[
    Layer("@-bottom"),
    Layer(),
    RotatedLayer("@-dir"),
])

reinforced_liquid_router = LayeredBlock("Reinforced Liquid Router", category, 1, {
    items.graphite: 8,
    items.beryllium: 4
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

reinforced_liquid_container = LayeredBlock("Reinforced Liquid Container", category, 2, {
    items.tungsten: 10,
    items.beryllium: 16
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

reinforced_liquid_tank = LayeredBlock("Reinforced Liquid Tank", category, 3, {
    items.tungsten: 40,
    items.beryllium: 50
}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL, layers=[Layer("@-bottom"), Layer()])

all_blocks = [
    mechanical_pump, rotary_pump, impulse_pump, reinforced_pump,
    conduit, pulse_conduit, plated_conduit,
    liquid_router, liquid_container, liquid_tank, liquid_junction,
    bridge_conduit, phase_conduit, reinforced_conduit,
    reinforced_liquid_junction, reinforced_bridge_conduit,
    reinforced_liquid_router, reinforced_liquid_container, reinforced_liquid_tank
]
