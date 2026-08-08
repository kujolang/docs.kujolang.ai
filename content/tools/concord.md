---
title: Concord
description: Find drift across code, docs, examples, specs, and generated artifacts.
template: docs
section: Tools
nav_title: Concord
order: 190
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: concord
previous: /tools/patchbrief/
next: /tools/shipcheck/
tags: [tool, drift, docs]
---


## Use it when…

The same contract appears in code, docs, examples, specs, or generated files and you want to know whether the surfaces still agree.

## Interface overview

| Surface | What is available |
| --- | --- |
| Scan | `scan` across the current or selected project directory |
| Focused checks | `check <rule>` for CLI/docs and other known agreement contracts |
| Outputs | Markdown, JSON, output files, and actionable task lists |
| Drift classes | CLI/docs, Spec/Eval, manifest/docs, versions, examples, and generated artifacts |

## Main workflows

- Scan before release to find duplicated facts that no longer agree.
- Run a named check while iterating on one contract, such as CLI documentation.
- Export JSON into CI or write a Markdown report for maintainers.
- Generate tasks from findings while keeping the repository’s declared source of truth explicit.

## Five-minute example

```bash
kujo run concord.kujo -- scan --format json
kujo run concord.kujo -- tasks
```

## What you get

Drift findings, task lists, and a report that points to the source-of-truth mismatch.

## How it fits

Run after [Eval](/tools/eval/) and before [ShipCheck](/tools/shipcheck/).

## Boundaries

Preview/dogfood wording remains visible while the ecosystem continues to stabilize.

## Reference

See the [Concord repository](https://github.com/kujolang/concord).
