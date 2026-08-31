---
title: Core / Foundation
description: The Kujo runtime, package, execution, and collaboration foundation.
template: docs
section: Ecosystem
nav_title: Core / Foundation
order: 10
audience: all
difficulty: beginner
status: local scope verified
version: current
last_updated: 2026-08-30
tags: [ecosystem, foundation]
---

The foundation contains four primary repositories:

- [Kujo](/tools/kujo/) — the language, VM-first runtime, CLI, standard library, and local project workflow.
- [Kennel](/tools/kennel/) — deterministic manifests, dependencies, lockfiles, source policy, and trust policy.
- [Workcell](/tools/workcell/) — bounded Docker or Podman execution with declared artifacts and integrity receipts.
- [Source](/tools/source/) — an agent-first collaboration platform built around Git, work, evidence, and bounded capabilities.

Kujo `v1.1.0` is published with platform binaries and checksums. Its Agent Development Platform composes explicit Kennel, Agents SDK, AI SDK, MCP, RAG, Dispatch, Eval, Workcell, Watchdog, RunLedger, and Relay boundaries without folding those tools into opaque hosted state. Kennel and Workcell keep local and deployment boundaries explicit. Source is an MVP platform whose production storage and worker paths require deployment-specific validation.
