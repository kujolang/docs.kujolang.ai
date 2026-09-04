---
title: Source
description: Coordinate agent-first software work, evidence, decisions, and canonical Git state.
template: docs
section: Tools
nav_title: Source
order: 27
audience: developer
difficulty: advanced
status: MVP
version: current
last_updated: 2026-08-23
scope: local evaluation and deployment integration
source_repo: source
tags: [tool, git, collaboration, agents]
---

## Use it when…

A project needs work, sessions, changes, evidence, decisions, bounded agent capabilities, and canonical Git state represented in one inspectable system.

## Interface overview

Source includes a CLI, HTTP API, management UI, smart-HTTP Git transport, capability-gated auth, JSON/SQLite/Postgres storage paths, organization and project isolation, a durable job queue, and evidence integration seams for Kujo tools.

## Five-minute example

```bash
npm install
npm test
node bin/source.js demo --password '<12+ character local password>'
node bin/source.js serve --port 8787
```

The demo prints the exact IDs used to sign in and does not create a shared default password.

## What you get

A local vertical slice for `Project → Work → Session → Change → Evidence → Decision → Canonical Git State`, plus agent discovery and Git contribution surfaces.

## Boundaries

Source is an MVP, not a blanket hosted-service claim. JSON is single-process; exposed or multi-process serving requires the documented Postgres, writer-fencing, TLS, worker, capacity, and operations controls.

## Reference

Source source is currently private. Public source access and installation are not available; the commands above are for authorized checkout owners.
