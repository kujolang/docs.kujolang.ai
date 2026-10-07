---
title: AI Chat
description: A local multi-provider agent workspace with live code review, durable supervision, isolated worktrees, scoped tools, and persistent chat tabs.
template: docs
section: Showcases
nav_title: AI Chat
order: 30
audience: developer
difficulty: intermediate
status: local scope verified
version: 1.3.0
last_updated: 2026-10-06
scope: local-first
source_repo: ai-chat
previous: /showcases/crud-api/
next: /showcases/ssg/
tags: [showcase, ai, chat]
---


## Use it when…

You want to run coding, review, content, or operations agents side by side while keeping their permissions, code changes, tool evidence, and recovery controls visible.

## Interface overview

| Surface | What is available |
| --- | --- |
| App | Local multi-pane chat UI, persistent workspace tabs, live diffs, review comments, plans, steering, checkpoints, and a command palette |
| API | Health, providers, state, automations, chat, SSE streaming, transcription, MCP management, attention, artifacts, worktrees, and review routes |
| State | SQLite conversations, incremental state changes, encrypted keys and checkpoints, backups, attention events, and execution receipts |
| Integrations | OpenAI-compatible providers, native Codex, local ChatGPT plan access, Watchdog, Hermes / Nous, xAI OAuth, local tools, browser sessions, scoped MCP, and fixture mode |

## Main workflows

- Configure provider profiles and models in Settings, then compare one prompt across multiple panes.
- Review each agent's live file changes in unified or split diffs, comment on files or hunks, and use conflict-aware checkpoint restore or rewind when necessary.
- Isolate coding chats in managed Git worktrees, attach bounded files and images, and inspect command, test, browser, source, and error artifacts.
- Grant each chat only the MCP tools and resources it needs; use the attention inbox and command palette to move between pending approvals and active chats.
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

A local agent workspace with encrypted provider profiles, SSE streaming, multi-chat tabs, actionable code review, durable supervision, scoped extensions, transcription paths, and fixture mode.

## How it fits

Start with [AI SDK](/tools/ai-sdk/) for the provider contract and [Watchdog](/tools/watchdog/) for local telemetry.

## Boundaries

This is a local multi-provider showcase, not a managed chat service or deployed production certification. Credentials, permissions, proxy topology, backups, managed worktrees, and deployment remain integrator-owned. Local writes, shell execution, MCP connections, desktop notifications, browser execution, and ChatGPT plan access are explicit opt-ins.

## Reference

See the [AI Chat repository](https://github.com/kujolang/ai-chat) for API, provider, and deployment configuration.

## Current release and upgrade

[AI Chat 1.3.0](https://github.com/kujolang/ai-chat/releases/tag/v1.3.0) ships harness roadmap items HR-01 through HR-10: live per-pane code diffs, review comments, encrypted checkpoints and rewind, plans and steering, managed Git worktrees, typed attachments, execution artifacts, scoped MCP connections, an attention inbox, a command palette, and persistent multi-chat tabs. Deferred tools and external MCP capabilities remain subject to request-scoped authorization and interactive approvals.

Use **Node 22.17.0** and `npm ci`. Back up the database with its matching encryption secret, configuration, action manifests, and uncommitted managed worktrees before upgrading. Browser execution additionally needs Playwright Chromium and macOS Seatbelt or Linux Bubblewrap with permitted namespaces; unavailable containment fails closed. Follow the [versioned upgrade procedure](https://github.com/kujolang/ai-chat/blob/v1.3.0/SETUP_AND_INSTALL.md#upgrading-to-130).

The release passed 758 local tests with 756 passes and two platform skips, authenticated fixture smoke, a zero-vulnerability production dependency audit, ShipCheck's error-level gate, and GitHub CI. Its historical eight-hour reliability soak remains incomplete; the partial run is not a production-readiness certification.
