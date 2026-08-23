---
title: Tests and evaluation
description: Run deterministic acceptance checks locally or in CI and keep the expected result explicit.
custom_url: tests-and-evaluation
template: docs
section: Keep work reviewable
nav_title: Tests and evaluation
order: 20
audience: developer
difficulty: intermediate
status: launch scope
version: current
last_updated: 2026-08-23
previous: /review/context-and-task-contracts/
next: /review/evidence-and-run-history/
tags: [eval, tests, acceptance]
---


Use repository tests for implementation behavior and [Eval](/tools/eval/) for deterministic acceptance checks around JSON, HTTP, files, or commands.

```bash
kujo run main.kujo run
kujo run eval.kujo report
```

An evaluation result is strongest when the fixture, check, expected output, and policy are all reviewable. Eval is not a general sandbox and should not be described as one.
