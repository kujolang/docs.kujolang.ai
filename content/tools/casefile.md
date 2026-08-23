---
title: CaseFile
description: Capture a failure as a reproducible evidence bundle.
template: docs
section: Tools
nav_title: CaseFile
order: 220
audience: developer
difficulty: beginner
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: casefile
previous: /tools/packwrite/
next: /tools/lens/
tags: [tool, evidence, failures]
---


## Use it when…

A local failure needs to be handed to another person with enough context to reproduce it without leaking secrets.

## Interface overview

| Surface | What is available |
| --- | --- |
| Capture | A failed command, `--from-log`, or `--manual` evidence |
| Review | `list`, `show latest`, structured case JSON, Markdown, and reproduction notes |
| Operations | `doctor`, cleanup, output scoping, and optional `--mirror-exit-code` |
| Safety | Repository-bound paths, argument/log/note redaction, and bounded capture size |

## Main workflows

- Wrap a failing command so CaseFile records its output, exit code, duration, and environment context.
- Import an existing log when rerunning the failure is unsafe or expensive.
- Create a manual case for failures that cannot be represented by one command.
- Review the redacted bundle before sharing it and mirror the captured exit code when CI must preserve failure status.

## Five-minute example

```bash
kujo run casefile.kujo --interpreter -- capture --from-log build.log
kujo run casefile.kujo --interpreter -- list
kujo run casefile.kujo --interpreter -- show latest
```

## What you get

A redacted failure bundle with commands, environment facts, logs, and reproduction notes.

## How it fits

Pair it with [RunLedger](/tools/runledger/) for run metadata and [Scent](/tools/scent/) for bounded context policy.

## Boundaries

Capture only scoped, reviewable evidence; never store credentials or unrelated private data.

## Reference

See the [CaseFile repository](https://github.com/kujolang/casefile).
