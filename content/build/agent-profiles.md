---
title: Choose an Agent Project Profile
description: Select the smallest Kujo Agent Project profile that matches the tools, knowledge, workflow, isolation, and observability you need.
custom_url: agent-profiles
template: docs
section: Build with Kujo
nav_title: Agent Profiles
order: 9
audience: developer
difficulty: beginner
status: stable
version: 1.1.0
last_updated: 2026-08-30
previous: /build/owned-agent-projects/
next: /build/agent-credentials/
tags: [ai, agents, profiles, integrations]
---

Start with the smallest profile that expresses the agent you intend to own. Every profile produces the same repository-owned contract and can be reviewed before anything is installed or run.

```bash
kujo agent new my-agent --profile basic --install
```

## Profiles

| Profile | Included capability | External requirement |
| --- | --- | --- |
| `basic` | Agents SDK fixture execution and Eval | None |
| `tools` | Project tools and MCP | Only the services your tools call |
| `knowledge` | Local RAG indexing, retrieval, and citations | None for local content |
| `workflow` | A runnable Dispatch workflow | None for the fixture path |
| `hardened` | Least-privilege declarations and Workcell | A supported container runtime for isolated runs |
| `observable` | Watchdog adapter configuration and RunLedger receipts | Watchdog only when you enable its proxy; RunLedger is installed with the profile |
| `full` | Compatible local composition, including Relay | Requirements of the capabilities you enable |

`--install` is an explicit convenience boundary. Without it, Kujo only writes the project. With it, Kujo asks Kennel to install the exact revisions in the generated manifest. Optional external services are reported by Inspect and Doctor; they are not silently treated as mandatory for unrelated commands.

## Inspect before running

```bash
cd my-agent
kujo agent inspect
kujo doctor agent
```

Inspect separates required dependencies, optional external services, credential names, policies, and integration paths. Doctor verifies the local toolchain and can add live probes with `--deep`.

## Understand integration ownership

The generated repository owns the configuration for each integration. Kujo does not hide a second hosted copy of the contract.

- [Agents SDK](/tools/agents-sdk/) owns agent execution primitives.
- [AI SDK](/tools/ai-sdk/) owns normalized provider requests.
- [MCP](/tools/mcp/) owns tool and resource interoperability.
- [RAG Starter Kit](/tools/rag-starter-kit/) owns local knowledge retrieval.
- [Dispatch](/tools/dispatch/) owns durable workflows.
- [Workcell](/tools/workcell/) owns the container isolation boundary.
- [Watchdog](/tools/watchdog/) and [RunLedger](/tools/runledger/) add optional telemetry and receipts.

Next, [configure credentials and connectors](/build/agent-credentials/) or [review operational controls](/build/agent-operations/).
