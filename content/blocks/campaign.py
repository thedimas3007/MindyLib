from g_types.block import Block, BlockOutput, BlockOutputDirection, LayeredBlock
from .block_types import Pad
from .. import items

category = "campaign"

launch_pad = LayeredBlock("Launch Pad", category,  3, {
    items.copper: 350,
    items.silicon: 140,
    items.lead: 200,
    items.titanium: 150
}, power_consumption=4.0)

interplanetary_accelerator = LayeredBlock("Interplanetary Accelerator",  category, 7, {
    items.copper: 16000,
    items.silicon: 11000,
    items.thorium: 13000,
    items.titanium: 12000,
    items.surge_alloy: 6000,
    items.phase_fabric: 5000
}, power_consumption=10.0)

all_blocks = [launch_pad, interplanetary_accelerator]