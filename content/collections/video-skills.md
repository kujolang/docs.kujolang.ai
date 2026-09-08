---
title: Make videos with Kujo Skills
description: Install Kujo's HyperFrames video skills, choose from ten styles, and set an ElevenLabs narrator for demos, launches, explainers, or releases.
template: docs
section: Collections
nav_title: Video skills
order: 15
audience: developer
difficulty: intermediate
status: released guidance
version: 0.7.0
last_updated: 2026-09-08
scope: local-first
source_repo: kujo-skills
previous: /collections/skills/
next: /collections/workflows/
tags: [collection, skills, video, hyperframes]
---

Kujo's video skills help a coding agent turn source material into an editable HyperFrames composition and a rendered video. They cover demos, launches, explainers, feature reveals, integrations, and release announcements. ElevenLabs supplies narration when requested; the agent can also make an unnarrated video.

The two video skills ship in [Kujo Skills v0.7.0](https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0), alongside the VideoOps production skills. Their source now lives in `kujo-skills`, rather than `kujo-hyperframes`.

## Choose the entry point

| Skill | Use it for |
| --- | --- |
| `kujo-video-styles` | Ten reusable styles with different durations and story structures. Choose a style explicitly or ask the agent to choose. |
| `kujo-release-video` | A fixed 15-second, 1920×1080, 24 fps monochrome release announcement with narration, original ambient music, and sound effects. |
| `kujo-videoops-workflows` | A full production team covering the brief, media, composition, review, and delivery. |

The ten styles guide the story and motion. HyperFrames owns the native composition, preview, and render workflow. These skills are instructions and scripts, not a hosted video service or a substitute for the agent host's permissions.

## Install in Codex

From a new working directory, install the released skill folders:

```bash
git clone --branch v0.7.0 --depth 1 https://github.com/kujolang/kujo-skills.git
mkdir -p ~/.codex/skills
cp -R kujo-skills/skills/kujo-video-styles ~/.codex/skills/
cp -R kujo-skills/skills/kujo-release-video ~/.codex/skills/
```

For custom styles, also install the [native HyperFrames skills](https://github.com/heygen-com/hyperframes#skills):

```bash
npx hyperframes skills update
```

Use the destination supported by your agent host if it does not read `~/.codex/skills`. Copy each complete skill directory, including its scripts, references, and assets. The fixed release preset is bundled; custom video styles also rely on native HyperFrames skills. Install the tools required by the selected workflow before rendering.

## Ten styles and example prompts

These prompts are starting points. Replace the bracketed source with a local file, inspected URL, changelog, product brief, or pull request. Durations are the style defaults, not a promise that any script will fit without editing.

| Style ID | Best fit | Default duration | Default voice |
| --- | --- | --- | --- |
| `cinematic-hero-launch` | A major launch with intrigue, proof, and a thesis | 50 seconds | Brian |
| `apple-style-micro-launch` | One polished product interaction, often muted | 12 seconds | Sarah |
| `release-notes-changelog` | One release headline and supporting changes | 45 seconds | Daniel |
| `real-product-proof-reel` | A sequence showing real product capabilities | 40 seconds | Chris |
| `editorial-thesis-launch` | A source-backed argument about a product or idea | 45 seconds | George |
| `feature-reveal` | Friction, changed behavior, and the payoff | 25 seconds | Jessica |
| `integration-partnership-launch` | A real workflow crossing two systems | 25 seconds | Eric |
| `engineering-pr-to-video` | A problem, code change, mechanism, and evidence | 60 seconds | Alice |
| `short-product-launch` | A compact product introduction led by footage | 20 seconds | Matilda |
| `kinetic-release-drop` | One line, a visual mechanism, and a reveal | 8 seconds | Liam |

```text
Use $kujo-video-styles to make a cinematic-hero-launch for [product] from [source].
Use $kujo-video-styles to make a muted apple-style-micro-launch showing [interaction].
Use $kujo-video-styles to make a release-notes-changelog for [version] from [changelog].
Use $kujo-video-styles to make a real-product-proof-reel using [real captures].
Use $kujo-video-styles to make an editorial-thesis-launch explaining [argument] from [evidence].
Use $kujo-video-styles to make a feature-reveal showing [before and after].
Use $kujo-video-styles to make an integration-partnership-launch for [workflow and sources].
Use $kujo-video-styles to make an engineering-pr-to-video from [pull request].
Use $kujo-video-styles to make a short-product-launch for [tool] from [source].
Use $kujo-video-styles to make a kinetic-release-drop announcing [one source-backed change].
```

For the fixed release preset:

```text
Use $kujo-release-video to make a release film for [tool/version] from
[release information], in a new folder. Generate the ElevenLabs narration
and use the original ambient music and sound effects workflow.
```

## Choose the narrator and presentation

The fixed preset defaults to Brian. The ten styles use the voices in the table, and explicit voice choices take precedence. Voice names do not guarantee an accent; ask the agent to verify the provider's current voice metadata. For example:

```text
Use $kujo-video-styles to make a 40-second release-notes-changelog from
[source]. Use Eric's American voice from ElevenLabs. Verify the voice
before generation. Do not add captions. Use Departure Mono for the
closing headline.
```

You can supply an ElevenLabs voice ID instead of a name, or ask for a silent video. Store credentials in the configured environment or credential store, never in the brief, script, or repository. Generating provider media requires account access, an available allowance, and authorization; installing a skill does not supply them. Check the [provider's usage rights](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform) for the generation-time plan.

## Automate and review

The style CLI exposes `list`, `route`, `init`, `validate`, and `prepare`:

```bash
python3 ~/.codex/skills/kujo-video-styles/scripts/video_styles.py list
python3 ~/.codex/skills/kujo-video-styles/scripts/video_styles.py route --brief brief.json
```

Read the [versioned pipeline contract](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-video-styles/references/pipeline.md) before authoring a JSON brief. `prepare` creates an editable starter; it does not invent claims, generate narration, or certify the finished video. The agent still needs to inspect sources, author the composition, check frame boundaries and text, review audio, and render through HyperFrames.

VideoOps team productions use the shared media provider workflow in [`kujo-agents/videoops/tools`](https://github.com/kujolang/kujo-agents/tree/main/videoops/tools). Keep original media and receipts, reuse existing takes when rebuilding, and distinguish technical checks from a complete visual and listening review.

## Source and related guides

- [Kujo Video Styles source at v0.7.0](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-video-styles/SKILL.md)
- [Kujo Release Video source at v0.7.0](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-release-video/SKILL.md)
- [Released voice defaults and overrides](https://github.com/kujolang/kujo-skills/blob/v0.7.0/skills/kujo-video-styles/references/voices.md)
- [Browse all Kujo Skills](https://kujolang.ai/ecosystem/skills/)
- [Build with AI and agents](/build/ai-and-agents/)
