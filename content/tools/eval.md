---
title: Eval
description: Run deterministic acceptance checks locally or in CI.
template: docs
section: Tools
nav_title: Eval
order: 40
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: eval
previous: /tools/spec/
next: /tools/scout/
tags: [tool, evaluation, checks]
---


## Use it when…

You need explicit, deterministic checks around JSON, HTTP, files, commands, or a policy decision.

## Five-minute example

```bash
kujo run eval.kujo report
```

## What you get

Check results, policy explanations, snapshots, and a report suitable for local review or CI.

## How it fits

Run Eval after [Dispatch](/tools/dispatch/) or repository tests have produced a result.

## Boundaries

Eval is an acceptance-check runner, not a general sandbox.

## Reference

See the [Eval repository](https://github.com/kujolang/eval).

