---
title: Knowledge and retrieval
description: Ingest local knowledge and answer with namespaces, citations, and offline fallbacks.
custom_url: knowledge-and-retrieval
template: docs
section: Build with Kujo
nav_title: Knowledge and retrieval
order: 30
audience: developer
difficulty: intermediate
status: launch scope
version: current
previous: /build/workflows-and-approvals/
next: /tools/rag/
tags: [knowledge, rag, citations]
---

# Knowledge and retrieval

Use [RAG](/tools/rag/) when a workflow needs local ingestion, namespace isolation, citations, or offline fixture behavior. Keep the source documents, parser choices, chunking strategy, and retrieval result visible.

```bash
kujo run main.kujo --interpreter demo
```

The local-first boundary matters: this is a retrieval starter, not a hosted search service. Provider or deployment choices belong to the integrator.

