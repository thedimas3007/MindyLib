# MindyLib

Python-based parser for Mindustry schematics and maps. WIP

> [!WARNING]
> The library is not ready-to-use.

## TODO

* **Code**
  * [x] Implement game types
  * [x] Copy game blocks
    * [ ] Verify blocks afterward
    * [x] Classes for common blocks in `blocks`
  * [ ] Comprehensive documentation
  * [ ] Mod support as some sort of "plugin"
  * [x] Make layer rendering system
  * [ ] Add Generic block type for `Tile` for better typing
    * `Tile[DuctBridge]`
  * [ ] Default values for specific block types
    * Conveyors, conduits, etc.

* **Minor issues / improvements**:
  * [x] Fix tint for team-tinted blocks
  * [ ] Fix phase bridges having center transparent
  * [ ] Implement seamless conveyors for payload
  * [ ] Conveyors for rounded blocks
  * [ ] Arrows and ends on bridges
  * [ ] Dynamic inputs for `payload mass drivers` and `deconstructors`

* **Rendering implementation progress**
  * [x] Campaign
  * [x] Core
  * [x] Crafting
  * [x] Defense
  * [x] Distribution
  * [x] Experiment
  * [x] Liquid
  * [x] Logic
  * [x] Payload
  * [ ] Power
  * [ ] Production
  * [ ] Sandbox
  * [ ] Turret

* **Schematics**
  * [x] Improved preview generation
    * I mean, dynamic conveyors, colored sorters, etc
    * Maybe show those canvases rendered
  * [x] More information about schematics

* **Maps**
  * *Eventually*

> [!IMPORTANT]
> Environment (walls, floors, etc.) blocks weren't implemented since they're basically useless in schematics.
>
> Blocks are organized by categories from the game's block selector.
> Some special ones have separate categories: campaign, sandbox.
>
> Air blocks in schematics are just `None`
