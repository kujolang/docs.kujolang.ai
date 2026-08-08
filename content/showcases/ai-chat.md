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
version: current
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
npm install
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
