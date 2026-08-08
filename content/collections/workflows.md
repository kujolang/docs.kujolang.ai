---
title: Workflows
description: Browse runnable workflow packs and the artifact each workflow leaves behind.
template: docs
section: Collections
nav_title: Workflows
order: 20
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: kujo-workflows
previous: /collections/skills/
next: /collections/agents/
tags: [collection, workflows, receipts]
---


Workflows connect a task contract to execution and evidence. Each pack should say what it consumes, what it runs, and where the receipt lives.

```bash
kujo run workflow.kujo demo
```

Use [Dispatch](/tools/dispatch/) for resumable workflow primitives and [RunLedger](/tools/runledger/) for a run receipt.

