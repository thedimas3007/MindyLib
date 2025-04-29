from g_types.block import Block, BlockOutput, BlockOutputDirection
from .. import items

category = "payload"

class PayloadBlock(Block):
    def __init__(self, name, size, cost, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE, power_consumption=0.0):
        super().__init__(name, category, size, cost, output=output, output_direction=output_direction, power_consumption=power_consumption)
                         

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

payload_blocks = [
    payload_conveyor, payload_router, reinforced_payload_conveyor, reinforced_payload_router,
    payload_mass_driver, large_payload_mass_driver,
    small_deconstructor, deconstructor, constructor, large_constructor,
    payload_loader, payload_unloader,
]
