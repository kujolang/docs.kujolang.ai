---
title: Watchdog
description: Observe AI requests, tools, costs, latency, errors, and audit events.
template: docs
section: Tools
nav_title: Watchdog
order: 130
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: watchdog
previous: /tools/fence/
next: /tools/leash/
tags: [tool, telemetry, ai]
---


## Use it when…

You need a local proxy or dashboard to understand AI request volume, cost, latency, errors, and audit records.

## Five-minute example

```bash
kujo run dashboard_server.kujo
curl http://127.0.0.1:8787/api/requests
```

## What you get

Local telemetry, redacted request records, dashboard views, and proxy configuration.

## How it fits

Put it beside [AI SDK](/tools/ai-sdk/) or [Dispatch](/tools/dispatch/) when a workflow needs visibility.

## Boundaries

Watchdog is not a managed observability service; credentials and deployment remain integrator-owned.

## Reference

See the [Watchdog repository](https://github.com/kujolang/watchdog).

