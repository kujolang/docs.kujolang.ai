---
title: Dispatch
description: Orchestrate resumable, approved, and auditable workflows.
template: docs
section: Tools
nav_title: Dispatch
order: 70
audience: developer
difficulty: intermediate
status: launch scope
version: current
scope: local-first
source_repo: dispatch
next: /tools/watchdog/
tags: [tool, workflows, orchestration]
---

# Dispatch

## Use it when…

A task is a sequence of steps that can pause, resume, require approval, and leave a run receipt.

## Five-minute example

```bash
kujo run dispatch.kujo demo
kujo run dispatch.kujo runs
```

## What you get

Resumable workflow state, step events, approval boundaries, and an inspectable run record.

## How it fits

Start with [Spec](/tools/spec/) and capture the result with [RunLedger](/tools/runledger/).

## Boundaries

Live integrations need separate proof; local workflow orchestration is the documented scope.

## Reference

See the [Dispatch repository](https://github.com/kujolang/dispatch).

