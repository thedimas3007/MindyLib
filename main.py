from rich import inspect

from g_types import Schematic

s = Schematic.from_file("canv2.msch")
s.render_canvases()
inspect(s)