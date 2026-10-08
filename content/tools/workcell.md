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
version: 1.2.0
last_updated: 2026-09-29
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

## Version 1.2.0 and Kujo 1.6

Workcell 1.2.0 requires Kujo 1.6.0 and adds bounded preservation, portable execution results, conservative re-execution descriptors and expiry-gated owned cleanup. The Git CAS assurance profile and controlled process participant are experimental; Dispatch decides replay. Stable Docker/Podman scope and remote-adapter alpha boundaries remain unchanged.

See the [1.2.0 release](https://github.com/kujolang/workcell/releases/tag/v1.2.0) for the exact source and release evidence. Assurance beta remains opt-in, required/deny and single-effect; controlled handoffs remain alpha. These package releases do not stabilize remote trust or participant SDKs.

## Agent City

[Agent City](/showcases/agent-city/) can show permitted Workcell execution and returned artifacts. Its installer guide explains container requirements.
