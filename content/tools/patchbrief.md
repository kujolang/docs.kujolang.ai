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
scope: local-first
source_repo: patchbrief
previous: /tools/changebucket/
next: /tools/concord/
tags: [tool, review, diff]
---


## Use it when…

The implementation is done and a reviewer needs the intent, changed files, risk, and test evidence in one compact brief.

## Five-minute example

```bash
kujo run patchbrief.kujo summarize --base main --head HEAD
```

## What you get

A structured diff summary, reviewer notes, changed-file risk, and a handoff artifact.

## How it fits

Add [ChangeBucket](/tools/changebucket/) for footprint and [Concord](/tools/concord/) for drift.

## Boundaries

This remains preview/dogfood wording until broader release proof is available.

## Reference

See the [PatchBrief repository](https://github.com/kujolang/patchbrief).

