from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import TransportBlock
from .. import items

distribution = "distribution"
duct_category = f"{distribution}/ducts"
conveyor_category = f"{distribution}/conveyors"
stack_category = f"{distribution}/stack-conveyors"
unit_category = "units"

conveyor = TransportBlock("Conveyor", conveyor_category, 1, {
    items.copper: 1
}, output_direction=BlockOutputDirection.FRONT)

titanium_conveyor = TransportBlock("Titanium Conveyor", conveyor_category, 1, {
    items.copper: 1,
    items.lead: 1,
    items.titanium: 1
}, output_direction=BlockOutputDirection.FRONT)

plastanium_conveyor = TransportBlock("Plastanium Conveyor", stack_category, 1, {
    items.plastanium: 1,
    items.silicon: 1,
    items.graphite: 1
}, output_direction=BlockOutputDirection.NONE)

armored_conveyor = TransportBlock("Armored Conveyor", conveyor_category, 1, {
    items.plastanium: 1,
    items.thorium: 1,
    items.metaglass: 1
}, output_direction=BlockOutputDirection.FRONT)

junction = TransportBlock("Junction", distribution, 1, {
    items.copper: 2
})

item_bridge = TransportBlock("Bridge Conveyor", distribution, 1, {
    items.lead: 6,
    items.copper: 6
})

phase_conveyor = TransportBlock("Phase Conveyor", distribution, 1, {
    items.phase_fabric: 5,
    items.silicon: 7,
    items.lead: 10,
    items.graphite: 10
}, power_consumption=0.3)

sorter = TransportBlock("Sorter", distribution, 1, {
    items.lead: 2,
    items.copper: 2
})

inverted_sorter = TransportBlock("Inverted Sorter", distribution, 1, {
    items.lead: 2,
    items.copper: 2
})

router = TransportBlock("Router", distribution, 1, {
    items.copper: 3
})

distributor = TransportBlock("Distributor", distribution, 2, {
    items.lead: 4,
    items.copper: 4
})

overflow_gate = TransportBlock("Overflow Gate", distribution, 1, {
    items.lead: 2,
    items.copper: 4
})

underflow_gate = TransportBlock("Underflow Gate", distribution, 1, {
    items.lead: 2,
    items.copper: 4
})

mass_driver = TransportBlock("Mass Driver", distribution, 3, {
    items.titanium: 125,
    items.silicon: 75,
    items.lead: 125,
    items.thorium: 50
}, power_consumption=1.75)

duct = TransportBlock("Duct", duct_category, 1, {
    items.graphite: 5,
    items.metaglass: 2
}, output_direction=BlockOutputDirection.FRONT)

armored_duct = TransportBlock("Armored Duct", duct_category, 1, {
    items.beryllium: 2,
    items.tungsten: 1
}, output_direction=BlockOutputDirection.FRONT)

duct_router = TransportBlock("Duct Router", duct_category, 1, {
    items.graphite: 10,
    items.metaglass: 4
})

overflow_duct = TransportBlock("Overflow Duct", duct_category, 1, {
    items.graphite: 8,
    items.beryllium: 8
})

underflow_duct = TransportBlock("Underflow Duct", duct_category, 1, {
    items.graphite: 8,
    items.beryllium: 8
})

duct_bridge = TransportBlock("Duct Bridge", duct_category, 1, {
    items.graphite: 20,
    items.metaglass: 8
}, output_direction=BlockOutputDirection.FRONT)

duct_unloader = TransportBlock("Duct Unloader", duct_category, 1, {
    items.graphite: 20,
    items.silicon: 20,
    items.tungsten: 10
})

surge_conveyor = TransportBlock("Surge Conveyor", stack_category, 1, {
    items.surge_alloy: 1,
    items.tungsten: 1
}, output_direction=BlockOutputDirection.NONE, power_consumption=1/60)

surge_router = TransportBlock("Surge Router", duct_category, 1, {
    items.surge_alloy: 5,
    items.tungsten: 1
}, power_consumption=3/60)

unit_cargo_loader = Block("Unit Cargo Loader", unit_category, 3, {
    items.silicon: 80,
    items.surge_alloy: 50,
    items.oxide: 20
}, power_consumption=8/60)

unit_cargo_unload_point = Block("Unit Cargo Unload Point", unit_category, 2, {
    items.silicon: 60,
    items.tungsten: 60
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)

all_blocks = [
    conveyor, titanium_conveyor, plastanium_conveyor, armored_conveyor,
    junction, item_bridge, phase_conveyor, sorter, inverted_sorter, router,
    distributor, overflow_gate, underflow_gate, mass_driver, duct, armored_duct,
    duct_router, overflow_duct, underflow_duct, duct_bridge, duct_unloader,
    surge_conveyor, surge_router, unit_cargo_loader, unit_cargo_unload_point
]
