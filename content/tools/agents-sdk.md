---
title: Agents SDK
description: Build agents with tools, approvals, handoffs, tracing, stores, and budgets.
template: docs
section: Tools
nav_title: Agents SDK
order: 100
audience: developer
difficulty: intermediate
status: local scope verified
version: 1.1.3
last_updated: 2026-10-13
scope: local-first
source_repo: agents-sdk
previous: /tools/ai-sdk/
next: /tools/scent/
tags: [tool, agents, approvals]
---


## Use it when…

An AI call needs tools, approval boundaries, handoffs, tracing, session state, or explicit budgets.

## Interface overview

| Surface | What is available |
| --- | --- |
| Runtime | Agent configuration, runners, lifecycle events, cancellation, and bounded retries |
| Tools and safety | Typed tool registry, permissions, approvals, guardrails, and redaction hooks |
| State | Session, memory, artifact, and retrieval store contracts with in-memory fixtures |
| Coordination | Handoffs, tracing, budgets, MCP helpers, and integration adapters |

## Main workflows

- Import the modules under `src/agents/`; there is no separate end-user CLI.
- Build an agent around injected AI SDK callbacks so provider concerns stay outside the runtime.
- Register tools with schemas and risk metadata, then enforce approval before invocation.
- Persist sessions, memory, artifacts, traces, and handoff receipts through replaceable store interfaces.

## Install

Use Kujo 1.6.0 or newer and Kennel 1.1.0 or newer:

```bash
kennel add agents-sdk@1.1.3
kennel install
```

The package pins Ability 1.0.1 to an exact Git commit, so installation requires Git
and GitHub access. Model calls use host callbacks; offline examples need no provider
credentials.

## Five-minute example

From the Agents SDK source checkout with dependencies installed:

```bash
kujo run examples/examples_smoke_runner.kujo --interpreter
bash scripts/ci_no_network_enforcement.sh
```

## What you get

Agent runner primitives, tool contracts, approval events, handoff receipts, and local stores.

## How it fits

Pair it with [Spec](/tools/spec/) for a bounded task and [Dispatch](/tools/dispatch/) for resumable orchestration.

## Boundaries

Hosted adapters remain integrator-owned. Use fixture mode when proving the workflow shape.

## Reference

See the [Agents SDK repository](https://github.com/kujolang/agents-sdk).

## Portable operation contracts

Use [Ability](/tools/ability/) to preserve an operation’s identity, schemas, effects, and retry semantics across application and agent surfaces. Its SDK previews and fixture development kit help check contracts; the application retains execution authority.

## Version 1.1.3

[Agents SDK 1.1.3](https://github.com/kujolang/agents-sdk/releases/tag/v1.1.3),
released October 13, hardens approval and handoff boundaries, runtime limits,
resume-state recovery, and session deletion. Automatic storage IDs cannot replace
existing records. Retrieval and tool artifacts retain source whitespace, and
malformed RAG citation IDs produce structured errors.

Model retries use a loop instead of growing the call stack. Run token budgets
include reported usage from failed retries, rejected structured output, and
failed streams. The final model response retains its own usage. Memory, artifact,
and trace queries materialize only the requested page.

Public API signatures and result shapes remain unchanged. Corrected validation
can reject runs that previously passed through a bug. Preserved whitespace can
increase artifact byte counts, and complete token accounting can trigger a
budget limit sooner. Trim source content only when that is intended.

Verification covers 277 contract cases, 42 fixtures, module exports, examples,
and context regression gates on Kujo 1.6.0. Offline checks do not prove live-provider
or deployment readiness.

## Operational limits

Budgets, timeouts, and cancellation use cooperative lifecycle checks. Callbacks
must enforce per-attempt deadlines and cancellation. Missing usage is not estimated.
Cost telemetry uses `cost_cents`, while the generic budget counter uses
`cost_microunits`; automatic conversion is undefined. Use host/provider cost
limits until that contract is defined.

Controlled Ability handoffs remain experimental alpha. Dispatch owns review and
replay admission. Application identity, approvals, credentials, file roots,
retention, and multiwriter coordination remain host responsibilities.

See the [release notes](https://github.com/kujolang/agents-sdk/blob/v1.1.3/docs/RELEASE_NOTES.md)
and [security guide](https://github.com/kujolang/agents-sdk/blob/v1.1.3/docs/SECURITY_PRODUCTION_GUIDE.md).
