---
title: Muzzle
description: Run noisy workflows quietly while preserving complete logs and summaries.
template: docs
section: Tools
nav_title: Muzzle
order: 150
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: muzzle
previous: /tools/leash/
next: /tools/runledger/
tags: [tool, workflows, logs]
---


## Use it when…

A trusted workflow produces too much console noise but its complete log and outcome still need to remain available.

## Interface overview

| Surface | What is available |
| --- | --- |
| Setup | `muzzle init` and workflow definitions under `.muzzle/workflows/` |
| Execution | `muzzle run <name>`, arguments, timeouts, dry-run, JSON, and verbose modes |
| Review | Workflow listing, complete logs, summaries, and report paths |
| Maintenance | Manifests, meaningful exit codes, loop mode, and `muzzle clean` |

## Main workflows

- Initialize repo-local workflow definitions and review the command each one will run.
- Execute a named workflow with compact output while preserving the complete log.
- Use `--dry-run` before risky or environment-specific workflows and `--json` in automation.
- Open the report or rerun with `--verbose` when the compact summary is not enough.

## Five-minute example

```bash
muzzle init
muzzle run build --dry-run
muzzle run build --json
```

## What you get

Quiet terminal output, a complete log, a summary, and an exit status that remains meaningful to automation.

## How it fits

Use Muzzle around [PackWrite](/tools/packwrite/) or a bounded [Dispatch](/tools/dispatch/) run.

## Boundaries

Run trusted scripts only. Quiet output is not reduced scrutiny.

## Reference

See the [Muzzle repository](https://github.com/kujolang/muzzle).
