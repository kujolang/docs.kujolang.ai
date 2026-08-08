---
title: Ward
description: Monitor Dependabot alerts locally and prepare reviewable remediation plans.
template: docs
section: Tools
nav_title: Ward
order: 240
audience: developer
difficulty: advanced
status: local scope verified
version: current
scope: local-first security operations
source_repo: ward
previous: /tools/lens/
next: /tools/howl/
tags: [tool, dependabot, security]
---

## Use it when…

You need a local command center for Dependabot alerts across repositories, deterministic classification, reports, and guarded fix preparation.

## Five-minute example

```bash
ward doctor
ward collect --all
ward plan --unplanned
ward report --since 7d
ward dashboard
```

## What you get

Normalized alert state, deterministic plans, Markdown and JSON reports, a static dashboard, and dry-run fix preparation.

## How it fits

Use [PatchBrief](/tools/patchbrief/) and [ChangeBucket](/tools/changebucket/) to review any approved dependency changes.

## Boundaries

Ward is read-only by default. Live GitHub collection requires approved credentials, and code changes require explicit `--apply`; it does not push or merge automatically.

## Reference

See the [Ward repository](https://github.com/robertdevore/ward).
