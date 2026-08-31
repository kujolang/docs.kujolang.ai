---
title: Manage Agent Credentials and Connectors
description: Store reusable provider keys safely, configure project overrides, and connect Kujo Agent Projects without putting secrets in commands or Git.
custom_url: agent-credentials
template: docs
section: Build with Kujo
nav_title: Agent Credentials
order: 10
audience: developer
difficulty: intermediate
status: stable
version: 1.1.0
last_updated: 2026-08-30
previous: /build/agent-profiles/
next: /build/agent-operations/
tags: [ai, agents, credentials, connectors, security]
---

Kujo stores reusable provider keys in macOS Keychain, Windows Credential Manager, or Linux Secret Service. The project keeps only credential names and ignored local overrides, so secrets do not become part of the agent contract.

## Save a provider key once

```bash
kujo agent auth set openai
kujo agent auth status openai
```

`auth set` accepts masked interactive input. Built-in provider names include OpenAI, OpenRouter, and DeepSeek. A later Agent Project using the same provider can reuse the saved key.

```bash
kujo agent new live-agent --provider openai --model gpt-5 --install
cd live-agent
kujo agent run "Say hello"
```

If an interactive scaffold selects a live provider without a saved key, Kujo offers the same masked setup before leaving the project behind.

## Use safe automation inputs

Pass secrets through stdin or an existing environment variable, never a command argument that can land in shell history or process listings.

```bash
printf '%s' "$OPENAI_API_KEY" | kujo agent auth set openai --from-stdin
kujo agent auth set openai --from-env OPENAI_API_KEY
kujo agent new ci-agent --credential-stdin --install
```

Use `--no-credential` when scaffolding should remain offline or credentials will be supplied later.

## Choose credential scope

Kujo resolves credentials in this order:

| Priority | Source |
| --- | --- |
| 1 | Current process environment |
| 2 | Owner-only, Git-ignored project `.env.local` |
| 3 | Operating-system credential store |

Use `kujo agent auth set openai --project` for a project-specific override. `auth status` reports the source without revealing the value. Revoke a saved credential with `kujo agent auth remove openai`.

## Add API-key connectors

Named connector credentials use the same storage contract:

```bash
kujo agent auth set --name LINEAR_API_TOKEN
kujo agent auth status --name LINEAR_API_TOKEN
```

Keep OAuth connectors on their scoped consent and refresh-token flow. The API-key store does not turn OAuth into a long-lived token. Custom OpenAI-compatible provider endpoints require HTTPS unless a loopback URL is explicitly enabled for local development.

Kujo never prints the stored secret in status, Inspect, Doctor, or JSON output.
Continue with [agent operations and hardening](/build/agent-operations/).
