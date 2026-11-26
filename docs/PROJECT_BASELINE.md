# Pirate's Breath — Project Baseline

## Pack inventory
The original uploaded `Pirate-s_Breath.mcaddon` contains nested BP and RP archives. The cleaned combined package correctly nests two `.mcpack` files. The extracted pack contents are 4,633 files:

| Pack | Files | JSON/JSONC | Other |
|---|---:|---:|---|
| Behavior Pack | 1,510 | 1,364 | 80 JavaScript modules |
| Resource Pack | 3,123 | 1,913 | models, textures, animations, particles, sounds |

The Behavior Pack contains 38 fruit-specific JavaScript modules.

## Manifest baseline
Behavior Pack header UUID `7abcb8fa-d0b1-4167-ac8c-bf421e3b9efc`; module UUID `52697c72-170c-419c-b141-9dc44408627b`; RP dependency UUID `b34b6e61-3ecb-4336-92b2-4c1acdc72557`; version `76.0.0`; minimum engine `1.21.60`; script dependencies `@minecraft/server 2.8.0`, `@minecraft/server-ui 2.1.0`.

Resource Pack header UUID `b34b6e61-3ecb-4336-92b2-4c1acdc72557`; module UUID `edbf7ead-9a19-46f5-b6cc-2f554db0f9df`; version `76.0.0`; minimum engine `1.21.60`.

The code header mentions a 1.21.100-era build. The intended compatibility test target from the earlier project discussion is Bedrock beta 26.70 (engine 1.26.70). The main pack remains at its original 1.21.60 minimum and server API 2.8.0 until compatibility is checked and tested. A separate prototype package declares engine 1.26.70 and server API 2.11.0; it is not the main source pack and must not be merged without review.

## Architecture map
| System | Important source path |
|---|---|
| Runtime/event wiring | `BP/scripts/main.js` |
| Fruit registry | `BP/scripts/index/item_index.js` |
| Fruit lookup | `BP/scripts/akumanomi.js` |
| Fruit abilities | `BP/scripts/akumanomi/*.js` |
| Skill registry/inventory | `BP/scripts/index/skill_item_index.js` |
| Fruit status/skill selection | `BP/scripts/status_akumanomi.js` |
| Haki | `BP/scripts/status_haki.js`, `BP/scripts/haki.js` |
| Fighting styles | `BP/scripts/status_fighting.js`, `BP/scripts/fighting.js` |
| Sword techniques | `BP/scripts/status_katanawaza.js`, `BP/scripts/katanawaza.js` |
| Rokushiki | `BP/scripts/rokushiki.js` |
| Factions/allegiance | `BP/scripts/status_job.js` |
| Status hub | `BP/scripts/status.js` |
| Inventory helpers | `BP/scripts/function.js` |
| Custom components | `BP/scripts/customComp/` |
| Models/textures/animations/sounds | `RP/` |

## Static audit evidence
3,277 JSON/JSONC files parsed successfully; 80 JS files scanned with no unresolved relative imports; BP dependency UUID matches RP header UUID. No Minecraft runtime test has yet been completed.

## Compatibility rules
The fruit catalogue uses existing numbered IDs (up to 40) and namespace `op_asa:`. Do not renumber IDs or change existing property meanings without a migration plan. New fruits require coordinated registry, skill, item, script, entity, RP asset, localization, cooldown and progression work.
