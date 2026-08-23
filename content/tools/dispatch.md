---
title: Dispatch
description: Orchestrate resumable, approved, and auditable workflows.
template: docs
section: Tools
nav_title: Dispatch
order: 60
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: dispatch
previous: /tools/scout/
next: /tools/mcp/
tags: [tool, workflows, orchestration]
---


## Use it when…

A task is a sequence of steps that can pause, resume, require approval, and leave a run receipt.

## Interface overview

| Surface | What is available |
| --- | --- |
| Execute | `demo`, workflow templates, workflow files, JSON inputs, and tool allow/deny lists |
| Continue | `resume` and decision-file resume paths |
| Inspect | `runs`, `show`, `inspect`, JSON output, filtering, and diagnostics |
| Operate | `doctor`, guarded `cleanup`, `export-run`, and `import-run` |

## Main workflows

- Run a named or file-based workflow with explicit inputs, policy profile, and tool boundaries.
- Pause at approval or cancellation points and resume from persisted run state.
- Inspect lifecycle events and trace payloads without rerunning the workflow.
- Export a signed run bundle for handoff, then verify it when importing elsewhere.

## Five-minute example

```bash
kujo run dispatch.kujo demo "Research topic" --yes --non-interactive
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
