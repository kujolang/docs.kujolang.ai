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
last_updated: 2026-08-23
scope: local-first
source_repo: runledger
previous: /tools/muzzle/
next: /tools/changebucket/
tags: [tool, evidence, receipts]
---


## Use it when…

You need a durable receipt for what ran, when it ran, what it used, and whether it passed.

## Interface overview

| Surface | What is available |
| --- | --- |
| Lifecycle | `start` and `finish` with task, status, verdict, and git metadata |
| Accounting | `usage`, `cost`, and notes attached to a run |
| Review | `list`, `show`, `compare`, and Markdown `report` |
| Follow-up | Structured follow-up items stored with `.runledger/` receipts |

## Main workflows

- Start a receipt before an agent or automation run and retain the returned run ID.
- Add usage, cost, or decision notes as evidence becomes available.
- Finish with an explicit pass, partial, or fail state and a concise verdict.
- Compare related runs or render a Markdown report for review and handoff.

## Five-minute example

```bash
runledger start --name quickstart-check
runledger finish <run-id> --status pass --verdict "checks passed"
runledger list
```

## What you get

Run metadata, token and cost notes, verdicts, comparison reports, and follow-ups.

## How it fits

Use it after [Eval](/tools/eval/) or [Dispatch](/tools/dispatch/) and alongside [CaseFile](/tools/casefile/).

## Boundaries

RunLedger records declared run information; it is not automatic billing capture or a hosted ledger.

## Reference

See the [RunLedger repository](https://github.com/kujolang/runledger).
