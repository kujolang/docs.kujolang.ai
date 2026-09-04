---
title: Workcell
description: Run bounded Kujo and agent workflows in disposable Docker or Podman workspaces.
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

Workcell validates an execution definition, prepares a disposable Git workspace, runs the workload through Docker or Podman, exports declared artifacts, records evidence, and removes resources it owns.

The main commands are `doctor`, `init`, `validate`, `inspect`, `run`, `verify`, `clean`, `backends`, and `recover`. Use `inspect` to resolve policy without starting a container.

## Portable backends

Provider-neutral definitions let a workload switch host profiles without embedding provider configuration. Before provisioning, Workcell compares the workload's requirements with the backend's capabilities. The receipt then records which controls were accepted, enforced, observed, unsupported, or unknown.

Docker and Podman provide the supported execution path. Adapters for E2B, Vercel Sandbox, and Daytona are previews. Offline conformance checks their protocol behavior but does not certify a live provider account, plan, region, security boundary, latency, cost, or cleanup path. Run the repository's live-certification procedure before production use.

## Five-minute example

```bash
./bin/workcell init
./bin/workcell validate --file workcell.json
./bin/workcell inspect --file workcell.json --json
./bin/workcell run --file workcell.json --repo . --no-pull
```

## Evidence and recovery

Each run writes evidence under `.workcell/runs/<run-id>/`. The run directory separates the receipt, integrity manifest, logs, changes, exported artifacts, verification result, and cleanup outcome. `workcell verify` checks sealed evidence offline, while `recover` reconciles interrupted external resources by ownership.

## Boundaries

Workcell does not protect against a compromised daemon or host kernel, provide microVM or hosted multi-tenant isolation, or certify deployment-specific egress and image policy. Run `workcell doctor` on each target host.

## Reference

See the [Workcell repository](https://github.com/kujolang/workcell) for installation, examples, contract references, provider operations, and current releases.
