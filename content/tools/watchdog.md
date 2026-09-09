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
last_updated: 2026-09-09
scope: local-first
source_repo: watchdog
previous: /tools/fence/
next: /tools/leash/
tags: [tool, telemetry, ai]
---


## Use it when…

You need a local proxy or dashboard to understand AI request volume, cost, latency, errors, and audit records.

## Interface overview

| Surface | What is available |
| --- | --- |
| Proxy | OpenAI-compatible requests under `/proxy/v1` with passthrough or override auth |
| APIs | `/api/requests`, `/api/proxy-config`, health, readiness, and structured exports |
| Dashboard | Request, tool, agent-step, latency, token, cost-estimate, and failure views |
| Operations | SQLite storage, token auth, host policy, redaction, rate limits, and retention controls |

## Main workflows

- Start the local dashboard server and point an OpenAI-compatible client at its proxy base URL.
- Inspect requests through the dashboard or JSON APIs without changing the application contract.
- Enable API and proxy tokens before exposing the server beyond a trusted local boundary.
- Treat displayed cost as a versioned direct-provider estimate, not an invoice.

## Five-minute example

```bash
WDG_HOST=127.0.0.1 kujo run --interpreter dashboard_server.kujo
curl http://127.0.0.1:7700/api/proxy-config
```

## What you get

Local telemetry, redacted request records, dashboard views, and proxy configuration.

## How it fits

Put it beside [AI SDK](/tools/ai-sdk/) or [Dispatch](/tools/dispatch/) when a workflow needs visibility.

## Boundaries

Watchdog is not a managed observability service; credentials and deployment remain integrator-owned.

## Reference

See the [Watchdog repository](https://github.com/kujolang/watchdog).

## Published release and current development

The latest published GitHub Release checked on September 9 is [v1.0.1](https://github.com/kujolang/watchdog/releases/tag/v1.0.1). Recent default-branch work adds canonical v2 telemetry intake and cross-system correlation, rejects partial invalid batches before privacy filtering, and reuses validated canonical bytes and hashes. The v2 contract is distinct from the 1.0.1 product release. SDK and workflow integrations must use compatible pinned revisions; operator authentication, retention, exporter credentials, and deployment policy remain required.

These newer changes are [source work at 314698b0502c](https://github.com/kujolang/watchdog/tree/314698b0502c5d2139df46b7523482c6d089b6ff); they are not retroactively included in the older release archive.
