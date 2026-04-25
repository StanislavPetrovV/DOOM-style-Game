# Architecture

The game code now lives in the `game/` package, split by responsibility to make maintenance easier.

## Main Flow

1. `game/app.py` creates the window, initializes systems, and runs the main loop.
2. `game/player.py` handles input, movement, damage, and recovery.
3. `game/raycasting.py` computes visible wall columns.
4. `game/object_renderer.py` draws the background, walls, sprites, and HUD.
5. `game/object_handler.py` creates decorative sprites and enemies.
6. `game/npc.py` controls enemy AI, damage, and animations.
7. `game/pathfinding.py` maintains the NPC navigation graph.

## Resources

- `game/assets.py` resolves absolute paths to `resources/`.
- `resources/textures/` contains walls, HUD, and screens.
- `resources/sprites/` contains static sprites, animated sprites, NPCs, and the weapon.
- `resources/sound/` contains sound effects and music.

## Entry Points

- `main.py` remains as a compatibility launcher.
- `python -m game` also starts the game.
