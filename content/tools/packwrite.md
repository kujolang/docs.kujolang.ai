---
title: PackWrite
description: Compile repeatable agent execution packs from context and prompts.
template: docs
section: Tools
nav_title: PackWrite
order: 210
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: packwrite
previous: /tools/shipcheck/
next: /tools/casefile/
tags: [tool, agents, packs]
---


## Use it when…

A team repeats the same agent workflow and needs the context, prompt, model configuration, and evidence contract to be inspectable.

## Interface overview

| Surface | What is available |
| --- | --- |
| Generate | `packwrite init [file]` builds an `agent/` pack from `MEGA_PROMPT.md` |
| Validate | Deterministic `validate` plus environment-aware `doctor --strict` |
| Prompts | `prompt <target>` for implementation and review agents |
| Configuration | `packwrite.toml`, provider/model settings, and offline fake-response tests |

## Main workflows

- Preview pack generation with `--dry-run` before writing the repo-local `agent/` directory.
- Validate the generated execution pack before handing it to an implementation agent.
- Print the exact prompt for a supported target so it can be piped without decoration.
- Use `doctor` to separate config, endpoint, credential, and generated-state problems.

## Five-minute example

```bash
packwrite init MEGA_PROMPT.md --dry-run
packwrite validate
packwrite prompt codex-review
```

## What you get

An execution pack, prompt, config, doctor output, and deterministic validation result.

## How it fits

Compile from [Scent](/tools/scent/) and run quietly with [Muzzle](/tools/muzzle/).

## Boundaries

PackWrite is a local/team workflow compiler; provider and hosted execution remain separate concerns.

## Reference

See the [PackWrite repository](https://github.com/kujolang/packwrite).
