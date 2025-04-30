import math

from g_types.block import Block, BlockOutput, BlockOutputDirection
from .block_types import PayloadBlock, PowerGenerator, PowerBlock

sandbox_category = "sandbox"
power_category = "power"
distribution_category = "distribution"
payload_category = "payload"

power_source = PowerGenerator("Power Source", 1, {}, power_generation=math.inf)
power_void = PowerBlock("Power Void",  1, {}, power_consumption=math.inf)

item_source = Block("Item Source", distribution_category, 1, {}, output=BlockOutput.ITEM, output_direction=BlockOutputDirection.ALL)
item_void = Block("Item Void", distribution_category, 1, {})

liquid_source = Block("Liquid Source", distribution_category, 1, {}, output=BlockOutput.LIQUID, output_direction=BlockOutputDirection.ALL)
liquid_void = Block("Liquid Void", distribution_category, 1, {})

payload_source = PayloadBlock("Payload Source", 5, {})
payload_void = PayloadBlock("Payload Void", 5, {}, output=BlockOutput.NONE, output_direction=BlockOutputDirection.NONE)

heat_source = Block("Heat Source", sandbox_category, 1, {})

all_blocks = [
    power_source, power_void,
    item_source, item_void,
    liquid_source, liquid_void,
    payload_source, payload_void,
    heat_source,
]
