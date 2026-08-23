---
title: Cinch
description: A local development harness for files, Git, commands, AI context, tools, and proof.
template: docs
section: Showcases
nav_title: Cinch
order: 70
audience: developer
difficulty: advanced
status: macOS-first release candidate / hardened alpha
version: current
last_updated: 2026-08-23
scope: local desktop application
source_repo: cinch
tags: [showcase, desktop, developer-tools, agents]
---

## What it demonstrates

Cinch combines workspaces, file editing, Git review, approved commands, OpenRouter chat, explicit context, MCP processes, local retrieval, Kujo tool launches, proof artifacts, and Trail exports in a Tauri desktop application.

## Run it

```bash
pnpm install
pnpm tauri:dev
pnpm verify
```

## What you get

A macOS-first desktop workflow for prompt-to-PR work with SQLite state, approval gates, diffs, tests, browser proof, context audit manifests, and portable Trail records.

## Boundary

Signing, notarization, broader native automation, and fresh-machine Windows/Linux validation remain release gates. Live application data is not application-layer encrypted; optional encrypted backup bundles protect copied backups.

## Reference

See the [Cinch repository](https://github.com/kujolang/cinch).
