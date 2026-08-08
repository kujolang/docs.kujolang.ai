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
scope: local-first
source_repo: scout
previous: /tools/eval/
next: /tools/dispatch/
tags: [tool, context, repository]
---


## Use it when…

You need to understand a repository's files, entry points, contracts, dependencies, and risk before changing it.

## Five-minute example

```bash
kujo run scout.kujo --repo .
```

## What you get

A structured context map, file tree, intelligence summary, and optional security or dependency exports.

## How it fits

Pass only the useful parts to [Scent](/tools/scent/) before execution.

## Boundaries

Scout is repository intelligence, not an automatic implementation plan or security certification.

## Reference

See the [Scout repository](https://github.com/kujolang/scout).

