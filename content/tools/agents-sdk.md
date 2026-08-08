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

## Five-minute example

```bash
kujo run examples/approval-agent.kujo --interpreter fixture
```

## What you get

Agent runner primitives, tool contracts, approval events, handoff receipts, and local stores.

## How it fits

Pair it with [Spec](/tools/spec/) for a bounded task and [Dispatch](/tools/dispatch/) for resumable orchestration.

## Boundaries

Hosted adapters remain integrator-owned. Use fixture mode when proving the workflow shape.

## Reference

See the [Agents SDK repository](https://github.com/kujolang/agents-sdk).

