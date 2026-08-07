---
title: CaseFile
description: Capture a failure as a reproducible evidence bundle.
template: docs
section: Tools
nav_title: CaseFile
order: 160
audience: developer
difficulty: beginner
status: launch scope
version: current
scope: local-first
source_repo: casefile
next: /tools/runledger/
tags: [tool, evidence, failures]
---

# CaseFile

## Use it when…

A local failure needs to be handed to another person with enough context to reproduce it without leaking secrets.

## Five-minute example

```bash
casefile capture --from-log build.log
casefile show latest
```

## What you get

A redacted failure bundle with commands, environment facts, logs, and reproduction notes.

## How it fits

Pair it with [RunLedger](/tools/runledger/) for run metadata and [Redact](/tools/redact/) for sensitive input policy.

## Boundaries

Capture only scoped, reviewable evidence; never store credentials or unrelated private data.

## Reference

See the [CaseFile repository](https://github.com/kujolang/casefile).

