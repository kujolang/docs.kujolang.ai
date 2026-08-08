---
title: RunLedger
description: Record run metadata, usage, cost, verdicts, and follow-ups.
template: docs
section: Tools
nav_title: RunLedger
order: 160
audience: developer
difficulty: beginner
status: local scope verified
version: current
scope: local-first
source_repo: runledger
previous: /tools/muzzle/
next: /tools/changebucket/
tags: [tool, evidence, receipts]
---


## Use it when…

You need a durable receipt for what ran, when it ran, what it used, and whether it passed.

## Five-minute example

```bash
runledger start --name quickstart-check
runledger finish --verdict pass
runledger show latest
```

## What you get

Run metadata, token and cost notes, verdicts, comparison reports, and follow-ups.

## How it fits

Use it after [Eval](/tools/eval/) or [Dispatch](/tools/dispatch/) and alongside [CaseFile](/tools/casefile/).

## Boundaries

RunLedger records declared run information; it is not automatic billing capture or a hosted ledger.

## Reference

See the [RunLedger repository](https://github.com/kujolang/runledger).

