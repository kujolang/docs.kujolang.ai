---
title: Leash
description: Supervise local AI agents through policy-gated approvals and a mobile control plane.
template: docs
section: Tools
nav_title: Leash
order: 140
audience: developer
difficulty: advanced
status: local scope verified
version: current
scope: local-first supervision
source_repo: leash
previous: /tools/watchdog/
next: /tools/muzzle/
tags: [tool, approvals, supervision]
---

## Use it when…

Local coding agents need human approval, policy-as-code risk classification, durable decisions, and remote supervision without moving execution off the workstation.

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

See the [Leash repository](https://github.com/kujolang/leash).
