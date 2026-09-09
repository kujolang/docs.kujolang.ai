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
version: 0.6.0
last_updated: 2026-09-09
scope: local-first
source_repo: kujo-workflows
previous: /collections/video-skills/
next: /collections/agents/
tags: [collection, workflows, receipts]
---


Workflows connect a task contract to execution and evidence. Each pack should say what it consumes, what it runs, and where the receipt lives.

```bash
(cd loop-engineering && bash scripts/run-workflow.sh --demo)
```

The collection is the [`0.6.0` release](https://github.com/kujolang/kujo-workflows/releases/tag/v0.6.0), with 44 local workflows. Kits have individual Ready, Limited, or Experimental labels; hosted runners and blanket production readiness are not claimed. Use [Dispatch](/tools/dispatch/) for resumable workflow primitives and [RunLedger](/tools/runledger/) for a run receipt.

The [Publishing House Operator](/build/publishing-house-operator/) released in `0.4.0` composes the eleven editorial workflow kits into a lease-protected daily control loop while preserving StoryDesk, VersionSeal, PressWire, and the other tools' separate authority. The release also adds the source-backed [Owned Agent Project workflow](https://github.com/kujolang/kujo-workflows/tree/v0.4.0/owned-agent-project).

See the [Kujo Workflows repository](https://github.com/kujolang/kujo-workflows).

## VideoOps production workflows

The current collection includes the production initializer and five stages: creative planning, asset resolution, media generation, HyperFrames editing, and independent quality review. [Browse all six VideoOps workflows](https://github.com/kujolang/kujo-workflows/tree/v0.6.0/docs/videoops). Shared production media tools and schemas live in [Kujo Agents 1.4.0](https://github.com/kujolang/kujo-agents/releases/tag/v1.4.0); the [135 skills in Kujo Skills 0.7.0](/collections/skills/) provide agent guidance.

Fixture mode is distinct from provider execution. The release's rootful Colima gate passed with AppArmor and seccomp; synthetic rootless identity checks do not establish live rootless certification. ElevenLabs TTS passed in the companion runtime, while Sound Effects authorization and Free-plan music remained blocked. No publication or account upgrade is implied.
