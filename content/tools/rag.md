---
title: RAG
description: Build local retrieval flows with namespaces, citations, and offline fallbacks.
template: docs
section: Tools
nav_title: RAG
order: 80
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: rag
previous: /tools/mcp/
next: /tools/ai-sdk/
tags: [tool, retrieval, knowledge]
---


## Use it when…

You need to ingest local knowledge, isolate namespaces, retrieve relevant chunks, and return citations.

## Interface overview

| Surface | What is available |
| --- | --- |
| CLI | `ingest`, `query`, `serve`, `demo`, and `bootstrap` |
| Retrieval | Parser, chunking, embedding, namespace isolation, and citation metadata |
| Server | Local ingest/query HTTP endpoints with OpenAPI and SDK contract parity |
| Storage | Local indexes, maintenance utilities, and deterministic offline fixtures |

## Main workflows

- Ingest one file or a recursive directory into a named namespace.
- Query that namespace and inspect the chunks and citations used in the answer.
- Run the local server when an application needs HTTP ingestion and query boundaries.
- Bootstrap a reference repository or use demo mode to verify the full path without a hosted service.

## Five-minute example

```bash
kujo run main.kujo --interpreter ingest --path ./docs --recursive true --namespace team_a
kujo run main.kujo --interpreter query --question "How does this work?" --namespace team_a
```

## What you get

Local indexes, ingest/query/serve flows, namespace controls, citation metadata, and offline fixture behavior.

## How it fits

Start with [Knowledge and retrieval](/build/knowledge-and-retrieval/) and add [MCP](/tools/mcp/) only at the integration boundary.

## Boundaries

RAG is not a hosted retrieval service; parser, embedding, and deployment proof stay with the integrator.

## Reference

See the [RAG repository](https://github.com/kujolang/rag).
