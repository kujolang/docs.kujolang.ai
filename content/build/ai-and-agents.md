---
title: AI and agents
description: Move from a normalized model call to tools, approvals, handoffs, and local state.
custom_url: ai-and-agents
template: docs
section: Build with Kujo
nav_title: AI and agents
order: 10
audience: developer
difficulty: intermediate
status: launch scope
version: current
last_updated: 2026-08-27
next: /tools/ai-sdk/
tags: [ai, agents, build]
---


Lead with increasing responsibility:

For a cross-cutting Kujo project, begin with the [`kujo-way-development`](/collections/skills/#start-with-the-kujo-way) skill so repository ownership, contracts, capability boundaries, deterministic execution, and completion evidence are decided before implementation.

1. [AI SDK](/tools/ai-sdk/) for normalized chat and embedding contracts.
2. [Agents SDK](/tools/agents-sdk/) for tools, approvals, handoffs, stores, and tracing.
3. [Dispatch](/tools/dispatch/) for resumable, auditable workflows.
4. [Watchdog](/tools/watchdog/) for local request, cost, latency, error, and audit visibility.

Begin with fixture mode when a provider is not part of the question you are trying to answer. Add live credentials only at the boundary where they are needed.
