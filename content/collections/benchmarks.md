---
title: Benchmarks
description: Benchmark methodology, fixtures, scorecards, and reproducibility limits.
template: docs
section: Collections
nav_title: Benchmarks
order: 40
audience: developer
difficulty: advanced
status: guidance
version: current
last_updated: 2026-08-23
scope: local-first
previous: /collections/agents/
next: /ecosystem/
tags: [collection, benchmarks, evaluation]
---


Benchmarks are only useful when the fixture, environment, scoring rule, and limitation are visible. Record the run and compare like with like.

```bash
runledger start --name benchmark-run
```

Benchmark scores are evidence for the measured setup, not universal performance claims.

There is currently no dedicated `kujolang/kujo-benchmarks` repository. Benchmark fixtures live with the tools and workflow kits they measure; keep the originating repository and commit in every receipt.
