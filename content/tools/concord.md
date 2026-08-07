---
title: Concord
description: Find drift across code, docs, examples, specs, and generated artifacts.
template: docs
section: Tools
nav_title: Concord
order: 200
audience: developer
difficulty: intermediate
status: preview / dogfood
version: current
scope: local-first
source_repo: concord
next: /tools/shipcheck/
tags: [tool, drift, docs]
---

# Concord

## Use it when…

The same contract appears in code, docs, examples, specs, or generated files and you want to know whether the surfaces still agree.

## Five-minute example

```bash
concord scan --format json
concord report --format markdown
```

## What you get

Drift findings, task lists, and a report that points to the source-of-truth mismatch.

## How it fits

Run after [Eval](/tools/eval/) and before [ShipCheck](/tools/shipcheck/).

## Boundaries

Preview/dogfood wording remains visible while the ecosystem continues to stabilize.

## Reference

See the [Concord repository](https://github.com/kujolang/concord).

