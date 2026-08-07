---
title: AI runtime basics
description: See the shared controls for provider calls, replay, budgets, secrets, and egress.
custom_url: ai-runtime
template: docs
section: Learn Kujo
nav_title: AI runtime
order: 60
audience: developer
difficulty: intermediate
status: launch scope
version: current
previous: /learn/editor-support/
next: /build/ai-and-agents/
tags: [ai, runtime, budgets, secrets]
---

# AI runtime basics

The AI runtime story is about controlled calls rather than a single provider: normalize the contract, bound spend and time, keep secrets out of source, and make replay or fixture mode possible.

Start with the [AI SDK](/tools/ai-sdk/) for provider-gated chat or embeddings, then move to [Agents SDK](/tools/agents-sdk/) when tools, approvals, handoffs, or state enter the design.

## Boundary

Provider-specific credentials and hosted adapters remain integrator-owned. The local examples are useful for proving workflow shape, not for claiming a managed AI platform.

