---
title: Tribunal
description: Produce an advisory decision receipt for a review gate.
template: docs
section: Tools
nav_title: Tribunal
order: 280
audience: developer
difficulty: advanced
status: preview; advisory and unsigned
version: current
scope: local-first
source_repo: tribunal
next: /tools/workcell/
tags: [tool, review, decisions]
---

# Tribunal

## Use it when…

A review gate needs a structured, explainable recommendation and a receipt that can be attached to a handoff.

## Five-minute example

```bash
kujo run tribunal.kujo decide --input evidence.json
```

## What you get

An advisory decision receipt with inputs, rule results, and rationale.

## How it fits

Feed it evidence from [Eval](/tools/eval/), [CaseFile](/tools/casefile/), or [RunLedger](/tools/runledger/).

## Boundaries

The receipt is advisory and unsigned. It is not a legal, security, or enterprise approval.

## Reference

See the [Tribunal repository](https://github.com/kujolang/tribunal).

