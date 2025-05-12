# MindyLib

Python-based parser for Mindustry schematics and maps. WIP

> [!WARNING]
> The library is not ready-to-use.

## TODO

* **Code**
  * [x] Implement game types
  * [x] Copy game blocks
    * [ ] Verify blocks afterward
    * [ ] Classes for common blocks in `blocks`
      * Conveyors, routers, pipes, etc.
      * Will implement same rendering logic
  * [ ] Clean-up Enums, join mby
  * [ ] Get rid of loads of ifs; implement rotation logic
  * [ ] ~~Colorful output of tests~~
  * [ ] Comprehensive documentation
  * [ ] Mod support as some sort of "plugin"
  * [ ] Make layer rendering system
    * RotatedLayer, TintedLayer, etc
    * So that I won't have to reimplement many block
  * [ ] Add Generic block type for `Tile` for better typing
    * `Tile[DuctBridge]`

* **Minor issues**:
  * [x] Fix tint for team-tinted blocks
  * [ ] Conveyors for rounded blocks 

* **Rendering implementation progress**
  * [x] Campaign
  * [x] Core
  * [x] Crafting
  * [x] Defense
  * [ ] Distribution
  * [ ] Experiment
  * [ ] Liquid
  * [ ] Logic
  * [ ] Payload
  * [ ] Power
  * [ ] Production
  * [ ] Sandbox
  * [ ] Turret

* **Schematics**
  * [ ] Improved preview generation
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
