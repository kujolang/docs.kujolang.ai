---
title: Scout
description: Build a structured map of an unfamiliar repository.
template: docs
section: Tools
nav_title: Scout
order: 50
audience: developer
difficulty: beginner
status: local scope verified
version: 1.1.0
last_updated: 2026-09-26
scope: local-first
source_repo: scout
previous: /tools/eval/
next: /tools/dispatch/
tags: [tool, context, repository]
---


## Use it when…

You need to understand a repository's files, entry points, contracts, dependencies, and risk before changing it.

## Interface overview

| Surface | What is available |
| --- | --- |
| Scan | Repository path, depth, quick mode, and output-directory controls |
| Focus | Skip dependency, route, or security analysis when it is outside the task |
| Security | Baseline suppression plus SARIF and JSONL exports |
| Boundaries | Rooted bounded reads, aggregate resource ceilings, strict partial-scan exits, and stable `SCOUT-LIMIT-*` identifiers |
| Artifacts | `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, and `scan_manifest.json` |

## Main workflows

- Run a quick scan for orientation or a bounded-depth scan for a focused subsystem.
- Generate durable repository context files for humans and downstream agents.
- Export security findings into machine-readable formats for existing review systems.
- Compare findings with a reviewed baseline while keeping suppressed items visible on demand.
- Use the versioned performance and labeled-corpus receipts as regression evidence in CI.

## Five-minute example

```bash
git clone --depth 1 --branch v1.1.0 https://github.com/kujolang/scout.git
cd scout
kujo run scout.kujo -- . --quick
kujo run scout.kujo -- ./src -o ./reports -d 3
```

Scout 1.1.0 requires Kujo 1.5.0 or newer.

## What you get

A structured context map, file tree, intelligence summary, scan manifest, and optional
SARIF, JSONL, Kennel, security, or dependency outputs. The 1.1.0 release also publishes
deterministic performance ceilings and exact-match evidence for 18 route families,
10 dependency-manifest families, and the security fixture corpus.

## How it fits

Pass only the useful parts to [Scent](/tools/scent/) before execution.

## Boundaries

Scout is repository intelligence, not an automatic implementation plan, complete static
analyzer, or security certification. Its quality metrics are corpus-scoped, and findings
and partial-scan diagnostics still require review.

## Reference

See the [Scout 1.1.0 release](https://github.com/kujolang/scout/releases/tag/v1.1.0)
and [repository](https://github.com/kujolang/scout).
