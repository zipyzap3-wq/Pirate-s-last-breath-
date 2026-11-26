# Radial Selector — Interaction and Integration Design

## Purpose
Replace the current multi-page status/skill browsing experience with a GTA V-inspired quick-select system while preserving every existing gameplay action. Prioritize touch controls; a true free-floating radial overlay is a later technical gate, not an assumption.

## Existing functions that must survive
| Current status-menu entry | New selector destination |
|---|---|
| Allegiance/job | Utility → Faction |
| Devil Fruit status and skills | Devil Fruit → Fruit-specific abilities |
| Haki infusion | Haki → Infusion modes |
| Fighting style | Fighting Style → Equipped style and techniques |
| Sword techniques | Swords → Equipped sword and techniques |
| Rokushiki | Special → Rokushiki/movement |
| Money | Utility → Currency/status |
| Acquired Haki abilities | Haki → Learned abilities |
| Help | Utility → Help and controls |
| Operator/creative tools | Separate privileged/admin page; never shown to ordinary players |

The slot-8 item currently cycles Status, Haoshoku and Kenbunshoku variants when the player sneaks. Preserve those quick actions during the transition.

## Top-level categories
1. Devil Fruit
2. Fighting Style
3. Swords
4. Guns / Ranged
5. Haki
6. Special / Movement
7. Items / Consumables
8. Utility / Status

Hide or visibly lock categories when their content is unavailable.

## Fruit sub-wheel
- Show current fruit and mastery.
- List only skills unlocked by existing fruit mastery.
- Distinguish unlocked, equipped, on cooldown and unavailable.
- Retain favorites and allow favorite skills to occupy quick slots.
- Use the existing fruit skill registry as the source of truth.

## Selection behavior
This is a quick-equip/quick-access interface, not a replacement for ability implementations. Route selections through existing skill-item and ability dispatch logic so cooldowns, fruit-state checks, transformations and inventory rules remain intact. Do not bypass current item-use handlers.

## Bedrock UI implementation gate
The project currently uses `@minecraft/server-ui` ActionFormData and ModalFormData. DDUI provides dynamic form components, but a form is not automatically a true radial HUD overlay. Prototype in this order:
1. Mobile-first category selector using supported form APIs.
2. Dynamic DDUI form only if the target engine/API exposes required features.
3. True custom HUD overlay only after a minimal proof-of-concept is imported and tested on Bedrock beta 26.70.

If the overlay is unsupported or unstable, ship a polished radial-style category menu with nested pages rather than a broken overlay.

## Acceptance tests
- All old status-menu actions remain reachable.
- Ordinary players cannot access operator/creative actions.
- Locked skills, cooldowns and transformations behave as before.
- No item is duplicated, deleted or overwritten during selection.
- Touch controls work; no keyboard-only gesture is required.
- Cancel/back returns to the correct parent page.
