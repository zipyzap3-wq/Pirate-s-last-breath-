# Google AI Studio — Master Project Brief

You are editing Pirate's Breath, an existing Minecraft Bedrock add-on. Extend the existing project; do not replace it.

## Read order
1. README.md
2. docs/PROJECT_BASELINE.md
3. docs/GAMEPLAY_SYSTEM_SPEC.md
4. docs/IMPLEMENTATION_ROADMAP.md
5. docs/KNOWN_ISSUES.md
6. The actual source files involved in the task.

## Non-negotiable constraints
- Bedrock Edition only.
- Preserve namespace op_asa:, pack UUIDs, fruit IDs, player properties, scoreboards, tags and working systems.
- Do not renumber or repurpose existing fruit IDs.
- Do not rewrite the project wholesale.
- Read affected source files and callers before editing.
- Implement cross-pack features fully: BP logic/definitions plus RP assets, animations, particles, textures, sounds and localization.
- No fake/placeholder functionality described as complete.
- Never overwrite inventory blindly or lose player items.
- Keep old menu access until the new selector has full feature parity.
- Verify API availability against official Bedrock documentation and exact target version.

## First objectives
1. Find the exact cause of fruit abilities missing from the hotbar. Trace acquisition, fruit state, skill unlock, item grant, inventory slot, hotbar display, use event and ability dispatch.
2. Design a GTA V-inspired radial quick-select with categories for fruit abilities, fighting styles, swords, guns, Haki, special abilities/movement, consumables and utility. Prototype supported UI first; do not assume a true floating overlay exists.
3. Build Gasu Gasu no Mi as the first complete new fruit vertical slice.
4. Add Mero Mero no Mi and Kage Kage no Mi.
5. Design one original Mythical Zoan. Thunderbird is a candidate only, not a locked concept.
6. Expand inventory/equipment, mastery, XP, bounty, factions, quests, NPCs, bosses, islands, seas and travel.

## Required work method
Inspect source → map dependencies → propose minimal change → implement → run static audit → run official Creator Tools validation → package → test in Bedrock → report exact results. If runtime testing cannot be performed, say so.

## Deterministic tools
- python tools/bedrock_audit.py --project .
- python tools/package_addon.py --project .
- Mojang Minecraft Creator Tools: https://mctools.dev
- Blockbench: https://www.blockbench.net/
- Snowstorm: https://snowstorm.app/

## Required report
List files changed, why each changed, features added, preserved behavior, validation output, actual in-game tests, target version/device, and remaining issues. Static checks are not runtime proof.
