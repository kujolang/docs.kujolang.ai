---
title: Spec
description: Turn a request into a structured, checkable task contract.
template: docs
section: Tools
nav_title: Spec
order: 30
audience: developer
difficulty: beginner
status: local scope verified
version: current
scope: local-first
source_repo: spec
previous: /tools/kennel/
next: /tools/eval/
tags: [tool, contracts, tasks]
---


## Use it when…

The request is too open-ended to evaluate safely and needs an objective, constraints, acceptance checks, and completion state.

## Five-minute example

```bash
kujo run spec.kujo validate task.spec.yml
```

## What you get

A structured task contract that can be handed to an agent or workflow and checked after the run.

## How it fits

Use [Scout](/tools/scout/) and [Scent](/tools/scent/) to focus the context before execution.

## Boundaries

Spec defines work; it does not itself run untrusted code or prove that an implementation is correct.

## Reference

See the [Spec repository](https://github.com/kujolang/spec).

