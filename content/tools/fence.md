---
title: Fence
description: Check architecture boundaries and import rules.
template: docs
section: Tools
nav_title: Fence
order: 120
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: fence
previous: /tools/scent/
next: /tools/watchdog/
tags: [tool, architecture, boundaries]
---


## Use it when…

The repository has architectural boundaries, import rules, or a baseline that should fail loudly when changed.

## Five-minute example

```bash
fence check --changed-only --baseline fence-baseline.json
```

## What you get

Boundary findings, dependency graphs, explanations, and optional baseline comparisons.

## How it fits

Run beside [ShipCheck](/tools/shipcheck/) and [Concord](/tools/concord/).

## Boundaries

Fence checks architecture; it is not a runtime sandbox or a complete security review.

## Reference

See the [Fence repository](https://github.com/kujolang/fence).

