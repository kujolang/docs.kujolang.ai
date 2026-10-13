---
title: AI SDK
description: Use normalized chat and embedding contracts with fixtures, retries, and redaction.
template: docs
section: Tools
nav_title: AI SDK
order: 90
audience: developer
difficulty: intermediate
status: release documented
version: 1.2.0
last_updated: 2026-10-13
scope: local-first
source_repo: ai-sdk
previous: /tools/rag/
next: /tools/agents-sdk/
tags: [tool, ai, providers]
---


## Use it when

You need chat or embedding calls with a shared response contract, retries, redaction, usage accounting, and offline fixtures.

## Install

AI SDK 1.2.0 requires Kujo 1.6.0 or newer and Kennel 1.1.0 or newer:

```bash
kennel add ai-sdk@1.2.0
kennel install
```

Import `src/ai_sdk.kujo` and `src/providers.kujo`. AI SDK is a library; it has no separate CLI. In a checkout, run `kujo run examples/main.kujo` to try fixtures without a provider key.

## What 1.2.0 changes

- Client copies share persistent process-local counters. Inspect them with `client_state`; use the documented reset APIs for cleanup.
- Completed provider usage remains charged when a budget or structured-output check rejects a result. Structured-output retries recheck budgets.
- Optional `governance_mode: "strict"` holds backend ownership through a request and its accounting. `atomic_memory_backend()` supplies process-local ownership and quarantine after uncertain writes.
- Fallback entry options cannot bypass strict mode or atomic-backend validation.
- Native downloads enforce response limits while reading. Endpoint allowlists disable redirects.

## Streaming and compatibility

Existing provider dictionaries, native driver hooks, two-argument custom transports, and normalized `delta`, `done`, and `error` callbacks keep their contracts. Response, provider-driver, and model-catalog versions remain 1.0.0.

The optional `on_transport_chunk` callback delivers transport text as it arrives. It requires a runtime with `http_stream_collect`; published Kujo 1.5.0 and 1.6.0 reject the option before I/O. Existing buffered streaming works on those releases. The release notes identify tested source backports; installing AI SDK does not replace your runtime.

## Accounting boundaries

Best-effort accounting remains the default. Strict mode rejects provider fallback and requires a shared backend with acquire/get/set/release hooks. The built-in backend is process-local. Distributed budgets require durable state and fenced ownership. Reconcile uncertain usage before clearing quarantine; do not reset it automatically on retries.

A completed request may exceed its remaining budget and is charged before rejection. SDK accounting is not a provider-side hard spending cap.

## Verification

The full local release gate passes 185 Kujo tests on both published 1.5.0 and 1.6.0, plus wrapper, HTTP, schema, example, documentation, and benchmark checks. The declared minimum remains 1.6.0. The release notes record live-provider evidence separately; offline fixtures do not certify a deployment.

## Related tools

Use [Agents SDK](/tools/agents-sdk/) when calls need tools, approvals, handoffs, or stores. See the [provider index](/ecosystem/providers/) for native APIs, authentication variables, and driver availability.

## Reference

- [AI SDK 1.2.0 release](https://github.com/kujolang/ai-sdk/releases/tag/v1.2.0)
- [Release notes and runtime requirements](https://github.com/kujolang/ai-sdk/blob/v1.2.0/docs/RELEASE_1_2_0.md)
- [AI runtime basics](/learn/ai-runtime/)

## License

MIT
