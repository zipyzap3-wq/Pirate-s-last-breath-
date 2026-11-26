# Implementation Roadmap

1. **Baseline and preservation — complete:** extract/map BP/RP; preserve IDs/UUIDs; establish audit and packaging workflow.
2. **Hotbar/runtime diagnosis:** trace `status_akumanomi.js`, `index/skill_item_index.js`, `items.js`, `customComp/customComp_item.js`, `sneak.js` and inventory helpers. Find root cause before editing. Test full/empty inventory, respawn, reconnect and fruit switching.
3. **Radial selector:** inventory every current status-menu action. Prototype mobile-friendly UI using supported Bedrock APIs. Investigate a true overlay only after checking target-client support. Keep old menu until feature parity.
4. **First fruit vertical slice:** implement Gasu Gasu no Mi using the closest existing Logia pattern. Complete registry, skills, items, scripts, entities, assets, localization, cooldowns and mastery. Validate/test.
5. **First fruit batch:** implement Mero Mero, Kage Kage and the original Mythical Zoan. Thunderbird remains provisional, not locked.
6. **Core RPG:** inventory/equipment, fighting styles, swords/ranged weapons, Haki mastery, XP, bounty, reputation, factions, titles and achievements.
7. **World loop:** quest state, NPCs, quest chains, rewards, bosses, drops, respawns, island/sea progression and travel.
8. **Stabilization:** full validation, asset/reference checks, target-beta compatibility, import/world-load tests and multiplayer checks where possible. Deliver separate BP/RP and combined MCAddon with test report.

Work from a reversible development copy. Completion requires evidence, not just generated files. Do not overwrite working systems wholesale.
