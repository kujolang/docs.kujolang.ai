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

## Five-minute example

```bash
changebucket check --base main --head HEAD --markdown
```

## What you get

File-category counts, change budgets, risk, and blast-radius reports in JSON or Markdown.

## How it fits

Use after [PatchBrief](/tools/patchbrief/) and before [ShipCheck](/tools/shipcheck/).

## Boundaries

Footprint is a decision aid, not a substitute for tests, review, or architecture analysis.

## Reference

See the [ChangeBucket repository](https://github.com/kujolang/changebucket).

