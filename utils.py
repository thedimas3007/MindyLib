from enum import IntFlag
from struct import unpack
from typing import IO

from PIL import Image, ImageEnhance, ImageFilter, ImageChops

from content.items import get_item_by_code
from content.liquids import get_liquid_by_code
from g_types.point2 import Point2

class JavaTypes(IntFlag):
    BYTE     = 1
    SHORT    = 2
    INT      = 4
    LONG     = 8
    FLOAT    = 4 | 0x20
    DOUBLE   = 8 | 0x20

    S_BYTE   = 1 | 0x10
    S_SHORT  = 2 | 0x10
    S_INT    = 4 | 0x10
    S_LONG   = 8 | 0x10
    S_FLOAT  = 4 | 0x10 | 0x20
    S_DOUBLE = 8 | 0x10 | 0x20

    def is_signed(self) -> bool:
        return self.value & 0x10 != 0

    def is_float(self) -> bool:
        return self.value & 0x20 != 0

    def size(self) -> int:
        return self.value & 0x0F

def read_utf(stream: IO) -> str:
    length = int.from_bytes(stream.read(2), "big")
    return stream.read(length).decode("utf-8")

def read_num(stream: IO, num_type: JavaTypes) -> int | float:
    if num_type.is_float():
        return unpack("f" if num_type.size() == 4 else "d", stream.read(num_type.size()))[0]
    else:
        return int.from_bytes(stream.read(num_type.size()), "big", signed=num_type.is_signed())

def read_bool(stream: IO) -> bool:
    return read_num(stream, JavaTypes.BYTE) != 0

def read_obj(stream: IO) -> object:
    obj_type = read_num(stream, JavaTypes.BYTE)
    if obj_type ==    0: return None # null
    elif obj_type ==  1: return read_num(stream, JavaTypes.INT) # int
    elif obj_type ==  2: return read_num(stream, JavaTypes.LONG) # long
    elif obj_type ==  3: return read_num(stream, JavaTypes.FLOAT) # float
    elif obj_type ==  4: return read_utf(stream) # string
    elif obj_type ==  5:
        cont_type = read_num(stream, JavaTypes.BYTE)
        sub_id = read_num(stream, JavaTypes.SHORT)
        if cont_type == 0:
            return get_item_by_code(sub_id)
        elif cont_type == 4:
            return get_liquid_by_code(sub_id)
        else:
            return f"Content[{cont_type}, {sub_id}]"
    elif obj_type ==  6: # int[]
        arr_len = read_num(stream, JavaTypes.SHORT)
        return [read_num(stream, JavaTypes.INT) for _ in range(arr_len)]
    elif obj_type ==  7: return Point2(read_num(stream, JavaTypes.S_INT), read_num(stream, JavaTypes.S_INT)) # Point2
    elif obj_type ==  8: # Point2[]
        arr_len = read_num(stream, JavaTypes.BYTE)
        return [Point2.unpack(read_num(stream, JavaTypes.INT)) for _ in range(arr_len)]
    elif obj_type ==  9: return f"UnlockableContent[{read_num(stream, JavaTypes.BYTE)}, {read_num(stream, JavaTypes.SHORT)}]" # UnlockableContent; TODO
    elif obj_type == 10: return read_bool(stream) # bool
    elif obj_type == 11: return read_num(stream, JavaTypes.DOUBLE) # double
    elif obj_type == 12: return f"Build[{read_num(stream, JavaTypes.INT)}]" # world.build; TODO
    elif obj_type == 13: return f"LAccess[{read_num(stream, JavaTypes.SHORT)}]" # LAccess; TODO
    elif obj_type == 14: return list(stream.read(read_num(stream, JavaTypes.INT))) # byte[]
    elif obj_type == 15: return read_num(stream, JavaTypes.BYTE) # UnitCommand; deprecated
    elif obj_type == 16: # bool[]
        arr_len = read_num(stream, JavaTypes.INT)
        return [read_bool(stream) for _ in range(arr_len)]
    elif obj_type == 17: return f"Unit[{read_num(stream, JavaTypes.INT)}]" # Unit; TODO
    elif obj_type == 18: # Vec2[]; TODO
        arr_len = read_num(stream, JavaTypes.SHORT)
        stream.read(arr_len * 8)
        return f"Vec2[{arr_len}]"
    elif obj_type == 19: # Vec2; TODO
        stream.read(8)
        return "Vec2"
    elif obj_type == 20: return f"Team[{read_num(stream, JavaTypes.BYTE)}]" # Team; TODO
    elif obj_type == 21: # int[]; Basically IntSeq, but who cares
        arr_len = read_num(stream, JavaTypes.SHORT)
        return [read_num(stream, JavaTypes.INT) for _ in range(arr_len)]
    elif obj_type == 22: # Object[]
        arr_len = read_num(stream, JavaTypes.INT)
        return [read_obj(stream) for _ in range(arr_len)]
    elif obj_type == 23: return f"UnitCommand[{read_num(stream, JavaTypes.BYTE)}]" # UnitCommand
    else:
        raise Exception(f"Unknown object type: {obj_type}")

def paste_opacity(bg: Image.Image, fg: Image.Image, pos: tuple[int, int], opacity=1.0):
    if opacity < 0 or opacity > 1:
        raise ValueError("opacity must be >=0 and <=1")

    fg = fg.convert("RGBA")
    alpha = fg.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    fg.putalpha(alpha)
    bg.paste(fg, pos, fg)

def add_outline(image: Image.Image, color: tuple[int, int, int], thickness: int):
    alpha = image.split()[3]
    bigger_alpha = alpha.filter(ImageFilter.MaxFilter(thickness * 2 + 1))
    outline_mask = ImageChops.difference(bigger_alpha, alpha)

    outline = Image.new("RGBA", image.size, (0, 0, 0, 0))
    outline.paste(color, (0, 0), outline_mask)

    return Image.alpha_composite(outline, image)

from PIL import Image, ImageOps

def tint_image(image: Image.Image, color: tuple[int, int, int] | int) -> Image.Image:
    if isinstance(color, int):
        color = (color >> 16, color >> 8 & 0xff, color & 0xff)

    image = image.convert("RGBA")
    grayscale = ImageOps.grayscale(image)
    tinted = Image.new("RGBA", image.size)

    for y in range(image.height):
        for x in range(image.width):
            a = image.getpixel((x, y))[3]
            brightness = grayscale.getpixel((x, y)) / 255
            r = int(color[0] * brightness)
            g = int(color[1] * brightness)
            b = int(color[2] * brightness)
            tinted.putpixel((x, y), (r, g, b, a))

    return tinted

def get_sprite(category: str, name: str):
    return Image.open(f"sprites/blocks/{category}/{name}.png").convert("RGBA")