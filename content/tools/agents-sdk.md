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
version: current
last_updated: 2026-09-09
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

## Five-minute example

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

## Published release and current development

The latest published GitHub Release checked on September 9 is [v1.0.0](https://github.com/kujolang/agents-sdk/releases/tag/v1.0.0). Recent default-branch work adds bounded run, retrieval, tool, and handoff observations, preserves observed identities, and demonstrates real MCP tool lifecycles. Programming-language retrieval preferences are optional; provider execution and telemetry policy remain explicit integration boundaries.

These newer changes are [source work at bb2202d8b54f](https://github.com/kujolang/agents-sdk/tree/bb2202d8b54f44717b1b1f0157a6774f2027cea1); they are not retroactively included in the older release archive.
