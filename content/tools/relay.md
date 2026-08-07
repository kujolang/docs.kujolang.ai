---
title: Relay
description: Persist and hand off workflow state with integrity-checked receipts.
template: docs
section: Tools
nav_title: Relay
order: 270
audience: developer
difficulty: advanced
status: preview; local persistence scope
version: current
scope: local-first
source_repo: relay
next: /tools/tribunal/
tags: [tool, workflows, handoff]
---

# Relay

## Use it when…

A workflow must pause, resume, or move between workers without losing its state or receipt.

## Five-minute example

```bash
kujo run relay.kujo demo
```

## What you get

Persisted workflow state, integrity checks, and a handoff receipt.

## How it fits

Use after [Dispatch](/tools/dispatch/) and before an advisory gate such as [Tribunal](/tools/tribunal/).

## Boundaries

Preview/local persistence scope; do not imply a hosted workflow service.

## Reference

See the [Relay repository](https://github.com/kujolang/relay).

