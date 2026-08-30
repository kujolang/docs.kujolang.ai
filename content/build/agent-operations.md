---
title: Operate and Harden Agent Projects
description: Diagnose, inspect, run, evaluate, automate, and isolate a repository-owned Kujo Agent Project.
custom_url: agent-operations
template: docs
section: Build with Kujo
nav_title: Agent Operations
order: 11
audience: developer
difficulty: intermediate
status: stable
version: 1.1.0
last_updated: 2026-08-30
previous: /build/agent-credentials/
next: /build/review-and-ship/
tags: [ai, agents, operations, evaluation, security]
---

Kujo gives the Agent Project one local lifecycle for people and automation.

| Task | Command |
| --- | --- |
| Diagnose the installed platform | `kujo doctor agent` |
| Describe the resolved contract | `kujo agent inspect` |
| Execute an agent | `kujo agent run "Your prompt"` |
| Run the project evaluation | `kujo agent eval` |

Add `--json` to any of these commands for versioned machine output. Commands
return a nonzero status when a required dependency, policy, evaluation, or run
fails, so CI does not have to parse human prose.

## Diagnose without spending model tokens

```bash
kujo doctor agent
kujo agent inspect --json
```

The default diagnostic validates local dependencies and configuration without a
provider request. `kujo doctor agent --deep` adds the live probes declared by
the project.

## Run prompts and prompt files

```bash
kujo agent run "Summarize the project contract"
kujo agent run --file prompts/release-review.md
```

The fixture path remains deterministic. A live provider run uses the configured
model and the credential resolution rules described in
[Agent Credentials](/build/agent-credentials/).

## Isolate effects with Workcell

Capability declarations authorize effects; they are not a sandbox. The
`hardened` profile adds a separate Workcell container boundary with a read-only
root, bounded command, resource limits, fixture-network denial, and a receipt.

```bash
kujo agent new isolated-agent --profile hardened --install
cd isolated-agent
git add . && git commit -m "Initialize owned agent"
kujo agent run --workcell
```

Workcell requires a supported local container runtime and a trusted host. Kujo
fails closed when a referenced path escapes the project, a credential is
missing, a required dependency is absent, or a declared security boundary
cannot be established.

## Make the run reviewable

Use Eval for repeatable acceptance checks, RunLedger for local run receipts,
and Watchdog only when you want its telemetry proxy. The `basic` profile does
not require either observability tool.

Return to [Agent Projects](/build/owned-agent-projects/) or explore the
[Agents showcase](https://agents.kujolang.ai/).
