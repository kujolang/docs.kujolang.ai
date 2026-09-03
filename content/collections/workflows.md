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
last_updated: 2026-09-02
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

The collection is the locally verified [`0.4.0` release](https://github.com/kujolang/kujo-workflows/releases/tag/v0.4.0), with 38 workflow kits. Kits have individual Ready, Limited, or Experimental labels; hosted runners and blanket production readiness are not claimed. Use [Dispatch](/tools/dispatch/) for resumable workflow primitives and [RunLedger](/tools/runledger/) for a run receipt.

The [Publishing House Operator](/build/publishing-house-operator/) released in `0.4.0` composes the eleven editorial workflow kits into a lease-protected daily control loop while preserving StoryDesk, VersionSeal, PressWire, and the other tools' separate authority. The release also adds the source-backed [Owned Agent Project workflow](https://github.com/kujolang/kujo-workflows/tree/v0.4.0/owned-agent-project).

See the [Kujo Workflows repository](https://github.com/kujolang/kujo-workflows).
