---
title: AssetWorks
description: Plan media assets and preserve provenance, accessibility records, and checksums.
template: docs
section: Tools
nav_title: AssetWorks
order: 310
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first media operations
source_repo: assetworks
tags: [tool, media, provenance, accessibility]
---

## Use it when…

Media work needs an immutable plan, provenance, captions or accessibility artifacts, deterministic probes, and checksum-backed validation.

## Five-minute example

```bash
assetworks init --state .assetworks --json
assetworks plan --input fixtures/core.json --actor producer --json
assetworks validate --json
assetworks export --output assetworks-export.json --json
```

## What you get

Immutable records, append-only audit events, deterministic media evidence, optional signed manifests, and portable exports.

## Boundaries

FFmpeg, image tooling, hosted storage, and external services are optional adapters. AssetWorks does not claim hosted identity or distributed multi-host coordination.

## Reference

See the [AssetWorks repository](https://github.com/kujolang/assetworks).
