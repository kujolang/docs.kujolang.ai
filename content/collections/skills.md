---
title: Skills
description: Install and use the 135 Kujo Skills in v0.7.0, including development, WebOps, VideoOps, and ten HyperFrames video styles.
template: docs
section: Collections
nav_title: Skills
order: 10
audience: developer
difficulty: intermediate
status: local scope verified
version: 0.7.0
last_updated: 2026-09-08
scope: local-first
source_repo: kujo-skills
previous: /showcases/
next: /collections/video-skills/
tags: [collection, skills, agents]
---


Use the skill catalog to select a focused operating contract for a task. Read the skill instructions, follow their required evidence, and keep the selected skill's scope visible in the handoff.

[Kujo Skills v0.7.0](https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0) contains **135 skills** for development, WebOps, publishing, and video production. Browse the [complete website catalog](https://kujolang.ai/ecosystem/skills/) or the [versioned source index](https://github.com/kujolang/kujo-skills/blob/v0.7.0/SKILLS_INDEX.md).

## Make videos with your agent

Use [`kujo-video-styles`](/collections/video-skills/) for product demos, launches, feature reveals, integrations, engineering explainers, and release announcements. It supplies ten reusable styles over the native HyperFrames workflow, with per-style ElevenLabs narrator defaults and your own voice overrides.

Use `kujo-release-video` for the fixed 15-second monochrome release preset. For a production team spanning planning, acquisition, editing, review, and delivery, start with `kujo-videoops-workflows`. The shared media execution package lives in `kujo-agents/videoops/tools`; the skills do not bundle that runtime or grant provider access.

[Install the video skills and choose a style](/collections/video-skills/).

## Start with the Kujo Way

Use [`kujo-way-development`](https://kujolang.ai/ecosystem/skills/kujo-way-development/) when building or substantially reviewing a Kujo project that crosses language, SDK, agent, workflow, security, and validation boundaries. It gives an agent one compact operating loop:

```text
Route -> Contract -> Inspect -> Implement -> Execute -> Challenge -> Record -> Stop
```

Install it from the released skills repository:

```bash
git clone https://github.com/kujolang/kujo-skills.git
mkdir -p ~/.codex/skills
cp -R kujo-skills/skills/kujo-way-development ~/.codex/skills/
```

Invoke it as `$kujo-way-development`. For a syntax-only question, use `kujo-core-language`; for work contained within one ecosystem tool, prefer that tool's focused workflow skill.

- [Read the complete skill source](https://github.com/kujolang/kujo-skills/blob/main/skills/kujo-way-development/SKILL.md)
- [Browse the released skills index](https://github.com/kujolang/kujo-skills/blob/main/SKILLS_INDEX.md)

## Browse the catalog

```bash
rg --files skills | sort
```

The collection is guidance and workflow glue; it is not a hosted agent marketplace.
