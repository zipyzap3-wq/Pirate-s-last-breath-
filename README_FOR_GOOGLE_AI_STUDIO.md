# Pirate's Breath — Google AI Studio Source Pack

## What this pack contains
- `SOURCE_PART_01.txt` through `SOURCE_PART_09.txt`: readable text source files concatenated with explicit file-path headers.
- `FILE_INDEX.csv`: inventory of every file in the add-on, including non-text assets.
- `ADDON_OVERVIEW.md`: package structure and upload/use instructions.

## Original package structure
The uploaded `.mcaddon` contains two nested archives:
- `Pirate's_Breath_BP.zip` — behavior pack
- `Pirate's_Breath_RP.zip` — resource pack

## Source coverage
Text/code files included: 3,400 (`.json`, `.js`, `.mcfunction`, `.txt`, `.lang`, `.material`).
All other files (textures, audio, structures, and other binary assets) are listed in `FILE_INDEX.csv` but are not converted into text. Their original binary data is not included in this text pack.

## How to use in Google AI Studio
1. Open Google AI Studio and start a prompt/chat.
2. Upload the `SOURCE_PART_*.txt` files (you may need to upload them in batches).
3. Upload `ADDON_OVERVIEW.md` and `FILE_INDEX.csv`.
4. Tell the model to treat the file-path headers as the authoritative paths and to inspect relevant files before proposing changes.
5. For actual add-on editing/testing, retain the original `.mcaddon` as the asset source. This text pack is for understanding and code analysis; it is not itself an installable Minecraft add-on.

## Important
This is a format conversion, not a code repair or modernization. File contents are preserved as-is. Do not assume every behavior can be understood from text alone: models, textures, sounds, structures, and cross-file references may need inspection in the original pack.
