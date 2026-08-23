---
title: ContentGraph
description: Build an inspectable graph of content relationships, clusters, gaps, and link opportunities.
template: docs
section: Tools
nav_title: ContentGraph
order: 280
audience: developer
difficulty: advanced
status: local scope verified
version: current
last_updated: 2026-08-23
scope: read-only content intelligence
source_repo: contentgraph
tags: [tool, content, graph, web]
---

## Use it when…

Content needs deterministic relationship analysis across local source, SiteProbe runs, sitemaps, CSV/CMS exports, or SearchBridge evidence.

## Five-minute example

```bash
./contentgraph build --source ./content --out .contentgraph/baseline
./contentgraph orphans .contentgraph/baseline
./contentgraph link-opportunities .contentgraph/baseline
./contentgraph export .contentgraph/baseline --format graphml --out graph.graphml
```

## What you get

Versioned graph data, node and relationship inspection, clusters, overlaps, orphan findings, explainable link proposals, comparisons, and JSON, GraphML, or SARIF export.

## Boundaries

ContentGraph never edits input content. Source discovery rejects symlink escapes, ignores generated/dependency directories, and bounds nodes, queries, explanations, and exports.

## Reference

See the [ContentGraph repository](https://github.com/kujolang/contentgraph).
