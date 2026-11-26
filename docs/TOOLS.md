# Recommended Bedrock Development Tools

These are deterministic development tools, not AI agents or API integrations.

1. **Mojang Minecraft Creator Tools** — official validator, packager and asset renderer: https://mctools.dev and https://github.com/Mojang/minecraft-creator-tools. Use the Inspector or CLI for schema/platform checks after the local audit. Current Microsoft documentation lists Node.js 22+ for the CLI.
2. **Blockbench** — inspect/edit Bedrock entity models and animations: https://www.blockbench.net/.
3. **Snowstorm** — create/preview particle effects: https://snowstorm.app/.
4. **Bedrock Builder** — optional Node.js pipeline for copying packs, bundling scripts and packaging MCAddons: https://github.com/gabriel-aplok/bedrock-builder. Adopt only after verifying it preserves custom components, scripts, assets and manifests.

The repository contains the source export and file index. Complete binary assets remain in the preserved original/clean pack archives and must be included in a full installable build.
