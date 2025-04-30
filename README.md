# MindustryParser

Python-based parser for Mindustry schematics and maps. WIP

## TODO

* **Code**
  * [x] Implement game types
  * [ ] Copy game blocks
    * [ ] Verify blocks afterward
    * [ ] Move DefenseBlock into turrets
    * [ ] Classes for common blocks in `blocks`
      * Conveyors, routers, pipes, etc.
      * Will implement same rendering logic
  * [ ] ~~Colorful output of tests~~
  * [ ] Comprehensive documentation
  * [ ] Mod support as some sort of "plugin"

> [!IMPORTANT]  
> Environment (walls, floors, etc.) blocks weren't implemented since they're basically useless in schematics.
> 
> Blocks are organized by categories from the game's block selector.
> Some special ones have separate categories: campaign, sandbox.

* **Schematics**
  * [ ] Improved preview generation
    * I mean, dynamic conveyors, colored sorters, etc
    * Maybe show those canvases rendered
  * [ ] More information about schematics

* Maps
  * *Eventually*