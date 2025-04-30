from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import Factory, PayloadBlock
from .sandbox import payload_void
from .. import items

unit_category = "unit"
payload_category = "payload"

command_center = Block("Command Center", unit_category, 2, {
    items.copper: 200,
    items.lead: 250,
    items.silicon: 250,
    items.graphite: 100,
})

ground_factory = Factory("Ground Factory", 3, {
    items.copper: 50,
    items.lead: 120,
    items.silicon: 80,
}, power_consumption=1.2)

air_factory = Factory("Air Factory", 3, {
    items.copper: 60,
    items.lead: 70,
}, power_consumption=1.2)

naval_factory = Factory("Naval Factory", 3, {
    items.copper: 150,
    items.lead: 130,
    items.metaglass: 120,
}, power_consumption=1.2)

additive_reconstructor = Factory("Additive Reconstructor", 3, {
    items.copper: 200,
    items.lead: 120,
    items.silicon: 90,
}, power_consumption=3.0)

multiplicative_reconstructor = Factory("Multiplicative Reconstructor", 5, {
    items.lead: 650,
    items.silicon: 450,
    items.titanium: 350,
    items.thorium: 650,
}, power_consumption=6.0)

exponential_reconstructor = Factory("Exponential Reconstructor", 7, {
    items.lead: 2000,
    items.silicon: 1000,
    items.titanium: 2000,
    items.thorium: 750,
    items.plastanium: 450,
    items.phase_fabric: 600,
}, power_consumption=13.0)

tetrative_reconstructor = Factory("Tetrative Reconstructor", 9, {
    items.lead: 4000,
    items.silicon: 3000,
    items.thorium: 1000,
    items.plastanium: 600,
    items.phase_fabric: 600,
    items.surge_alloy: 800,
}, power_consumption=25.0)

repair_point = Block("Repair Point", unit_category, 1, {
    items.lead: 30,
    items.copper: 30,
    items.silicon: 20,
})

repair_turret = Block("Repair Turret", "turrets", 2, {
    items.silicon: 90,
    items.thorium: 80,
    items.plastanium: 60,
})

resupply_point = Block("Resupply Point", unit_category, 2, {
    items.lead: 20,
    items.copper: 15,
    items.silicon: 15,
})

tank_fabricator = Factory("Tank Fabricator", 3, {
    items.silicon: 200,
    items.beryllium: 150,
}, power_consumption=2)

ship_fabricator = Factory("Ship Fabricator", 3, {
    items.silicon: 250,
    items.beryllium: 200,
}, power_consumption=2)

mech_fabricator = Factory("Mech Fabricator", 3, {
    items.silicon: 200,
    items.graphite: 300,
    items.tungsten: 60,
}, power_consumption=2)

tank_refabricator = Factory("Tank Refabricator", 3, {
    items.beryllium: 200,
    items.tungsten: 80,
    items.silicon: 100,
}, power_consumption=3)

mech_refabricator = Factory("Mech Refabricator", 3, {
    items.beryllium: 250,
    items.tungsten: 120,
    items.silicon: 150,
}, power_consumption=2.5)

ship_refabricator = Factory("Ship Refabricator", 3, {
    items.beryllium: 200,
    items.tungsten: 100,
    items.silicon: 40,
}, power_consumption=2.5)

prime_refabricator = Factory("Prime Refabricator", 5, {
    items.thorium: 250,
    items.oxide: 200,
    items.tungsten: 200,
    items.silicon: 400,
}, power_consumption=5)

tank_assembler = Factory("Tank Assembler", 5, {
    items.thorium: 500,
    items.oxide: 150,
    items.carbide: 80,
    items.silicon: 500,
}, power_consumption=3)

ship_assembler = Factory("Ship Assembler", 5, {
    items.carbide: 100,
    items.oxide: 200,
    items.tungsten: 500,
    items.silicon: 800,
    items.thorium: 400,
}, power_consumption=3)

mech_assembler = Factory("Mech Assembler", 5, {
    items.carbide: 200,
    items.thorium: 600,
    items.oxide: 200,
    items.tungsten: 500,
    items.silicon: 900,
}, power_consumption=3)

basic_assembler_module = Block("Basic Assembler Module", unit_category, 5, {
    items.carbide: 300,
    items.thorium: 500,
    items.oxide: 200,
    items.phase_fabric: 400,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=4)

unit_repair_tower = Block("Unit Repair Tower", unit_category, 2, {
    items.graphite: 90,
    items.silicon: 90,
    items.tungsten: 80,
}, power_consumption=1)

payload_conveyor = PayloadBlock("Payload Conveyor", 3, {
    items.graphite: 10,
    items.copper: 20
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT)

payload_router = PayloadBlock("Payload Router", 3, {
    items.graphite: 15,
    items.copper: 20
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.ALL)

reinforced_payload_conveyor = PayloadBlock("Reinforced Payload Conveyor", 3, {
    items.tungsten: 10
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT)

reinforced_payload_router = PayloadBlock("Reinforced Payload Router", 3, {
    items.tungsten: 15
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.ALL)

payload_mass_driver = PayloadBlock("Payload Mass Driver", 3, {
    items.tungsten: 120,
    items.silicon: 120,
    items.graphite: 50
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=0.5)

large_payload_mass_driver = PayloadBlock("Large Payload Mass Driver", 5, {
    items.thorium: 200,
    items.tungsten: 200,
    items.silicon: 200,
    items.graphite: 100,
    items.oxide: 30
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=3 )

small_deconstructor = PayloadBlock("Small Deconstructor", 3, {
    items.beryllium: 100,
    items.silicon: 100,
    items.oxide: 40,
    items.graphite: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=1)

deconstructor = PayloadBlock("Deconstructor", 5, {
    items.beryllium: 250,
    items.oxide: 100,
    items.silicon: 250,
    items.carbide: 250
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=3)

constructor = PayloadBlock("Constructor", 3, {
    items.thorium: 100
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2)

large_constructor = PayloadBlock("Large Constructor", 5, {
    items.silicon: 150,
    items.oxide: 150,
    items.tungsten: 200,
    items.phase_fabric: 40
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2)

payload_loader = PayloadBlock("Payload Loader", 3, {
    items.graphite: 50,
    items.silicon: 50,
    items.tungsten: 80
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2)

payload_unloader = PayloadBlock("Payload Unloader", 3, {
    items.graphite: 50,
    items.silicon: 50,
    items.tungsten: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=2)

all_blocks = [
    command_center,
    ground_factory, air_factory, naval_factory,
    additive_reconstructor, multiplicative_reconstructor, exponential_reconstructor, tetrative_reconstructor,
    repair_point, repair_turret, resupply_point,
    tank_fabricator, ship_fabricator, mech_fabricator,
    tank_refabricator, mech_refabricator, ship_refabricator, prime_refabricator,
    tank_assembler, ship_assembler, mech_assembler, basic_assembler_module,
    unit_repair_tower,
    payload_conveyor, payload_router, reinforced_payload_conveyor, reinforced_payload_router,
    payload_mass_driver, large_payload_mass_driver,
    small_deconstructor, deconstructor, constructor, large_constructor,
    payload_loader, payload_unloader,
]
