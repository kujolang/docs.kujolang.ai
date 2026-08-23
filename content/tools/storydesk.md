---
title: StoryDesk
description: Plan editorial work with immutable ideas, commissions, assignments, handoffs, and queues.
template: docs
section: Tools
nav_title: StoryDesk
order: 290
audience: all
difficulty: intermediate
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first editorial operations
source_repo: storydesk
tags: [tool, editorial, planning, workflow]
---

## Use it when…

An editorial operation needs a control desk for ideas, campaigns, commissions, assignment, status, blockers, handoffs, daily packets, and human review queues.

## Five-minute example

```bash
storydesk init --state .storydesk --json
storydesk idea add --input fixtures/core.json --actor commissioning-editor --json
storydesk idea list --limit 25 --json
storydesk validate --json
```

## What you get

Immutable local records, audit-oriented history, deterministic packets, review queues, and portable exports with optional signing.

## Boundaries

StoryDesk records editorial control state; identity, scheduling, and external systems remain adapter boundaries. Run the repository's production review for the actual deployment environment.

## Reference

See the [StoryDesk repository](https://github.com/kujolang/storydesk).
