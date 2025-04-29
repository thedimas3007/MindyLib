from g_types.block import Block
from .. import items

category = "logic"

class LogicBlock(Block):
    def __init__(self, name, size, cost, **kwargs):
        super().__init__(name, category, size, cost, **kwargs)

message = LogicBlock("Message", 1, {
    items.graphite: 5
})

switch = LogicBlock("Switch", 1, {
    items.graphite: 5
})

micro_processor = LogicBlock("Micro Processor", 1, {
    items.copper: 90,
    items.lead: 50,
    items.silicon: 50
})

logic_processor = LogicBlock("Logic Processor", 2, {
    items.lead: 320,
    items.silicon: 80,
    items.graphite: 60,
    items.thorium: 50
})

hyper_processor = LogicBlock("Hyper Processor", 3, {
    items.lead: 450,
    items.silicon: 150,
    items.thorium: 75,
    items.surge_alloy: 50
})

memory_cell = LogicBlock("Memory Cell", 1, {
    items.graphite: 30,
    items.silicon: 30
})

memory_bank = LogicBlock("Memory Bank", 2, {
    items.graphite: 80,
    items.silicon: 80,
    items.phase_fabric: 30
})

logic_display = LogicBlock("Logic Display", 3, {
    items.lead: 100,
    items.silicon: 50,
    items.metaglass: 50
})

large_logic_display = LogicBlock("Large Logic Display", 6, {
    items.lead: 200,
    items.silicon: 150,
    items.metaglass: 100,
    items.phase_fabric: 75
})

canvas = LogicBlock("Canvas", 2, {
    items.silicon: 50
})

reinforced_message = LogicBlock("Reinforced Message", 1, {
    items.graphite: 10,
    items.beryllium: 5
})

world_processor = LogicBlock("World Processor", 1, {})

world_cell = LogicBlock("World Cell", 1, {})

world_message = LogicBlock("World Message", 1, {})

logic_blocks = [
    message, switch, micro_processor, logic_processor, hyper_processor,
    memory_cell, memory_bank, logic_display, large_logic_display, canvas,
    reinforced_message, world_processor, world_cell, world_message
]
