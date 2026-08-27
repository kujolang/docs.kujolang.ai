---
title: Workflows and approvals
description: Turn a sequence of steps into bounded, resumable, and auditable work.
custom_url: workflows-and-approvals
template: docs
section: Build with Kujo
nav_title: Workflows and approvals
order: 20
audience: developer
difficulty: intermediate
status: launch scope
version: current
last_updated: 2026-08-27
previous: /build/ai-and-agents/
next: /tools/spec/
tags: [workflows, approvals, dispatch]
---


Define the request with [Spec](/tools/spec/), focus context with [Scent](/tools/scent/), prepare execution with [PackWrite](/tools/packwrite/), then use [Dispatch](/tools/dispatch/) for resumable steps and approvals.

```bash
kujo run dispatch.kujo demo
```

Leave the workflow receipt beside the run. It should be possible to see what was requested, what was allowed, what ran, and what remains.
