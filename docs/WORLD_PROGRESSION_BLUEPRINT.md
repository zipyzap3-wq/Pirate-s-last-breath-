# World and Island Progression Blueprint

## Design goal
Create a Blox Fruits-inspired progression route through One Piece-style seas and islands, using original island layouts, NPCs, quests, enemies and bosses. The route should feel like a connected world rather than disconnected grind arenas.

## Progression layers
### 1. Starting waters
Safe arrival/tutorial area; teach combat, quest acceptance, money, bounty, faction choice and fruit basics. Include starter NPCs, low-tier enemies, a trainer, merchant and a visible route to the next island.

### 2. First sea route
Several islands arranged as a rising difficulty chain. Each island has a distinct enemy group, quest chain, local boss or mini-boss, merchant/trainer and exploration reward. Add optional secrets and rare encounter points. Unlock the next segment through player level plus a quest/boss milestone, not level alone.

### 3. Second sea route
Unlock after a major progression quest. Introduce stronger factions, specialized trainers, advanced weapon styles, demanding bosses and advanced Haki progression. Add repeatable events and group-friendly encounters.

### 4. Third sea / endgame route
High-level islands, elite bosses, raids and fruit-awakening challenges. High bounty and faction reputation have meaningful consequences. Tie rare rewards to defined challenge loops, not random drops alone.

## Island template
Each island defines identity/biome/silhouette, landmarks, arrival and safe zones, travel connection, level band, quest NPCs/chains/rewards, enemy roster/spawn zones/respawns, boss arena/mechanics/drops, merchants/trainers/faction presence, secrets, map label and hazards.

## Quest route
Tutorial quests teach one mechanic at a time. Main route quests connect islands and unlock travel. Side quests reward exploration, bounty/reputation and materials. Repeatable quests provide XP/money. Boss quests define prerequisites, encounter state and reward claims.

## Faction paths
Extend the existing allegiance system:
- Pirate: bounty growth, pirate territory, rival crews and wanted encounters.
- Marine: rank progression, marine bases, patrols and pirate-hunt missions.
- Bounty Hunter: target contracts, capture/defeat objectives and reward claims.

All paths share the world and core progression but vary contracts, reputation and NPC reactions. Do not lock essential progression behind an early faction choice.

## Travel and route readability
Connect islands with boats/sea travel and unlockable fast travel where appropriate. Make the next destination readable through quest text, map markers or NPC directions. Preserve exploration freedom. Respect world bounds, chunk loading and multiplayer state.

## Implementation rules
Keep island, quest, enemy and boss definitions data-driven. Store persistent quest/faction progress separately from transient combat state. Avoid expensive per-tick scans and excessive entity counts. Use bounded structure placement and non-destructive terrain edits. Map existing structures and mobs before creating duplicates.
