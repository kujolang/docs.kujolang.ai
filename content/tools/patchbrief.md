---
title: PatchBrief
description: Turn a diff into a reviewable summary and handoff.
template: docs
section: Tools
nav_title: PatchBrief
order: 180
audience: developer
difficulty: beginner
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: patchbrief
previous: /tools/changebucket/
next: /tools/concord/
tags: [tool, review, diff]
---


## Use it when…

The implementation is done and a reviewer needs the intent, changed files, risk, and test evidence in one compact brief.

## Interface overview

| Surface | What is available |
| --- | --- |
| Summary | `summarize` for intent, changed files, risk, and diff statistics |
| Tests | `suggest-tests` for evidence matched to the change |
| Handoff | `handoff` for an implementation-to-reviewer brief |
| Formats | Human-readable output or structured JSON with optional pretty printing |

## Main workflows

- Summarize the current diff before asking another person or agent to review it.
- Generate test suggestions, then record which checks actually ran rather than treating suggestions as proof.
- Produce a compact handoff after implementation and verification are complete.
- Use JSON output when another tool needs to consume the brief deterministically.

## Five-minute example

```bash
kujo run patchbrief.kujo -- summarize
kujo run patchbrief.kujo -- summarize --format json --pretty
```

## What you get

A structured diff summary, reviewer notes, changed-file risk, and a handoff artifact.

## How it fits

Add [ChangeBucket](/tools/changebucket/) for footprint and [Concord](/tools/concord/) for drift.

## Boundaries

This remains preview/dogfood wording until broader release proof is available.

## Reference

See the [PatchBrief repository](https://github.com/kujolang/patchbrief).
