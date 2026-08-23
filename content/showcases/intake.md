---
title: Intake
description: Normalize inbound work, route it through policy, and require approval before external effects.
template: docs
section: Showcases
nav_title: Intake
order: 60
audience: developer
difficulty: intermediate
status: local-first showcase; live mailbox smoke ready
version: current
last_updated: 2026-08-23
scope: local-first reference application
source_repo: intake
tags: [showcase, intake, approvals, automation]
---

## What it demonstrates

Intake normalizes manual, file, webhook, Slack, GitHub, Jira, Linear, ClickUp, and email inputs into durable items, applies deterministic rules and safety checks, proposes actions, requires policy-defined approval, and exports reviewed learning.

## Five-minute example

```bash
npm install
npm link
intake init
intake item create --title "Client asked about pricing" --body "Follow up with details" --queue sales
intake items
intake doctor
```

## What you get

Local state under `.intake/`, a token-authenticated localhost dashboard, source health, actions, approvals, audit logs, backups, retention controls, and Strata or TotalRecall-compatible learning exports.

## Boundary

Intake is ready for local-first live mailbox smoke and adapter development, not a fully packaged enterprise deployment. Direct sending is blocked by default; remote effects stay behind policy and human approval.

## Reference

See the [Intake repository](https://github.com/kujolang/intake).
