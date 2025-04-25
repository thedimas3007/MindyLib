import json
import zlib

from io import BytesIO
from PIL import Image
from struct import unpack
from typing import Literal

from content.items import get_item_by_code
from content.liquids import get_liquid_by_code
from point2 import Point2

f = open("test-sch.msch", "rb")

if f.read(4) != b"msch":
    raise Exception("Not a schematics file")

def read_utf(stream: BytesIO) -> str:
    length = int.from_bytes(stream.read(2), "big")
    return stream.read(length).decode("utf-8")

def read_num(stream: BytesIO, size: int, signed: bool = False) -> int:
    return int.from_bytes(stream.read(size), "big", signed=signed)

def read_float(stream: BytesIO, size: int) -> float:
    return unpack("f" if size == 4 else "d", stream.read(size))[0]

def read_bool(stream: BytesIO) -> bool:
    return read_num(stream, 1) != 0

def read_obj(stream: BytesIO) -> object:
    obj_type = read_num(stream, 1)
    if obj_type ==    0: return None # null
    elif obj_type ==  1: return read_num(stream, 4) # int
    elif obj_type ==  2: return read_num(stream, 8) # long
    elif obj_type ==  3: return read_float(stream, 4) # float
    elif obj_type ==  4: return read_utf(stream) # string
    elif obj_type ==  5:
        cont_type = read_num(stream, 1)
        sub_id = read_num(stream, 2)
        if cont_type == 0:
            return get_item_by_code(sub_id)
        elif cont_type == 4:
            return get_liquid_by_code(sub_id)
        else:
            return f"Content[{cont_type}, {sub_id}]"
    elif obj_type ==  6: # int[]
        arr_len = read_num(stream, 2)
        return [read_num(stream, 4) for _ in range(arr_len)]
    elif obj_type ==  7: return Point2(read_num(stream, 4, True), read_num(stream, 4, True)) # Point2
    elif obj_type ==  8: # Point2[]
        arr_len = read_num(stream, 1)
        return [Point2.unpack(read_num(stream, 4)) for _ in range(arr_len)]
    elif obj_type ==  9: return f"UnlockableContent[{read_num(stream, 1)}, {read_num(stream, 2)}]" # UnlockableContent; TODO
    elif obj_type == 10: return read_bool(stream) # bool
    elif obj_type == 11: return read_float(stream, 8) # double
    elif obj_type == 12: return f"Build[{read_num(stream, 4)}]" # world.build; TODO
    elif obj_type == 13: return f"LAccess[{read_num(stream, 2)}]" # LAccess; TODO
    elif obj_type == 14: return list(stream.read(read_num(stream, 4))) # byte[]
    elif obj_type == 15: return read_num(stream, 1) # UnitCommand; deprecated
    elif obj_type == 16: # bool[]
        arr_len = read_num(stream, 4)
        return [read_bool(stream) for _ in range(arr_len)]
    elif obj_type == 17: return f"Unit[{read_num(stream, 4)}]" # Unit; TODO
    elif obj_type == 18: # Vec2[]; TODO
        arr_len = read_num(stream, 2)
        stream.read(arr_len * 8)
        return f"Vec2[{arr_len}]"
    elif obj_type == 19: # Vec2; TODO
        stream.read(8)
        return "Vec2"
    elif obj_type == 20: return f"Team[{read_num(stream, 1, False)}]" # Team; TODO
    elif obj_type == 21: # int[]; Basically IntSeq, but who cares
        arr_len = read_num(stream, 2)
        return [read_num(stream, 4) for _ in range(arr_len)]
    elif obj_type == 22: # Object[]
        arr_len = read_num(stream, 4)
        return [read_obj(stream) for _ in range(arr_len)]
    elif obj_type == 23: return f"UnitCommand[{read_num(stream, 2, False)}]" # UnitCommand
    else:
        raise Exception(f"Unknown object type: {obj_type}")

ver = f.read(1)
print(f"Version: {ver[0]}")
print()

decom = BytesIO(zlib.decompress(f.read()))
print(f"Decompressed size: {decom.getbuffer().nbytes} bytes")
print()

height = read_num(decom, 2)
width = read_num(decom, 2)
print(f"Size: {height}x{width}")
print()

total_tags = read_num(decom, 1)
print(f"Total tags: {total_tags}")
tags = {}
for i in range(total_tags):
    key = read_utf(decom)
    value = read_utf(decom)
    tags[key] = value
print(f"- {tags}")
labels = []
try:
    labels = json.loads(tags["labels"])
except Exception as e:
    print(f"Failed to parse labels: {e}")
print(f"Labels: {labels}")
print()

blocks_used = read_num(decom, 1)
print(f"Unique blocks: {blocks_used}")
blocks = []
for i in range(blocks_used):
    name = read_utf(decom)
    blocks.append(name)
print(f"- {blocks}")
print()

preview = Image.new("RGBA", (height*32, width*32), (0, 0, 0, 0))

total_blocks = read_num(decom, 4)
block_count = {k:0 for k in blocks}
print(f"Total blocks: {total_blocks}")
for i in range(total_blocks):
    index = read_num(decom, 1)
    label = blocks[index]
    point = Point2.unpack(read_num(decom, 4))
    cfg = read_obj(decom)
    rot = read_num(decom, 1) % 4

    block_img = Image.open(f"sprites/block-{label}-ui.png")
    block_img = block_img.rotate(rot * 90)
    # point.y = int(height-point.y-block_img.height/32)

    print(f"- Block {i}: {label} at {point} ({rot})")
    if cfg: print(f"  Config: {cfg}")
    # If a bridge has enormous coordinates and after addition it becomes (-1; -1), then it has no connection
    # Bridge with no outputs at (134; 47) will have config set to (-135; -48) or (-1; -1) in world coordinates
    block_count[blocks[index]] += 1

    tile_width = block_img.width // 32
    tile_height = block_img.height // 32

    x_offset = (tile_width - 1) // 2
    y_offset = (tile_height - 1) // 2

    x_pos = (point.x - x_offset) * 32
    flipped_y = (width - point.y - tile_height + y_offset) * 32

    preview.paste(block_img, (x_pos, flipped_y))

print()

print("Block count:")
for k, v in block_count.items():
    print(f"- {k}: {v}")

preview.save("preview.png")
f.close()