---
title: GalleyPack
description: Bind editorial artifacts into versioned, checksum-backed production packages.
template: docs
section: Tools
nav_title: GalleyPack
order: 305
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first package control
source_repo: galleypack
tags: [tool, editorial, packaging, checksums]
---

## Use it when…

Editorial artifacts need exact file binding, lineage, upstream evidence and review references, package freezing, comparison, and drift detection.

## Five-minute example

```bash
galleypack init --json
galleypack add --input fixtures/core.json --path article.md --actor production-editor --json
galleypack freeze --input package.json --path manifest.json --actor production-editor --json
galleypack validate --id package-example-v1 --json
```

## What you get

Immutable artifact and package records, manifests, hashes, lineage, comparisons, reports, history, and exports.

## Boundaries

GalleyPack fails closed on unsafe paths, symlinks, malformed or incompatible records, duplicate IDs, unsafe overwrite, and byte drift. It packages evidence; it does not publish it.

## Reference

See the [GalleyPack repository](https://github.com/kujolang/galleypack).
