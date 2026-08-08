---
title: ChangeBucket
description: Measure change footprint, categories, and blast radius.
template: docs
section: Tools
nav_title: ChangeBucket
order: 170
audience: developer
difficulty: beginner
status: local scope verified
version: current
scope: local-first
source_repo: changebucket
previous: /tools/runledger/
next: /tools/patchbrief/
tags: [tool, review, blast-radius]
---


## Use it when…

You need a compact measure of how much changed and which parts of the repository are affected.

## Interface overview

| Surface | What is available |
| --- | --- |
| Revision scope | `--base`, `--head`, and `--repo` |
| Reports | Terminal summary plus `--json`, `--markdown`, and `--output` |
| Budgets | `check` with maximum files, churn, and related thresholds |
| Analysis | File categories, risk signals, and blast-radius summaries |

## Main workflows

- Compare a base and head revision to establish the review footprint.
- Export JSON for automation or Markdown for a pull request and handoff.
- Enforce explicit budgets with `changebucket check`; a breach exits non-zero.
- Use the result to focus review, then rely on tests and architecture checks for correctness.

## Five-minute example

```bash
changebucket --base main --head HEAD --markdown
changebucket check --max-files 20 --max-churn 800
```

## What you get

File-category counts, change budgets, risk, and blast-radius reports in JSON or Markdown.

## How it fits

Use after [PatchBrief](/tools/patchbrief/) and before [ShipCheck](/tools/shipcheck/).

## Boundaries

Footprint is a decision aid, not a substitute for tests, review, or architecture analysis.

## Reference

See the [ChangeBucket repository](https://github.com/kujolang/changebucket).
