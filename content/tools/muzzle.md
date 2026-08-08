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
scope: local-first
source_repo: muzzle
previous: /tools/leash/
next: /tools/runledger/
tags: [tool, workflows, logs]
---


## Use it when…

A trusted workflow produces too much console noise but its complete log and outcome still need to remain available.

## Five-minute example

```bash
kujo run muzzle.kujo run --workflow ./workflow.yml
```

## What you get

Quiet terminal output, a complete log, a summary, and an exit status that remains meaningful to automation.

## How it fits

Use Muzzle around [PackWrite](/tools/packwrite/) or a bounded [Dispatch](/tools/dispatch/) run.

## Boundaries

Run trusted scripts only. Quiet output is not reduced scrutiny.

## Reference

See the [Muzzle repository](https://github.com/kujolang/muzzle).

