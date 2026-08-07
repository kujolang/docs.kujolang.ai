---
title: Security and network examples
description: Authorized-use examples with inert fixtures and explicit safety boundaries.
template: docs
section: Showcases
nav_title: Security and network examples
order: 60
audience: developer
difficulty: advanced
status: showcase / controlled fixtures
version: current
scope: local-first
source_repo: kujo/showcases
next: /collections/skills/
tags: [showcase, security, network]
---

# Security and network examples

## Use it when…

You need to study a boundary pattern using authorized, inert fixtures rather than live targets.

## Five-minute example

```bash
kujo run examples/inert-network.kujo --interpreter fixture
```

## What you get

An explicit capability request, fixture-backed result, and a safety boundary that can be reviewed.

## How it fits

Read the [security model](/security/) and [MCP](/tools/mcp/) before adapting an integration.

## Boundaries

Authorized use only. Never treat these fixtures as permission to probe third-party systems.

