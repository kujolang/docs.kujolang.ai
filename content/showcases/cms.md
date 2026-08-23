---
title: CMS
description: A server-first content system with models, delivery routes, auth boundaries, jobs, and operational checks.
template: docs
section: Showcases
nav_title: CMS
order: 10
audience: developer
difficulty: advanced
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: cms
previous: /tools/
next: /showcases/crud-api/
tags: [showcase, cms, content]
---


## Use it when…

You want to see a server-first content application with explicit content models and delivery boundaries.

## Interface overview

| Surface | What is available |
| --- | --- |
| Runtime | `backend/runtime/main.kujo`; no separate CMS CLI wrapper |
| Content API | Types, taxonomies, entries, media, menus, plugins, themes, tenants, and workspaces |
| Discovery | `/health`, `/v1`, `/v1/contract`, `/v1/openapi.json`, feeds, sitemap, robots, and `llms.txt` |
| Operations | Auth-gated writes, rate limits, idempotency, jobs, webhooks, migrations, backup, and restore |

## Main workflows

- Start the API on its default local boundary and inspect the contract or OpenAPI route.
- Model content and deliver only published entries anonymously; protect drafts and mutations with bearer auth.
- Process webhook and background-job outboxes, including dead-letter replay.
- Run contract, startup, security, integration, and release-gate checks before deployment.

## Five-minute example

```bash
kujo run backend/runtime/main.kujo
curl http://127.0.0.1:4200/v1/openapi.json
```

## What you get

Content models, delivery routes, auth boundaries, background jobs, migrations, and operational checks.

## How it fits

Compare with [CRUD API](/showcases/crud-api/) for a smaller API pattern and [SSG](/showcases/ssg/) for deterministic publishing.

## Boundaries

This is a local showcase. Hosted operations, identity, backups, and deployment require separate proof.

## Reference

See the [CMS repository](https://github.com/kujolang/cms) for route contracts and operational scripts.
