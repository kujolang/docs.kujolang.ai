---
title: Scent
description: Package focused, bounded, and redacted context for a task.
template: docs
section: Tools
nav_title: Scent
order: 110
audience: developer
difficulty: beginner
status: local scope verified
version: current
scope: local-first
source_repo: scent
previous: /tools/agents-sdk/
next: /tools/fence/
tags: [tool, context, redaction]
---


## Use it when…

The repository is larger than the task and the next agent or reviewer needs a compact, scoped context pack.

## Interface overview

| Surface | What is available |
| --- | --- |
| Selection | Task text, model target, token budget, changed/staged filters, and path selectors |
| Preview | `--dry-run`, compact `--json`, estimates, warnings, and no artifact writes |
| Outputs | `context.md`, `context.json`, `manifest.json`, `files.json`, `redactions.json`, and `metadata.json` |
| Safety | Repository-scoped paths, size limits, deterministic ordering, and pattern-based redaction |

## Main workflows

- Preview a pack to check estimated tokens, selected files, exclusions, and warnings.
- Use repeated `--include` and `--exclude` flags to focus the pack inside the discovered repo root.
- Select changed, staged, or unstaged files when the task follows a specific working-tree state.
- Review redaction metadata before handing the generated Markdown and JSON artifacts downstream.

## Five-minute example

```bash
kujo run /path/to/scent/scent.kujo pack --task "review the current change" --changed --budget 12000 --dry-run --json
```

## What you get

Budgeted context, include/exclude decisions, a manifest, and redaction-aware handoff material.

## How it fits

Use [Scout](/tools/scout/) to understand the repo and [PackWrite](/tools/packwrite/) to compile execution packs.

## Boundaries

Context packaging does not replace task contracts or access review.

## Reference

See the [Scent repository](https://github.com/kujolang/scent).
