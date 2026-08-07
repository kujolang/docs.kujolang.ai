---
title: RAG
description: Build local retrieval flows with namespaces, citations, and offline fallbacks.
template: docs
section: Tools
nav_title: RAG
order: 100
audience: developer
difficulty: intermediate
status: launch scope
version: current
scope: local-first
source_repo: rag
next: /tools/kujo-doctor/
tags: [tool, retrieval, knowledge]
---

# RAG

## Use it when…

You need to ingest local knowledge, isolate namespaces, retrieve relevant chunks, and return citations.

## Five-minute example

```bash
kujo run main.kujo --interpreter demo
```

## What you get

Local indexes, ingest/query/serve flows, namespace controls, citation metadata, and offline fixture behavior.

## How it fits

Start with [Knowledge and retrieval](/build/knowledge-and-retrieval/) and add [MCP](/tools/mcp/) only at the integration boundary.

## Boundaries

RAG is not a hosted retrieval service; parser, embedding, and deployment proof stay with the integrator.

## Reference

See the [RAG repository](https://github.com/kujolang/rag).

