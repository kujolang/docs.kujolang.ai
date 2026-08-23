---
title: CRUD API Showcase
description: A SQLite API and frontend playground showing auth strategies, recovery patterns, and contracts.
template: docs
section: Showcases
nav_title: CRUD API Showcase
order: 20
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: crud-api
previous: /showcases/cms/
next: /showcases/ai-chat/
tags: [showcase, api, sqlite]
---


## Use it when…

You want a conventional API and frontend pattern with SQLite, explicit contracts, and recovery drills.

## Interface overview

| Surface | What is available |
| --- | --- |
| API | Item and project CRUD, filtering, pagination, search, sorting, and health metadata |
| Concurrency | `If-Unmodified-Since`, `428` preconditions, and `409` conflict responses |
| Frontend | Next.js playground for exercising the API and auth strategies |
| Operations | Structured request IDs/logs, smoke tests, backup/recovery, performance, lint, and build checks |

## Main workflows

- Start the Kujo API, then use the frontend or `curl` against `http://127.0.0.1:4100`.
- Create and query items or projects through explicit JSON contracts.
- Read an item’s `updated_at` value and send it with updates or deletes to avoid lost writes.
- Run API smoke tests and frontend lint/build checks before treating a change as complete.

## Five-minute example

```bash
kujo run main.kujo
npm run dev --prefix frontend
curl http://127.0.0.1:4100/health
```

## What you get

SQLite item/project APIs, auth strategies, a Next.js playground, smoke tests, and recovery/performance examples.

## How it fits

Use it as the application baseline before exploring [CMS](/showcases/cms/) or [AI Chat](/showcases/ai-chat/).

## Boundaries

The showcase is not a hosted API product; persistence, auth, and deployment proof are environment-specific.

## Reference

See the [CRUD API repository](https://github.com/kujolang/crud-api) for endpoint and data-shape contracts.
