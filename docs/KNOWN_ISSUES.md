# Known Issues and Investigation Queue

## Confirmed observations
1. The user reported that some fruits/skills did not appear in the hotbar after importing and entering a world. The root cause has not yet been isolated.
2. The originally uploaded MCAddon stored its inner packs as `.zip` files. The cleaned combined package uses the expected nested `.mcpack` filenames.
3. The original and clean pack contents match after normalizing their top-level folder prefix; the clean pack is not a rewritten gameplay implementation.
4. Minecraft reported a duplicate during an import attempt. Its exact source is unconfirmed; possible causes include an already registered pack UUID, import-container layout, or an internal identifier collision. Do not guess.
5. No runtime test in Minecraft has been completed from this workspace.

## Hotbar trace
- `scripts/status_akumanomi.js`: creates the fruit skill menu and handles skill selection.
- `scripts/index/skill_item_index.js`: owns skill definitions, unlock levels and skill-item cleanup.
- `scripts/items.js`: contains the slot-8 status/Haki item use handler.
- `scripts/customComp/customComp_item.js`: registers the hotbar custom item.
- `scripts/sneak.js`: cycles slot-8 status/Haki items and other special items.
- `scripts/function.js`: contains inventory give/clear/slot helpers.

The fruit skill selection path currently grants skill items through `giveSkillItem()`, which calls `giveCommand(..., "inventory")`. `giveCommand()` uses `container.addItem()`, so it adds an item to an available inventory slot rather than guaranteeing a particular hotbar slot. This is an important behavior to verify against the user's exact symptom; it is not yet proven to be the reported root cause.

## Next diagnostic actions
- Trace skill unlock and fruit acquisition data against the exact fruit IDs.
- Inspect hotbar occupancy and the return value from inventory add operations.
- Check every item JSON identifier against its script registry and RP texture/attachable reference.
- Check duplicate identifiers and pack UUID/version state before changing identifiers.
- Test empty/full inventory, respawn, reconnect, fruit change and awakening.
