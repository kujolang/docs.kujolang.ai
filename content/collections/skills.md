---
title: Skills
description: Install, select, and validate Kujo-specific Agent Skills.
template: docs
section: Collections
nav_title: Skills
order: 10
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-25
scope: local-first
source_repo: kujo-skills
previous: /showcases/
next: /collections/workflows/
tags: [collection, skills, agents]
---


Use the skill catalog to select a focused operating contract for a task. Read the skill instructions, follow their required evidence, and keep the selected skill's scope visible in the handoff.

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
