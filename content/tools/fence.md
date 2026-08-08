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

## Interface overview

| Surface | What is available |
| --- | --- |
| Setup | `init` and `validate` for `fence.toml` rules |
| Checks | Full or `--changed-only` boundary analysis with optional baselines |
| Explanation | `explain <path>` for the rules and findings affecting one file |
| Graphs | Dependency output, including Mermaid and machine-readable reports |

## Main workflows

- Scaffold a rule file, define allowed dependencies, and validate the configuration.
- Check the whole repository in CI or only changed paths during local iteration.
- Create a reviewed baseline for existing debt without hiding new violations.
- Render a dependency graph or explain a single path when a boundary failure needs diagnosis.

## Five-minute example

```bash
kujo run fence.kujo -- check --changed-only --baseline fence-baseline.json
kujo run fence.kujo -- explain src/ui/LoginForm.tsx
```

## What you get

Boundary findings, dependency graphs, explanations, and optional baseline comparisons.

## How it fits

Run beside [ShipCheck](/tools/shipcheck/) and [Concord](/tools/concord/).

## Boundaries

Fence checks architecture; it is not a runtime sandbox or a complete security review.

## Reference

See the [Fence repository](https://github.com/kujolang/fence).
