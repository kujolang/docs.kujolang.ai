---
title: Relay
description: Compose and run bounded agent missions with lifecycle control and verifiable evidence.
template: docs
section: Tools
nav_title: Relay
order: 127
audience: developer
difficulty: advanced
status: stable v1 local scope
version: current
last_updated: 2026-08-23
scope: local and operator-controlled
source_repo: relay
tags: [tool, agents, missions, orchestration]
---

## Use it when…

An agent mission needs fixture or Watchdog-routed chat, policy-bound tools, an existing repository or isolated worktree, pause/resume controls, and integrity-checked evidence.

## Five-minute example

```bash
./bin/relay doctor --json
./bin/relay agents validate --json
./bin/relay chat "Summarize the mission boundary" --fixture --json
./bin/relay missions run examples/fixture-mission.json --fixture --json
```

## What you get

Mission state, tool and policy evidence, run listings, verification, and portable run exports.

## Boundaries

Relay is not hosted orchestration, multi-tenant identity, unrestricted shell access, or universal provider certification. Live requests must route through Watchdog; write missions require explicit policy approval.

## Reference

See the [Relay repository](https://github.com/kujolang/relay).
