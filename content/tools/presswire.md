---
title: PressWire
description: Execute approval-gated publication effects with idempotency and receipts.
template: docs
section: Tools
nav_title: PressWire
order: 320
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first publication gateway
source_repo: presswire
tags: [tool, publishing, approvals, receipts]
---

## Use it when…

A publication effect needs preflight checks, approval evidence, idempotency, resumable reconciliation, explicit compensation, corrections, and a durable receipt.

## Five-minute example

```bash
presswire init --state .presswire --json
presswire preflight --input fixtures/core.json --actor publisher --json
presswire validate --json
presswire export --output presswire-export.json --json
```

## What you get

Immutable publication records, append-only audit events, bounded effect state, receipts, correction evidence, and optional VersionSeal verification.

## Boundaries

CMS, Git-static, newsletter, and other delivery providers are optional adapters. PressWire does not claim hosted identity or distributed multi-host coordination.

## Reference

See the [PressWire repository](https://github.com/kujolang/presswire).
