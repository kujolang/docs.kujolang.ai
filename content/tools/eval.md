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
last_updated: 2026-09-09
scope: local-first
source_repo: eval
previous: /tools/spec/
next: /tools/scout/
tags: [tool, evaluation, checks]
---


## Use it when…

You need explicit, deterministic checks around JSON, HTTP, files, commands, or a policy decision.

## Interface overview

| Surface | What is available |
| --- | --- |
| Suites | JSON suite files with JSON, HTTP, file, command, and policy checks |
| Execution | `run`, parallel workers, summary-only output, and output directories |
| Review | `report`, `compare`, snapshots, and HTML/JSON output |
| Integrity | `lint`, `list-checks`, `policy-explain`, and `verify-manifest` |

## Main workflows

- Define acceptance checks in a versioned suite and run them locally with deterministic fixtures.
- Write artifacts and checksums to a dedicated output directory for CI or review.
- Rerun a suite to produce an HTML report, or compare results against a prior snapshot.
- Verify the artifact manifest before treating a copied evidence directory as trustworthy.

## Five-minute example

```bash
kujo run main.kujo run examples/release_gate_suite.json --output-dir .eval-run --json
kujo run main.kujo report examples/release_gate_suite.json --rerun --output-dir .eval-run --format html
kujo run main.kujo verify-manifest --output-dir .eval-run --json
```

## What you get

Check results, policy explanations, snapshots, and a report suitable for local review or CI.

## How it fits

Run Eval after [Dispatch](/tools/dispatch/) or repository tests have produced a result.

## Boundaries

Eval is an acceptance-check runner, not a general sandbox.

## Reference

See the [Eval repository](https://github.com/kujolang/eval).

## Published release and current development

The latest published GitHub Release checked on September 9 is [v1.0.0](https://github.com/kujolang/eval/releases/tag/v1.0.0). Recent default-branch work correlates evaluation scores with Watchdog traces and corrects command-policy false positives. Evaluation receipts and live-provider qualification remain separate.

These newer changes are [source work at 7ad5caef1b71](https://github.com/kujolang/eval/tree/7ad5caef1b718ab8a6ccdd02ef1b645af93ac133); they are not retroactively included in the older release archive.
