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
last_updated: 2026-08-23
tags: [ecosystem, foundation]
---

The foundation contains four primary repositories:

- [Kujo](/tools/kujo/) — the language, VM-first runtime, CLI, standard library, and local project workflow.
- [Kennel](/tools/kennel/) — deterministic manifests, dependencies, lockfiles, source policy, and trust policy.
- [Workcell](/tools/workcell/) — bounded Docker or Podman execution with declared artifacts and integrity receipts.
- [Source](/tools/source/) — an agent-first collaboration platform built around Git, work, evidence, and bounded capabilities.

Kujo `v1.0.1` is published with platform binaries and checksums. Kennel and Workcell keep local and deployment boundaries explicit. Source is an MVP platform whose production storage and worker paths require deployment-specific validation.
