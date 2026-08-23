---
title: BluePencil
description: Record structured editorial reviews, verdicts, disagreements, and calibration evidence.
template: docs
section: Tools
nav_title: BluePencil
order: 300
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first editorial review
source_repo: bluepencil
tags: [tool, editorial, review, quality]
---

## Use it when…

Editorial work needs an eight-dimension review, explicit findings and blockers, a bounded verdict, disagreement preservation, or blind reviewer calibration.

## Five-minute example

```bash
bluepencil init --json
bluepencil review --input fixtures/core.json --actor editorial-reviewer --json
bluepencil validate --json
bluepencil report --limit 100 --json
```

## What you get

Immutable reviews, comparisons, focused style/brand/claims/format/accessibility findings, calibration records, history, and portable exports.

## Boundaries

BluePencil operates under PROPOSE. It does not approve publication or rewrite source artifacts, and any blocking finding prevents a passing verdict.

## Reference

See the [BluePencil repository](https://github.com/kujolang/bluepencil).
