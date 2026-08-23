---
title: Workcell
description: Run bounded Kujo and agent workflows in disposable Docker or Podman worktrees.
template: docs
section: Tools
nav_title: Workcell
order: 25
audience: developer
difficulty: advanced
status: stable within local and CI scope
version: current
last_updated: 2026-08-23
scope: local and CI
source_repo: workcell
tags: [tool, execution, containers, security]
---

## Use it when…

A workflow needs a disposable Git worktree, bounded container resources, explicit network and filesystem policy, declared artifact export, and an integrity-verifiable receipt.

## Interface overview

`doctor`, `init`, `validate`, `inspect`, `run`, `verify`, and ownership-scoped `clean` form the stable v1 lifecycle. Docker and Podman are supported; `inspect` resolves policy without starting a container.

## Five-minute example

```bash
./bin/workcell init
./bin/workcell validate --file workcell.json
./bin/workcell inspect --file workcell.json --json
./bin/workcell run --file workcell.json --repo . --no-pull
```

## What you get

A run under `.workcell/runs/<run-id>/` with the receipt, manifest, verification result, exported artifacts, and cleanup outcome separated explicitly.

## Boundaries

Workcell does not protect against a compromised daemon or host kernel, provide microVM or hosted multi-tenant isolation, or certify deployment-specific egress and image policy. Run `workcell doctor` on each target host.

## Reference

See the [Workcell repository](https://github.com/kujolang/workcell).
