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
version: 1.3.0
last_updated: 2026-09-29
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

## Dispatch 1.3.0

[Dispatch 1.3.0](https://github.com/kujolang/dispatch/releases/tag/v1.3.0)
requires Kujo 1.6.0 and uses released AI SDK and Agents SDK dependencies. It adds
process-owned run locks, durable review checkpoints, failure-control decisions,
restart-safe continuation, retrieval preferences and bounded evidence inspection.
Stop older workers before upgrading and retain a backup; do not mix locking or
protected-state formats across versions. Follow the repository's
[upgrade guidance](https://github.com/kujolang/dispatch/blob/v1.3.0/docs/UPGRADING_TO_1_3.md).

`resume-decision` preserves configured tool authorization. An approval applies to
its reviewed step, not every later gate; concurrent delivery cannot create another
permission. Dispatch remains the sole replay/admission authority.

### Experimental companion contracts

Wave C beta assurance remains opt-in in the bounded single-effect required/deny
domain; alpha compatibility remains. SQLite, Workcell Git CAS and Ability supply
live effect verification. Wave D alpha handoffs correlate participant and result
references without granting replay permission. Participant SDKs remain alpha and
unpublished under the trusted-local-host model. Effect-set diagnostics are
read-only; they do not permit multi-effect replay.

No exactly-once effect guarantee, universal rollback, general machine-loss
recovery, remote participant authentication or stable participant SDK is claimed.
Source-blind agent adoption is technical evidence; human usability validation
remains separate. See the
[release notes](https://github.com/kujolang/dispatch/blob/v1.3.0/docs/RELEASE_1_3_0.md).
