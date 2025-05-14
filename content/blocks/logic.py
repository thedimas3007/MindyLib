from g_types.block import Block, BlockOutput, BlockOutputDirection
from g_types.layers import LayeredBlock, ConditionalLayer, Layer
from .block_types import LogicBlock
from .. import items

category = "logic"

message = LayeredBlock("Message", category, 1, {
    items.graphite: 5
})

switch = LayeredBlock("Switch", category, 1, {
    items.graphite: 5
}, layers=[Layer(), ConditionalLayer("@-on")])

micro_processor = LayeredBlock("Micro Processor", category, 1, {
    items.copper: 90,
    items.lead: 50,
    items.silicon: 50
})

logic_processor = LayeredBlock("Logic Processor", category, 2, {
    items.lead: 320,
    items.silicon: 80,
    items.graphite: 60,
    items.thorium: 50
})

hyper_processor = LayeredBlock("Hyper Processor", category, 3, {
    items.lead: 450,
    items.silicon: 150,
    items.thorium: 75,
    items.surge_alloy: 50
})

memory_cell = LayeredBlock("Memory Cell", category, 1, {
    items.graphite: 30,
    items.silicon: 30
})

memory_bank = LayeredBlock("Memory Bank", category, 2, {
    items.graphite: 80,
    items.silicon: 80,
    items.phase_fabric: 30
})

logic_display = LayeredBlock("Logic Display", category, 3, {
    items.lead: 100,
    items.silicon: 50,
    items.metaglass: 50
})

large_logic_display = LayeredBlock("Large Logic Display", category, 6, {
    items.lead: 200,
    items.silicon: 150,
    items.metaglass: 100,
    items.phase_fabric: 75
})

canvas = LayeredBlock("Canvas", category, 2, {
    items.silicon: 50
})

reinforced_message = LayeredBlock("Reinforced Message", category, 1, {
    items.graphite: 10,
    items.beryllium: 5
})

world_processor = LayeredBlock("World Processor", category, 1, {})

world_cell = LayeredBlock("World Cell", category, 1, {})

world_message = LayeredBlock("World Message", category, 1, {})

all_blocks = [
    message, switch, micro_processor, logic_processor, hyper_processor,
    memory_cell, memory_bank, logic_display, large_logic_display, canvas,
    reinforced_message, world_processor, world_cell, world_message
]
