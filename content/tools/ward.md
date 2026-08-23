---
title: Ward
description: Monitor Dependabot alerts locally and prepare reviewable remediation plans.
template: docs
section: Tools
nav_title: Ward
order: 240
audience: developer
difficulty: advanced
status: private preview
version: current
last_updated: 2026-08-23
scope: local-first security operations
source_repo: ward
previous: /tools/lens/
next: /tools/howl/
tags: [tool, dependabot, security]
---

## Use it when…

You need a local command center for Dependabot alerts across repositories, deterministic classification, reports, and guarded fix preparation.

## Interface overview

| Surface | What is available |
| --- | --- |
| Collect | `ward collect --all` reads configured GitHub Dependabot alerts |
| Decide | `plan --unplanned` and deterministic alert classification |
| Review | Markdown/JSON reports plus a local static dashboard |
| Remediate | Dry-run fix preparation; changes require explicit `--apply` |

## Main workflows

- Run `doctor`, configure repositories, and collect alerts with a token limited to required scopes.
- Classify unplanned alerts and review suggested ecosystem-specific commands.
- Generate a recent report or open the dashboard for cross-repository triage.
- Apply an approved safe fix explicitly, then review and push it through normal repository controls.

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

Ward source is currently a private repository, so public source access and installation are not available. Treat this page as capability orientation rather than public onboarding.
