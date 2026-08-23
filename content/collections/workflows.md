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
last_updated: 2026-08-23
scope: local-first
source_repo: kujo-workflows
previous: /collections/skills/
next: /collections/agents/
tags: [collection, workflows, receipts]
---


Workflows connect a task contract to execution and evidence. Each pack should say what it consumes, what it runs, and where the receipt lives.

```bash
(cd loop-engineering && bash scripts/run-workflow.sh --demo)
```

The collection is a locally verified `0.3.0` technical preview. Kits have individual Ready, Limited, or Experimental labels; hosted runners and blanket production readiness are not claimed. Use [Dispatch](/tools/dispatch/) for resumable workflow primitives and [RunLedger](/tools/runledger/) for a run receipt.

See the [Kujo Workflows repository](https://github.com/kujolang/kujo-workflows).
