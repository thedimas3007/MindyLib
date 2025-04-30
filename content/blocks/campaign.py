from g_types.block import Block, BlockOutput, BlockOutputDirection
from .. import items

category = "campaign"

class Pad(Block):
    def __init__(self, name, size, cost, power_consumption=0.0):
        super().__init__(name, category, size, cost, power_consumption=power_consumption)

launch_pad = Pad("Launch Pad",  3, {
    items.copper: 350,
    items.silicon: 140,
    items.lead: 200,
    items.titanium: 150
}, power_consumption=4.0)

interplanetary_accelerator = Block("Interplanetary Accelerator",  category, 7, {
    items.copper: 16000,
    items.silicon: 11000,
    items.thorium: 13000,
    items.titanium: 12000,
    items.surge_alloy: 6000,
    items.phase_fabric: 5000
}, power_consumption=10.0)

campaign_blocks = [launch_pad, interplanetary_accelerator]