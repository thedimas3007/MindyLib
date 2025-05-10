from typing import Optional

from g_types.block import Block
from . import campaign, core, crafting, defense, distribution, experiment, liquid, logic, payload, power, production, sandbox, turret

modules = [campaign, core, crafting, defense, distribution, experiment, liquid, logic, payload, power, production, sandbox, turret]

all_blocks = []
for module in modules:
    all_blocks.extend(module.all_blocks)

def get_block(id: str) -> Optional[Block]:
    return next((block for block in all_blocks if block.id == id), None)

if __name__ == "__main__":
    from rich import inspect
    for block in all_blocks[:15]:
        inspect(block)