---
title: AI SDK
description: Use normalized chat and embedding contracts with fixtures, retries, and redaction.
template: docs
section: Tools
nav_title: AI SDK
order: 30
audience: developer
difficulty: intermediate
status: launch scope
version: current
scope: local-first
source_repo: ai-sdk
next: /tools/agents-sdk/
tags: [tool, ai, providers]
---

# AI SDK

## Use it when…

You need a provider-gated chat or embedding call with a normalized contract and a fixture path for local checks.

## Five-minute example

```bash
kujo run main.kujo --interpreter fixture
```

## What you get

Normalized response and embedding shapes, retry/backoff behavior, redaction, and an offline fixture mode.

## How it fits

Move to [Agents SDK](/tools/agents-sdk/) when calls need tools, approvals, handoffs, or stores.

## Boundaries

Provider-specific proof and credentials remain integrator-owned; this is not a hosted model gateway.

## Reference

See the [AI SDK repository](https://github.com/kujolang/ai-sdk) and the [AI runtime basics](/learn/ai-runtime/) guide.

