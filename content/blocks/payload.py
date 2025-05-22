from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import Layer, RotatedLayer, LayeredBlock, OutlinedLayer
from .. import items

unit_category = "units"
payload_category = "payload"

def _factory_layers(dark: bool, inputs: bool, outputs: bool, top_side: bool, usual_top: bool, size: int):
    layers = [Layer()]
    if outputs:
        layers.append(RotatedLayer(("payload", f"factory-out-{size}{'-dark' if dark else ''}")))
    if inputs:
        layers.append(RotatedLayer(("payload", f"factory-in-{size}{'-dark' if dark else ''}")))
    if top_side:
        layers.append(RotatedLayer("@-side1", "@-side2"))

    if usual_top:
        layers.append(Layer(("payload", f"factory-top-{size}")))
    else:
        layers.append(Layer("@-top"))

    return layers

_factory = _factory_layers(False, False, True, False, True, 3)
_reconstructor = lambda s: _factory_layers(False, True, True, False, False, s)
_fabricator = _factory_layers(True, False, True, False, False, 3)
_refabricator = _factory_layers(True, True, True, False, False, 3)
_assembler = _factory_layers(True, False, False, True, False, 5)

ground_factory = LayeredBlock("Ground Factory", unit_category, 3, {
    items.copper: 50,
    items.lead: 120,
    items.silicon: 80,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=1.2, layers=_factory)

air_factory = LayeredBlock("Air Factory", unit_category, 3, {
    items.copper: 60,
    items.lead: 70,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=1.2, layers=_factory)

naval_factory = LayeredBlock("Naval Factory", unit_category, 3, {
    items.copper: 150,
    items.lead: 130,
    items.metaglass: 120,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=1.2, layers=_factory)

additive_reconstructor = LayeredBlock("Additive Reconstructor", unit_category, 3, {
    items.copper: 200,
    items.lead: 120,
    items.silicon: 90,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=3.0, layers=_reconstructor(3))

multiplicative_reconstructor = LayeredBlock("Multiplicative Reconstructor", unit_category, 5, {
    items.lead: 650,
    items.silicon: 450,
    items.titanium: 350,
    items.thorium: 650,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=6.0, layers=_reconstructor(5))

exponential_reconstructor = LayeredBlock("Exponential Reconstructor", unit_category, 7, {
    items.lead: 2000,
    items.silicon: 1000,
    items.titanium: 2000,
    items.thorium: 750,
    items.plastanium: 450,
    items.phase_fabric: 600,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=13.0, layers=_reconstructor(7))

tetrative_reconstructor = LayeredBlock("Tetrative Reconstructor", unit_category, 9, {
    items.lead: 4000,
    items.silicon: 3000,
    items.thorium: 1000,
    items.plastanium: 600,
    items.phase_fabric: 600,
    items.surge_alloy: 800,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=25.0, layers=_reconstructor(9))

repair_point = LayeredBlock("Repair Point", unit_category, 1, {
    items.lead: 30,
    items.copper: 30,
    items.silicon: 20,
}, layers=[Layer("@-base"), OutlinedLayer("@", 0x404049, 3)])

repair_turret = LayeredBlock("Repair Turret", unit_category, 2, {
    items.silicon: 90,
    items.thorium: 80,
    items.plastanium: 60,
}, layers=[Layer(("turrets/bases", "block-2")), OutlinedLayer("@", 0x404049, 3)])

tank_fabricator = LayeredBlock("Tank Fabricator", unit_category, 3, {
    items.silicon: 200,
    items.beryllium: 150,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=_fabricator)

ship_fabricator = LayeredBlock("Ship Fabricator", unit_category, 3, {
    items.silicon: 250,
    items.beryllium: 200,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=_fabricator)

mech_fabricator = LayeredBlock("Mech Fabricator", unit_category, 3, {
    items.silicon: 200,
    items.graphite: 300,
    items.tungsten: 60,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=_fabricator)

tank_refabricator = LayeredBlock("Tank Refabricator", unit_category, 3, {
    items.beryllium: 200,
    items.tungsten: 80,
    items.silicon: 100,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=3, layers=_refabricator)

mech_refabricator = LayeredBlock("Mech Refabricator", unit_category, 3, {
    items.beryllium: 250,
    items.tungsten: 120,
    items.silicon: 150,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2.5, layers=_refabricator)

ship_refabricator = LayeredBlock("Ship Refabricator", unit_category, 3, {
    items.beryllium: 200,
    items.tungsten: 100,
    items.silicon: 40,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2.5, layers=_refabricator)

prime_refabricator = LayeredBlock("Prime Refabricator", unit_category, 5, {
    items.thorium: 250,
    items.oxide: 200,
    items.tungsten: 200,
    items.silicon: 400,
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=5,
   layers=_factory_layers(True, True, True, False, False, 5))

tank_assembler = LayeredBlock("Tank Assembler", unit_category, 5, {
    items.thorium: 500,
    items.oxide: 150,
    items.carbide: 80,
    items.silicon: 500,
}, power_consumption=3, layers=_assembler)

ship_assembler = LayeredBlock("Ship Assembler", unit_category, 5, {
    items.carbide: 100,
    items.oxide: 200,
    items.tungsten: 500,
    items.silicon: 800,
    items.thorium: 400,
}, power_consumption=3, layers=_assembler)

mech_assembler = LayeredBlock("Mech Assembler", unit_category, 5, {
    items.carbide: 200,
    items.thorium: 600,
    items.oxide: 200,
    items.tungsten: 500,
    items.silicon: 900,
}, power_consumption=3, layers=_assembler)

basic_assembler_module = LayeredBlock("Basic Assembler Module", unit_category, 5, {
    items.carbide: 300,
    items.thorium: 500,
    items.oxide: 200,
    items.phase_fabric: 400,
}, power_consumption=4, layers=[Layer(), RotatedLayer("@-side1", "@-side2")])

unit_repair_tower = LayeredBlock("Unit Repair Tower", unit_category, 2, {
    items.graphite: 90,
    items.silicon: 90,
    items.tungsten: 80,
}, power_consumption=1)

payload_conveyor = LayeredBlock("Payload Conveyor", payload_category, 3, {
    items.graphite: 10,
    items.copper: 20
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, layers=[RotatedLayer("@-icon")])

payload_router = LayeredBlock("Payload Router", payload_category, 3, {
    items.graphite: 15,
    items.copper: 20
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.ALL, layers=[RotatedLayer("@-icon")])

reinforced_payload_conveyor = LayeredBlock("Reinforced Payload Conveyor", payload_category, 3, {
    items.tungsten: 10
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, layers=[RotatedLayer("@-icon")])

reinforced_payload_router = LayeredBlock("Reinforced Payload Router", payload_category, 3, {
    items.tungsten: 15
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.ALL, layers=[RotatedLayer("@-icon")])

payload_mass_driver = LayeredBlock("Payload Mass Driver", payload_category, 3, {
    items.tungsten: 120,
    items.silicon: 120,
    items.graphite: 50
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=0.5, layers=[
    Layer("@-base"),
    Layer("@-top"),
    RotatedLayer("factory-out-3-dark"),
    OutlinedLayer("@", 0x404049, 3),
])

large_payload_mass_driver = LayeredBlock("Large Payload Mass Driver", payload_category, 5, {
    items.thorium: 200,
    items.tungsten: 200,
    items.silicon: 200,
    items.graphite: 100,
    items.oxide: 30
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=3, layers=[
    Layer("@-base"),
    Layer("@-top"),
    RotatedLayer("factory-out-5-dark"),
    OutlinedLayer("@", 0x404049, 3),
])

small_deconstructor = LayeredBlock("Small Deconstructor", payload_category, 3, {
    items.beryllium: 100,
    items.silicon: 100,
    items.oxide: 40,
    items.graphite: 80
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=1, layers=[
    Layer(),
    Layer("@-top"),
])

deconstructor = LayeredBlock("Deconstructor", payload_category,  5, {
    items.beryllium: 250,
    items.oxide: 100,
    items.silicon: 250,
    items.carbide: 250
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=3, layers=[
    Layer(),
    Layer("@-top"),
])

constructor = LayeredBlock("Constructor", payload_category, 3, {
    items.thorium: 100
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=[
    Layer(),
    RotatedLayer("factory-out-3-dark"),
    Layer("@-top"),
])

large_constructor = LayeredBlock("Large Constructor", payload_category, 5, {
    items.silicon: 150,
    items.oxide: 150,
    items.tungsten: 200,
    items.phase_fabric: 40
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=[
    Layer(),
    RotatedLayer("factory-out-5-dark"),
    Layer("@-top"),
])

payload_loader = LayeredBlock("Payload Loader", payload_category, 3, {
    items.graphite: 50,
    items.silicon: 50,
    items.tungsten: 80
}, output=BlockOutput.PAYLOAD, output_direction=BlockOutputDirection.FRONT, power_consumption=2, layers=[
    Layer(),
    RotatedLayer("factory-out-3-dark"),
    RotatedLayer("factory-in-3-dark"),
    Layer("@-top"),
])

payload_unloader = LayeredBlock("Payload Unloader", payload_category, 3, {
    items.graphite: 50,
    items.silicon: 50,
    items.tungsten: 30
}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL, power_consumption=2, layers=[
    Layer(),
    RotatedLayer("factory-out-3-dark"),
    RotatedLayer("factory-in-3-dark"),
    Layer("@-top"),
])

all_blocks = [
    ground_factory, air_factory, naval_factory,
    additive_reconstructor, multiplicative_reconstructor, exponential_reconstructor, tetrative_reconstructor,
    repair_point, repair_turret,
    tank_fabricator, ship_fabricator, mech_fabricator,
    tank_refabricator, mech_refabricator, ship_refabricator, prime_refabricator,
    tank_assembler, ship_assembler, mech_assembler, basic_assembler_module,
    unit_repair_tower,
    payload_conveyor, payload_router, reinforced_payload_conveyor, reinforced_payload_router,
    payload_mass_driver, large_payload_mass_driver,
    small_deconstructor, deconstructor, constructor, large_constructor,
    payload_loader, payload_unloader,
]
