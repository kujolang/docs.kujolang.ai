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
version: current
last_updated: 2026-08-27
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
| Artifacts | `FILE_TREE.md`, `llms.txt`, `AGENTS.md`, `CHECKLIST.md`, `intelligence.json`, and `scan_manifest.json` |

## Main workflows

- Run a quick scan for orientation or a bounded-depth scan for a focused subsystem.
- Generate durable repository context files for humans and downstream agents.
- Export security findings into machine-readable formats for existing review systems.
- Compare findings with a reviewed baseline while keeping suppressed items visible on demand.

## Five-minute example

```bash
kujo run scout.kujo -- . --quick
kujo run scout.kujo -- ./src -o ./reports -d 3
```

## What you get

A structured context map, file tree, intelligence summary, and optional security or dependency exports.

## How it fits

Pass only the useful parts to [Scent](/tools/scent/) before execution.

## Boundaries

Scout is repository intelligence, not an automatic implementation plan or security certification.

## Reference

See the [Scout repository](https://github.com/kujolang/scout).
