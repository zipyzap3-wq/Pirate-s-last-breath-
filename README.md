# Pirate's Breath — Bedrock Add-on Project

This repository contains the exported source and project references for the Pirate's Breath Minecraft Bedrock add-on.

## Project direction
Expand the existing add-on into a One Piece-inspired open-world action RPG. Blox Fruits is a broad gameplay reference for exploration, island progression, quests, bosses, fruit mastery and combat loops; do not copy its code or proprietary assets.

## Project documents
- `docs/PROJECT_BASELINE.md` — inspected pack structure, versions and source map.
- `docs/GAMEPLAY_SYSTEM_SPEC.md` — requested gameplay systems.
- `docs/RADIAL_SELECTOR_DESIGN.md` — radial menu mapping and UI constraints.
- `docs/WORLD_PROGRESSION_BLUEPRINT.md` — sea/island progression route.
- `docs/IMPLEMENTATION_ROADMAP.md` — staged implementation and acceptance gates.
- `docs/AI_STUDIO_HANDOFF.md` — instructions for later Google AI Studio work.
- `docs/TOOLS.md` — useful non-AI Bedrock development tools.

## Source-pack note
The original installable Behavior Pack and Resource Pack are preserved separately from this text-export repository. The source export contains 3,400 text/code files across nine `SOURCE_PART_*.txt` files; binary assets are indexed in `FILE_INDEX.csv` but are not embedded in those text exports. Use the original/clean pack archives as the source of binary assets.

## Preservation rules
Keep the existing `op_asa:` namespace, fruit identifiers, player properties, scoreboards, tags and working systems stable. Read the implementation before changing it. Do not mark work complete without static validation and target-client testing.
