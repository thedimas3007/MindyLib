from g_types.block import BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, ConveyorLayer, ItemConfigLayer, Layer, OutlinedLayer, \
    ItemTintedLayer, RotatedLayer, StackConveyorLayer
from ..blocks.block_types import Conveyor, StackConveyor, Bridge, DirectionalBridge
from .. import items

distribution = "distribution"
duct_category = f"{distribution}/ducts"
conveyor_category = f"{distribution}/conveyors"
stack_category = f"{distribution}/stack-conveyors"
unit_category = "units"

# FIXME: Classes shall not be here, but rather moved to block_types.py eventually

conveyor = Conveyor("Conveyor", conveyor_category, 1, {
    items.copper: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[ConveyorLayer()])

titanium_conveyor = Conveyor("Titanium Conveyor", conveyor_category, 1, {
    items.copper: 1,
    items.lead: 1,
    items.titanium: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[ConveyorLayer()])

plastanium_conveyor = StackConveyor("Plastanium Conveyor", stack_category, 1, {
    items.plastanium: 1,
    items.silicon: 1,
    items.graphite: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[StackConveyorLayer()])

armored_conveyor = Conveyor("Armored Conveyor", conveyor_category, 1, {
    items.plastanium: 1,
    items.thorium: 1,
    items.metaglass: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[ConveyorLayer(strict=True)])

junction = LayeredBlock("Junction", distribution, 1, {
    items.copper: 2
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

item_bridge = Bridge("Bridge Conveyor", distribution, 1, {
    items.lead: 6,
    items.copper: 6
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

phase_conveyor = Bridge("Phase Conveyor", distribution, 1, {
    items.phase_fabric: 5,
    items.silicon: 7,
    items.lead: 10,
    items.graphite: 10
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=0.3)

sorter = LayeredBlock("Sorter", distribution, 1, {
    items.lead: 2,
    items.copper: 2
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[ItemConfigLayer(), Layer()])

inverted_sorter = LayeredBlock("Inverted Sorter", distribution, 1, {
    items.lead: 2,
    items.copper: 2
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[ItemConfigLayer(), Layer()])

router = LayeredBlock("Router", distribution, 1, {
    items.copper: 3
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

distributor = LayeredBlock("Distributor", distribution, 2, {
    items.lead: 4,
    items.copper: 4
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

overflow_gate = LayeredBlock("Overflow Gate", distribution, 1, {
    items.lead: 2,
    items.copper: 4
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

underflow_gate = LayeredBlock("Underflow Gate", distribution, 1, {
    items.lead: 2,
    items.copper: 4
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

mass_driver = LayeredBlock("Mass Driver", distribution, 3, {
    items.titanium: 125,
    items.silicon: 75,
    items.lead: 125,
    items.thorium: 50
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=1.75, layers=[
    Layer("@-base"),
    OutlinedLayer("@", 0x3f3f3f, 3)
])

duct = Conveyor("Duct", duct_category, 1, {
    items.graphite: 5,
    items.metaglass: 2
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[
    ConveyorLayer("@-bottom-#"),
    ConveyorLayer("@-top-#")
])

armored_duct = Conveyor("Armored Duct", duct_category, 1, {
    items.beryllium: 2,
    items.tungsten: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[
    ConveyorLayer("duct-bottom-#", strict=True), # NB: not armored-duct-bottom
    ConveyorLayer("@-top-#", strict=True)
])

duct_router = LayeredBlock("Duct Router", duct_category, 1, {
    items.graphite: 10,
    items.metaglass: 4
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[
    Layer(),
    ItemTintedLayer("duct-unloader-center", "@-top")
])

overflow_duct = LayeredBlock("Overflow Duct", duct_category, 1, {
    items.graphite: 8,
    items.beryllium: 8
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[
    Layer(),
    RotatedLayer("@-top")
])

underflow_duct = LayeredBlock("Underflow Duct", duct_category, 1, {
    items.graphite: 8,
    items.beryllium: 8
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[
    Layer(),
    RotatedLayer("@-top")
])

duct_bridge = DirectionalBridge("Duct Bridge", duct_category, 1, {
    items.graphite: 20,
    items.metaglass: 8
}, max_range=4, layers=[Layer(), RotatedLayer("@-dir")])

duct_unloader = LayeredBlock("Duct Unloader", duct_category, 1, {
    items.graphite: 20,
    items.silicon: 20,
    items.tungsten: 10
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[
    Layer(),
    ItemTintedLayer("@-center", "@-arrow"),
    RotatedLayer("@-top")
])

surge_conveyor = StackConveyor("Surge Conveyor", stack_category, 1, {
    items.surge_alloy: 1,
    items.tungsten: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.FRONT, layers=[StackConveyorLayer()])

surge_router = LayeredBlock("Surge Router", duct_category, 1, {
    items.surge_alloy: 5,
    items.tungsten: 1
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=3/60, layers=[
    Layer(),
    ItemTintedLayer("duct-unloader-center", "@-top")
])

unit_cargo_loader = LayeredBlock("Unit Cargo Loader", unit_category, 3, {
    items.silicon: 80,
    items.surge_alloy: 50,
    items.oxide: 20
}, power_consumption=8/60)

unit_cargo_unload_point = LayeredBlock("Unit Cargo Unload Point", unit_category, 2, {
    items.silicon: 60,
    items.tungsten: 60
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, layers=[
    Layer(),
    ItemTintedLayer("@-top")
])

all_blocks = [
    conveyor, titanium_conveyor, plastanium_conveyor, armored_conveyor,
    junction, item_bridge, phase_conveyor, sorter, inverted_sorter, router,
    distributor, overflow_gate, underflow_gate, mass_driver, duct, armored_duct,
    duct_router, overflow_duct, underflow_duct, duct_bridge, duct_unloader,
    surge_conveyor, surge_router, unit_cargo_loader, unit_cargo_unload_point
]
