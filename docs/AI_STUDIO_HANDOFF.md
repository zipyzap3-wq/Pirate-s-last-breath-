# Google AI Studio Handoff

This is a future handoff contract. No AI service or API is required to build or validate the add-on.

## Source hierarchy
1. Extracted Behavior Pack and Resource Pack are authoritative.
2. `docs/PROJECT_BASELINE.md` maps the inspected implementation.
3. `docs/GAMEPLAY_SYSTEM_SPEC.md` defines requested features.
4. `docs/IMPLEMENTATION_ROADMAP.md` defines order and acceptance gates.
5. Nine `SOURCE_PART_*.txt` files and `FILE_INDEX.csv` are text-export references; binary assets are not contained in the text export.

## Mandatory rules
- Read relevant source files and callers before editing.
- Preserve `op_asa:`, fruit IDs, UUIDs, player properties, scoreboards, tags and inventory state.
- Do not replace the add-on with an unrelated fresh project.
- A new fruit is not complete if only one JS file or item definition was added.
- Extend existing helpers/event wiring; avoid duplicate event subscriptions and parallel systems.
- Keep the old status menu available until the radial selector has feature parity.
- Check official Bedrock Script API documentation; do not invent unsupported APIs.
- Keep generated builds out of source folders.
- Report changed files, validation results, runtime test version/device and remaining issues.
- Never describe static validation as an in-game test.

## First tasks
1. Diagnose the fruit/skill hotbar problem end-to-end.
2. Map every status-menu action to its future radial destination.
3. Prototype supported UI and document whether a true overlay works on the target client.
4. Implement Gasu Gasu no Mi as the first complete new fruit.
5. Continue with Mero Mero, Kage Kage and the original Mythical Zoan.

## Validation
Use Mojang Minecraft Creator Tools after local static checks. The final MCAddon must contain two nested files ending in `.mcpack` at its root, not loose pack folders or nested `.zip` files. Check BP dependency UUID against RP header UUID.
