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
version: 1.2.2
last_updated: 2026-10-21
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
| Connected Sources | Exact evidence-backed inbound producer inventory, registration metadata, local verification, and safe named proxy-profile management |
| Operations | SQLite storage, token auth, host policy, redaction, rate limits, and retention controls |

## Main workflows

- Start the local dashboard server and point an OpenAI-compatible client at its proxy base URL.
- Inspect requests through the dashboard or JSON APIs without changing the application contract.
- Use Connected Sources to distinguish configured and observed inbound producers from outbound exporter destinations without fabricating connectivity or health.
- Create, edit, disable, or delete named proxy profiles; validated changes apply to new requests without restarting Watchdog, while historical telemetry remains intact.
- Enable API and proxy tokens before exposing the server beyond a trusted local boundary.
- Treat displayed cost as a versioned direct-provider estimate, not an invoice.

## Five-minute example

```bash
WDG_HOST=127.0.0.1 kujo run --interpreter dashboard_server.kujo
curl http://127.0.0.1:7700/api/proxy-config
```

## What you get

Local telemetry, canonical evidence, redacted request records, dashboard views, Connected Sources inventory, and proxy configuration.

## How it fits

Put it beside [AI SDK](/tools/ai-sdk/) or [Dispatch](/tools/dispatch/) when a workflow needs visibility.

## Boundaries

Watchdog is not a managed observability service; credentials and deployment remain integrator-owned.

## Reference

See the [Watchdog repository](https://github.com/kujolang/watchdog).

## Published release

[Watchdog v1.2.2](https://github.com/kujolang/watchdog/releases/tag/v1.2.2) fixes gateway credential forwarding, sensitive metadata handling, OTLP retries and delivery queue limits. It reduces canonical intake work, client cloning and backup memory use. Provider and OpenRouter pricing catalogs are refreshed; displayed costs remain estimates.

Existing routes and schema versions remain compatible. Invalid typed telemetry now returns an error, and changed OTLP records with an existing identity return 409. Keep API, gateway and provider credentials separate. Copy `config/proxy.example.json` when creating a local proxy configuration.

Use Kujo 1.6.0 or newer. Runtime measurement references and RunLedger correlation remain observational: they do not authorize execution or replay and do not prove business effects. Operators still own authentication, retention and deployment. Use an independent edge limiter when you need abuse protection; Watchdog's per-session buckets trust caller-supplied identity headers.

### Retained 1.1 behavior

[Watchdog v1.1.0](https://github.com/kujolang/watchdog/releases/tag/v1.1.0), published September 26, adds canonical v2 telemetry intake and correlation, lossless JSONL/OTLP projections, and the authenticated Connected Sources panel. Source status remains derived only from configuration or accepted local telemetry. Inbound producers stay separate from outbound exporter destinations, source registration metadata remains secret-free, and deleting a registration never deletes historical telemetry.

Named proxy-profile creates, updates, disables, and deletes apply to new requests without a process restart; in-flight requests retain their starting snapshot. Disabled and deleted profiles fail closed before egress. SDK and workflow integrations still need compatible pinned revisions, and operator authentication, retention, exporter credentials, and deployment policy remain required.

## Agent City

[Agent City](/showcases/agent-city/) uses Watchdog telemetry to show observed agent work and source health in a pixel-art city.
