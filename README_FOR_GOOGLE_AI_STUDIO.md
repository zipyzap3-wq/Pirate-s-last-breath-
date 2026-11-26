# Pirate's Breath — Google AI Studio Project Handoff

This repository contains a text/code export and the project specifications for the Minecraft Bedrock add-on Pirate's Breath. The installable Behavior Pack and Resource Pack are preserved separately as complete archives; binary assets are not embedded in the source text export.

## Read these first
1. `README.md` — project direction and preservation rules.
2. `docs/PROJECT_BASELINE.md` — real pack inventory, manifest versions, architecture and static audit evidence.
3. `docs/GAMEPLAY_SYSTEM_SPEC.md` — complete requested expansion systems.
4. `docs/IMPLEMENTATION_ROADMAP.md` — staged work order.
5. `docs/AI_STUDIO_HANDOFF.md` — strict instructions for future edits.
6. `docs/TOOLS.md` — non-AI Bedrock tools.

## Source files
- `SOURCE_PART_01.txt` through `SOURCE_PART_09.txt`: 3,400 text/code files with explicit source-path headers.
- `FILE_INDEX.csv`: inventory of all 4,633 original pack files, including binary assets.
- `ADDON_OVERVIEW.md`: source export summary.

## Authoritative implementation
The original add-on consists of a Behavior Pack and Resource Pack. The BP owns gameplay scripts, items, entities, blocks, functions and progression; the RP owns textures, models, animations, particles, sounds and localization. The source namespace is `op_asa:`.

The source text export is not an installable add-on. Binary assets are indexed but not included in the text parts. Use the preserved complete pack archives as the source for binary assets and final packaging.

## First work items
1. Diagnose the reported fruit/skill hotbar problem from acquisition through inventory, hotbar and item-use dispatch.
2. Map all functions in the existing status menu to the GTA-inspired radial selector.
3. Prototype the UI using supported Bedrock APIs; do not assume a free-floating radial overlay is supported until tested on the target client.
4. Implement Gasu Gasu no Mi as the first complete new fruit.
5. Continue with Mero Mero no Mi, Kage Kage no Mi and the original Mythical Zoan. Thunderbird is only a provisional concept.

## Rules
- This is Minecraft Bedrock, not Java Edition.
- Preserve existing fruit IDs, UUIDs, player properties, scoreboards, tags, helpers and working gameplay.
- Read source and callers before editing.
- Never replace the add-on wholesale.
- A new fruit must be integrated across both packs, not added as a lone script.
- Run the local audit and Mojang Minecraft Creator Tools validation.
- Report exact files changed, validation results and runtime tests. Do not describe static checks as in-game testing.
- No AI API or agent setup is part of this project workflow.
