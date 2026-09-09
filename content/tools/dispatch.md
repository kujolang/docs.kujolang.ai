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
last_updated: 2026-09-09
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
| Route | Deterministic agent/provider/model selection with policy constraints, evaluation, and bounded fallback |

## Main workflows

- Run a named or file-based workflow with explicit inputs, policy profile, and tool boundaries.
- Pause at approval or cancellation points and resume from persisted run state.
- Inspect lifecycle events and trace payloads without rerunning the workflow.
- Export a signed run bundle for handoff, then verify it when importing elsewhere.
- Validate and explain a routed workflow before execution; persisted route decisions and fallback evidence remain inspectable on resume.

## Five-minute example

```bash
kujo run dispatch.kujo demo "Research topic" --yes --non-interactive
kujo run dispatch.kujo runs
```

## What you get

Resumable workflow state, step events, approval boundaries, route decisions, and an inspectable run record.

## How it fits

Start with [Spec](/tools/spec/) and capture the result with [RunLedger](/tools/runledger/).

## Boundaries

Live integrations need separate proof; local workflow orchestration is the documented scope.

## Reference

See the [Dispatch repository](https://github.com/kujolang/dispatch).

## Published release and current development

The latest published GitHub Release checked on September 9 is [v1.2.0](https://github.com/kujolang/dispatch/releases/tag/v1.2.0). Recent default-branch work persists task retrieval preferences, adds a RAG documentation plugin and a real Agents SDK/RAG handler example, and exposes bounded task/retry observations with source attempt identity. These additions do not turn fixture coverage into proof for every live provider.

These newer changes are [source work at dcffd8f8c3fb](https://github.com/kujolang/dispatch/tree/dcffd8f8c3fb9bac1e66bc5a0ad6a5d078c88019); they are not retroactively included in the older release archive.
