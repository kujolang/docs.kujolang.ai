---
title: Intake
description: Normalize inbound requests, route them for review, and preserve an audit trail.
template: docs
section: Tools
nav_title: Intake
order: 260
audience: developer
difficulty: intermediate
status: preview; integration evidence required
version: current
scope: local-first
source_repo: intake
next: /tools/relay/
tags: [tool, requests, approvals]
---

# Intake

## Use it when…

Inbound requests need normalization, routing, approvals, and an auditable history before work begins.

## Five-minute example

```bash
kujo run main.kujo demo
```

## What you get

A normalized request, routing decision, approval state, and audit record.

## How it fits

Start with [Spec](/tools/spec/) when the request is ready to become bounded work.

## Boundaries

Intake remains preview and local-first; external integration proof is separate.

## Reference

See the [Intake repository](https://github.com/kujolang/intake).

