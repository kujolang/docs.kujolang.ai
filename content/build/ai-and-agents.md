---
title: AI and agents
description: Move from a repository-owned agent or normalized model call to tools, approvals, handoffs, and local state.
custom_url: ai-and-agents
template: docs
section: Build with Kujo
nav_title: AI and agents
order: 10
audience: developer
difficulty: intermediate
status: stable agent path
version: 1.1.0
last_updated: 2026-08-30
next: /build/owned-agent-projects/
tags: [ai, agents, build]
---


Start with the ownership boundary that matches the job.

For an agent that should live in Git, use Kujo's Agent Development Platform:

```bash
curl -fsSL https://kujolang.ai/install.sh | bash -s -- --group agent
kujo agent new my-agent --profile basic --install
```

The basic profile is offline and deterministic. Continue through [Agent
Projects](/build/owned-agent-projects/), then select a
[profile](/build/agent-profiles/), add [credentials](/build/agent-credentials/)
only if a live provider is required, and use the [operations
guide](/build/agent-operations/) for diagnostics, evaluation, and isolation.

For custom application code, add responsibility in layers:

For a cross-cutting Kujo project, begin with the [`kujo-way-development`](/collections/skills/#start-with-the-kujo-way) skill so repository ownership, contracts, capability boundaries, deterministic execution, and completion evidence are decided before implementation.

1. [AI SDK](/tools/ai-sdk/) for normalized chat and embedding contracts.
2. [Agents SDK](/tools/agents-sdk/) for tools, approvals, handoffs, stores, and tracing.
3. [Dispatch](/tools/dispatch/) for resumable, auditable workflows.
4. [Watchdog](/tools/watchdog/) for local request, cost, latency, error, and audit visibility.

Choose a package from the [provider index](/ecosystem/providers/) when a live model is part of the question. Begin with fixture mode when it is not. Add live credentials only at the boundary where they are needed.
