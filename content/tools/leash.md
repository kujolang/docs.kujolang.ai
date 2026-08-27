---
title: Leash
description: Supervise local AI agents through policy-gated approvals and a mobile control plane.
template: docs
section: Tools
nav_title: Leash
order: 140
audience: developer
difficulty: advanced
status: private preview
version: current
last_updated: 2026-08-27
scope: local-first supervision
source_repo: leash
previous: /tools/watchdog/
next: /tools/muzzle/
tags: [tool, approvals, supervision]
---

## Use it when…

Local coding agents need human approval, policy-as-code risk classification, durable decisions, and remote supervision without moving execution off the workstation.

## Interface overview

| Surface | What is available |
| --- | --- |
| Daemon | Primary Rust service with health, session, device, action, and decision routes |
| Policy | Kujo rules for risk classification, validation, and notification behavior |
| Agent adapters | Generic tmux, Copilot, Claude Code, Codex, and native Dispatch events |
| Mobile | Android control surface, JWT device identity, FCM notifications, and decision audit trail |

## Main workflows

- Run the daemon beside tmux-hosted agents so execution and working data remain local.
- Convert agent prompts and lifecycle output into structured, policy-classified events.
- Approve or reject actions through the API or mobile surface, with stronger confirmation for dangerous actions.
- Use the append-only audit trail to review who decided what and when.

## Five-minute example

```bash
cd daemon
cargo build --release
cp config.example.yml config.yml
./target/release/leashd config.yml
curl http://127.0.0.1:9191/health
```

## What you get

A local daemon, Kujo policy rules, tmux-based agent adapters, an audit trail, and an Android control surface for approval decisions.

## How it fits

Leash can supervise [Dispatch](/tools/dispatch/) workflows and use [Spec](/tools/spec/) or [Eval](/tools/eval/) results as approval context.

## Boundaries

The Rust daemon is the primary implementation. Android device, FCM, signing, notarization, packaged distribution, and public release proof remain external actions.

## Reference

Leash source is currently a private repository, so public source access and installation are not available. Treat this page as capability orientation rather than public onboarding.
