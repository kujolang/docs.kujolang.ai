---
title: Repository-owned Agent Projects
description: Scaffold, inspect, run, evaluate, and harden an agent whose intelligence configuration lives in Git.
custom_url: owned-agent-projects
template: docs
section: Build with Kujo
nav_title: Owned Agent Projects
order: 8
audience: developer
difficulty: intermediate
status: local first release
version: current
last_updated: 2026-08-29
next: /tools/agents-sdk/
tags: [ai, agents, projects, build]
---

An Agent Project makes the agent a normal repository. Its definition,
instructions, model preference, project skills, tool declarations, knowledge,
policies, workflows, evaluation, dependency pins, and runtime boundaries remain
reviewable files rather than hidden hosted state.

## Create and prove the fixture path

```bash
kujo agent new research-assistant --profile basic
cd research-assistant
kennel install
kujo doctor agent --deep
kujo agent inspect
kujo agent run "Summarize the project contract"
kujo agent eval
```

The default fixture path uses Agents SDK and requires no provider credential or
provider network. `agent.project.json` is the versioned root contract. Kennel
installs exact ecosystem revisions recorded by the generated repository.

There is deliberately no `kujo agent doctor`. Agent diagnostics extend the
canonical Doctor architecture through `kujo doctor agent` and its established
JSON report format.

## Choose a profile

| Profile | Adds |
| --- | --- |
| `basic` | deterministic Agents SDK execution and Eval |
| `tools` | project tools and MCP |
| `knowledge` | local RAG indexing, retrieval, and citations |
| `workflow` | a runnable Dispatch workflow |
| `hardened` | least-privilege declarations and Workcell |
| `observable` | Watchdog adapter configuration and RunLedger receipts |
| `full` | the compatible local composition, including Relay |

Inspect output distinguishes required dependencies, optional external services,
credential names, policies, and generated integration paths. It does not make a
live provider request.

## Use a live provider

Provider ownership lives in `config/model.json`. OpenAI, OpenRouter, DeepSeek,
and custom OpenAI-compatible choices use AI SDK for the request and normalized
response, followed by Agents SDK execution.

```bash
kujo agent auth set openai
kujo agent new live-agent --install
cd live-agent
kujo agent run "Say hello"
```

The first command accepts hidden input and saves the key in macOS Keychain,
Windows Credential Manager, or Linux Secret Service. Every later OpenAI Agent
Project can reuse it. If a live provider is selected without a saved key,
interactive `agent new` offers the same masked setup instead of leaving a broken
project behind.

Kujo resolves credentials from the CI environment, an ignored owner-only project
`.env.local`, then the operating-system credential store. Use `kujo agent auth
set openai --project` only for a project-specific override. `auth status` reports
where a credential came from without revealing it; `auth remove` revokes it.
Non-interactive automation reads credentials from stdin rather than a command
argument or shell history.

API-key connectors use the same storage contract while their reviewed project
configuration retains only the expected variable name:

```bash
kujo agent auth set --name LINEAR_API_TOKEN
```

OAuth connectors should retain their scoped consent and refresh-token flow;
Kujo's API-key store is not a reason to replace OAuth with a long-lived token.
Custom endpoints require HTTPS unless a loopback URL is explicitly enabled for
local development.

## Harden execution

Kujo capability flags authorize effects; they are not a sandbox. The hardened
profile declares a separate Workcell container boundary with a read-only root,
no fixture network, resource limits, a bounded command, and a receipt:

```bash
kujo agent new isolated-agent --profile hardened
cd isolated-agent && kennel install
git add . && git commit -m "Initialize owned agent"
kujo agent run --workcell
```

Workcell depends on a supported local container runtime and a trusted host.

## Learn from working sources

- [Self-hosted Agent Project](https://github.com/kujolang/kujo/tree/main/examples/owned-agent-project)
- [Executable lifecycle workflow](https://github.com/kujolang/kujo-workflows/tree/main/owned-agent-project)
- [Kujo Agent Project implementation guide](https://github.com/kujolang/kujo/blob/main/docs/BUILD_AN_AGENT.md)
- [Agents SDK](/tools/agents-sdk/), [AI SDK](/tools/ai-sdk/), and [Kennel](/tools/kennel/)

This page is included in the public `llms.txt` index and the static WebMCP site
index. Those discovery surfaces expose documentation only; they do not grant
agent execution authority.
