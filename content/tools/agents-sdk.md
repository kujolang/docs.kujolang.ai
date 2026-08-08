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
kujo test
```

## What you get

Agent runner primitives, tool contracts, approval events, handoff receipts, and local stores.

## How it fits

Pair it with [Spec](/tools/spec/) for a bounded task and [Dispatch](/tools/dispatch/) for resumable orchestration.

## Boundaries

Hosted adapters remain integrator-owned. Use fixture mode when proving the workflow shape.

## Reference

See the [Agents SDK repository](https://github.com/kujolang/agents-sdk).
