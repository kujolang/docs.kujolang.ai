---
title: Dossier
description: Preserve claims, sources, evidence, quotations, consent, rights, and freshness.
template: docs
section: Tools
nav_title: Dossier
order: 295
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first evidence ledger
source_repo: dossier
tags: [tool, evidence, claims, editorial]
---

## Use it when…

Material claims need exact source identity, captured support, evidence classification, conflicts, quote approval, consent, rights, and freshness checks.

## Five-minute example

```bash
dossier init --state .dossier --json
dossier claim add --input fixtures/core.json --actor standards-editor --json
dossier report --limit 100 --json
dossier validate --json
```

## What you get

Immutable, checksum-bound records, bounded reports and packets, audit history, and portable exports.

## Boundaries

Dossier preserves assertions and evidence state; it does not create legal authority, grant rights, or turn an inference into a verified fact. Hosted providers are optional and outside the baseline.

## Reference

See the [Dossier repository](https://github.com/kujolang/dossier).
