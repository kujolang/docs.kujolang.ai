---
title: ReaderSignal
description: Record privacy-bounded audience measurements, feedback, comparisons, and learning.
template: docs
section: Tools
nav_title: ReaderSignal
order: 325
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first measurement
source_repo: readersignal
tags: [tool, analytics, privacy, learning]
---

## Use it when…

Audience learning needs immutable measurement snapshots, feedback, privacy policy, deletion receipts, uncertainty-aware comparisons, and evidence links.

## Five-minute example

```bash
readersignal init --state .readersignal --json
readersignal snapshot --input fixtures/core.json --actor analyst --json
readersignal validate --json
readersignal export --output readersignal-export.json --json
```

## What you get

Bounded snapshots, feedback and comparison records, audit history, privacy-policy evidence, optional PressWire verification, and portable exports.

## Boundaries

ReaderSignal does not claim causal attribution, hosted identity, or distributed multi-host coordination. External measurement providers remain optional adapters.

## Reference

See the [ReaderSignal repository](https://github.com/kujolang/readersignal).
