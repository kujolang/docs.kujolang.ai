---
title: Scent
description: Package focused, bounded, and redacted context for a task.
template: docs
section: Tools
nav_title: Scent
order: 130
audience: developer
difficulty: beginner
status: launch scope
version: current
scope: local-first
source_repo: scent
next: /tools/packwrite/
tags: [tool, context, redaction]
---

# Scent

## Use it when…

The repository is larger than the task and the next agent or reviewer needs a compact, scoped context pack.

## Five-minute example

```bash
kujo run scent.kujo pack --target changed --budget 12000
```

## What you get

Budgeted context, include/exclude decisions, a manifest, and redaction-aware handoff material.

## How it fits

Use [Scout](/tools/scout/) to understand the repo and [PackWrite](/tools/packwrite/) to compile execution packs.

## Boundaries

Context packaging does not replace task contracts or access review.

## Reference

See the [Scent repository](https://github.com/kujolang/scent).

