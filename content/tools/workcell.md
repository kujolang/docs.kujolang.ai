---
title: Workcell
description: Run bounded Kujo and agent workflows with Workcell 1.1's stable Docker and Podman lifecycle.
template: docs
section: Tools
nav_title: Workcell
order: 25
audience: developer
difficulty: advanced
status: stable within local and CI scope
version: current
last_updated: 2026-09-04
scope: local and CI
source_repo: workcell
tags: [tool, execution, containers, security]
---

## Use it when…

A workflow needs a disposable Git worktree, bounded container resources, explicit network and filesystem policy, declared artifact export, and an integrity-verifiable receipt.

## Interface overview

`doctor`, `init`, `validate`, `inspect`, `run`, `verify`, ownership-scoped `clean`, `backends`, and `recover` form the Workcell 1.1 command surface. Docker and Podman provide the stable lifecycle; `inspect` resolves policy without starting a container.

## Portable backend preview

Workcell 1.1 includes alpha provider-neutral definitions, strict capability negotiation, portable receipts, ownership-bound recovery, and digest-pinned adapters for E2B, Vercel Sandbox, and Daytona. A workload can switch profiles without embedding provider configuration in its definition.

The portable contracts and remote adapters are not part of the stable guarantee. Offline conformance does not certify a live provider account, plan, region, control boundary, latency, cost, or cleanup behavior. Use the repository's live-certification procedure before promoting any adapter.

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

See the [Workcell repository](https://github.com/kujolang/workcell) and the [Workcell 1.1.0 release](https://github.com/kujolang/workcell/releases/tag/v1.1.0).
