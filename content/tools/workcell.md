---
title: Workcell
description: Execute a bounded local package with completion evidence.
template: docs
section: Tools
nav_title: Workcell
order: 290
audience: developer
difficulty: advanced
status: preview; trusted Docker or Podman boundary
version: current
scope: local-first
source_repo: workcell
next: /tools/stego-cipher/
tags: [tool, execution, containers]
---

# Workcell

## Use it when…

A package needs a bounded local execution boundary and a completion receipt.

## Five-minute example

```bash
workcell run --file workcell.json --repo . --no-pull
workcell verify --run .workcell/runs/<run-id> --json
```

## What you get

An execution run, completion evidence, and verification output.

## How it fits

Use after [PackWrite](/tools/packwrite/) when a repeatable package needs an execution gate.

## Boundaries

This is a trusted Docker/Podman local boundary; preview wording remains visible.

## Reference

See the [Workcell repository](https://github.com/kujolang/workcell).

