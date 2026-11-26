# Pirate's Breath — Gameplay Expansion Specification

## Product direction
Expand the existing Bedrock add-on into a One Piece-inspired open-world action RPG. Blox Fruits is a high-level reference for progression and gameplay loops, not a source for copied code or assets. Preserve working mechanics and expand the current BP/RP architecture.

## Devil Fruits
Preserve the fruit registry, IDs, tags, player properties, skill index, cooldowns and awakening state. Every new fruit is a complete vertical slice: fruit item, metadata, skill unlocks, handlers, attack entities, RP models/animations/particles/textures/sounds, localization, cooldowns and mastery.

First requested additions:
1. Gasu Gasu no Mi — canon Logia.
2. Original Mythical Zoan — exact model/name is not locked. Thunderbird was mentioned as a provisional idea only.
3. Mero Mero no Mi — canon Paramecia.
4. Kage Kage no Mi — canon Paramecia.

## Combat and Haki
Expand combos, hit reactions, blocking, dodging, knockback, projectiles, PvP and boss combat using existing event/combat helpers. Preserve Busoshoku, Kenbunshoku, Haoshoku, Ryuo and combined infusion states. Add mastery, advanced applications, effects, cooldowns and counterplay without incompatible parallel properties.

## Fighting styles and equipment
Extend fighting styles, Rokushiki, sword techniques, named weapons and progression. Add ranged weapons if the existing item/animation architecture supports them. Improve fruit storage, inventory organization, equipment slots, accessories, consumables and trade/drop rules. Inventory migration must never silently delete or duplicate items.

## RPG progression
Expand level/XP, fruit mastery, fighting-style mastery, Haki mastery, bounty, money, reputation, factions, titles and achievements. Reuse existing job/faction and bounty structures after their meanings are mapped.

## Quests, NPCs and bosses
Create persistent quest state, repeatable and chained quests, NPC interactions, objectives, rewards, boss AI, drops and respawn behavior. A dedicated quest framework was not identified in the current script inventory, so design it as a new module integrated through the existing runtime.

## World and exploration
Support island/region progression, seas, exploration, marine bases, pirate territories, hidden locations, travel and boss arenas. Respect existing structure/block conventions. Never perform unbounded block replacement or world edits.

## GTA-inspired radial selector
Replace the old status menu only after all its functions have replacement paths. Categories: Devil Fruit abilities; fighting styles; swords; guns/ranged weapons; Haki; special abilities/movement; items/consumables; utility/status. Goals: clear sectors/icons, selected-item highlight, cooldown/availability feedback, expandable sub-wheels, mobile/touch usability, and controller/keyboard support where Bedrock permits.

The current status menu uses `@minecraft/server-ui` ActionFormData. Official DDUI forms provide dynamic controls, but that does not prove a free-floating GTA-style overlay works on every Bedrock client. Prototype supported UI first. A radial-style multi-button selector is the fallback until a true overlay is verified.

## Hotbar reliability
Trace fruit possession → fruit status → unlocked skills → skill-item grant/equip → hotbar slot → item-use event → ability dispatch. Test empty/full inventory, death/respawn, reconnect, fruit switching and awakening. Do not solve missing hotbar items by blindly overwriting fixed slots.

## Acceptance gates
Static validation must pass, BP/RP references must match, IDs must remain stable, and every feature must be tested in the target Bedrock client before it is called complete.
