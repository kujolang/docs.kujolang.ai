---
title: Editorial publishing
description: Move a commissioned idea through evidence, review, packaging, approval, publication, and learning.
custom_url: editorial-publishing
template: docs
section: Build with Kujo
nav_title: Editorial publishing
order: 60
audience: all
difficulty: advanced
status: production-capable control plane
version: current
last_updated: 2026-09-02
tags: [editorial, publishing, evidence, approvals]
---

The publishing-house tools keep ownership and evidence separate:

1. [StoryDesk](/tools/storydesk/) owns ideas, campaigns, commissions, assignments, handoffs, and queues.
2. [Dossier](/tools/dossier/) owns claims, sources, evidence, quotes, consent, rights, and freshness.
3. [AssetWorks](/tools/assetworks/) owns media plans, provenance, and accessibility artifacts.
4. [BluePencil](/tools/bluepencil/) owns independent review, blockers, verdicts, and calibration.
5. [GalleyPack](/tools/galleypack/) binds exact files, lineage, review evidence, and frozen package versions.
6. [VersionSeal](/tools/versionseal/) binds approval and authority to the exact checksummed version.
7. [PressWire](/tools/presswire/) owns bounded publication effects, reconciliation, corrections, and receipts.
8. [ReaderSignal](/tools/readersignal/) owns privacy-bounded measurements and evidence-linked learning.

The [Publishing House Operator](/build/publishing-house-operator/) is the durable control loop above these tools and the eleven workflow kits. It reads StoryDesk, delegates resumable execution to Dispatch, invokes bounded workers through an explicit phase-adapter boundary, validates checksum-bound receipts, records checkpoints, routes exact-version approval, and lets PressWire own publication effects. Publication profiles currently cover the personal blog, `kujolang.ai`, `docs.kujolang.ai`, and `agents.kujolang.ai` without forking the agent roles.

The control plane supports live execution and deterministic rehearsal. A production installation configures its model and retrieval phase adapter, authenticated PressWire provider for any authorized Git effect, and enabled ReaderSignal or WebOps measurement credentials. Missing deployment capabilities block only the affected work. No tool silently grants authority held by another stage, and no fixture result is presented as a live publication effect.
