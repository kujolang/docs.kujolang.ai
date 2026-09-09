---
title: AI Chat
description: A local multi-provider chat application with encrypted profiles, streaming, transcription, and fixture mode.
template: docs
section: Showcases
nav_title: AI Chat
order: 30
audience: developer
difficulty: intermediate
status: local scope verified
version: 1.2.0
last_updated: 2026-09-09
scope: local-first
source_repo: ai-chat
previous: /showcases/crud-api/
next: /showcases/ssg/
tags: [showcase, ai, chat]
---


## Use it when…

You want a concrete local application surface for provider profiles, streaming, transcription, and offline fixtures.

## Interface overview

| Surface | What is available |
| --- | --- |
| App | Local multi-pane chat UI, provider/model profiles, and saved pane layouts |
| API | Health, providers, state, automations, chat, SSE streaming, and transcription routes |
| State | SQLite conversations, incremental state changes, encrypted keys, backups, and vacuum |
| Integrations | OpenAI-compatible providers, Watchdog, local tools, browser sessions, and fixture mode |

## Main workflows

- Configure provider profiles and models in Settings, then compare one prompt across multiple panes.
- Use `/api/chat/stream` for `token`, `thinking`, `done`, and `error` SSE events.
- Run the smoke suite without provider credentials to verify the fixture-backed application contract.
- Back up and maintain SQLite state with the supplied npm scripts before operational changes.

## Five-minute example

```bash
npm ci
npm run dev
npm run smoke
```

## What you get

A local chat UI, encrypted provider profiles, SSE streaming, transcription paths, and fixture mode.

## How it fits

Start with [AI SDK](/tools/ai-sdk/) for the provider contract and [Watchdog](/tools/watchdog/) for local telemetry.

## Boundaries

This is a local multi-provider showcase, not a managed chat service. Credentials and deployment are integrator-owned.

## Reference

See the [AI Chat repository](https://github.com/kujolang/ai-chat) for API, provider, and deployment configuration.

## Current release and upgrade

[AI Chat 1.2.0](https://github.com/kujolang/ai-chat/releases/tag/v1.2.0) adds encrypted execution journals, durable action receipts, interrupted-turn recovery, bounded stream replay, provider-context budgeting, and configured RAG documentation lookup with source links and code-example language preferences. Deferred tools remain subject to request-scoped authorization.

Use **Node 22.17.0** and `npm ci`. Back up the database together with its matching encryption configuration before upgrading, then restart the application. Browser execution additionally needs Playwright Chromium and macOS Seatbelt or Linux Bubblewrap with permitted namespaces; unavailable containment fails closed. Follow the [versioned upgrade procedure](https://github.com/kujolang/ai-chat/blob/v1.2.0/SETUP_AND_INSTALL.md#upgrading-to-120).

The release reports 387 local tests passed and one Linux-only skip. Its full eight-hour reliability soak is incomplete; the partial run is not a production-readiness certification.
