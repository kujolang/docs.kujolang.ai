---
title: AI SDK
description: Use normalized chat and embedding contracts with fixtures, retries, and redaction.
template: docs
section: Tools
nav_title: AI SDK
order: 90
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: ai-sdk
previous: /tools/rag/
next: /tools/agents-sdk/
tags: [tool, ai, providers]
---


## Use it when…

You need a provider-gated chat or embedding call with a normalized contract and a fixture path for local checks.

## Interface overview

| Surface | What is available |
| --- | --- |
| Library | `create_client`, `create_message`, chat completion, streaming, and embeddings |
| Providers | Provider packages with public AI SDK drivers, plus custom OpenAI-compatible endpoints |
| Reliability | Retries, backoff, timeouts, fallback providers, circuit breakers, and budgets |
| Safety and proof | Endpoint allowlists, protected headers, redaction, fixtures, schemas, and benchmarks |

## Main workflows

- Import `src/ai_sdk.kujo` and `src/providers.kujo`; this library does not add a separate user-facing CLI.
- Run the bundled example with no key to exercise deterministic fixture mode.
- Add a provider preset or custom endpoint while keeping the application response contract unchanged.
- Stream normalized `delta`, `done`, and `error` events, or request embeddings through the same client boundary.

## Five-minute example

```bash
kujo run examples/main.kujo
```

## What you get

Normalized response and embedding shapes, retry/backoff behavior, redaction, and an offline fixture mode.

## How it fits

Move to [Agents SDK](/tools/agents-sdk/) when calls need tools, approvals, handoffs, or stores.

## Boundaries

Provider-specific proof and credentials remain integrator-owned; this is not a hosted model gateway. See the [provider index](/ecosystem/providers/) for package versions, native APIs, authentication variables, and driver availability.

## Reference

See the [AI SDK repository](https://github.com/kujolang/ai-sdk) and the [AI runtime basics](/learn/ai-runtime/) guide.
