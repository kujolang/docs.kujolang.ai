---
title: Intake
description: Normalize inbound work, route it through policy, and require approval before external effects.
template: docs
section: Showcases
nav_title: Intake
order: 60
audience: developer
difficulty: intermediate
status: GitHub source release for local operators
version: 0.2.0
last_updated: 2026-10-13
scope: local-first reference application
source_repo: intake
tags: [showcase, intake, approvals, automation]
---

## What it demonstrates

Intake normalizes manual, file, webhook, Slack, GitHub, Jira, Linear, ClickUp, and email inputs into durable items, applies deterministic rules and safety checks, proposes actions, requires policy-defined approval, and exports reviewed learning.

## Install and try it

Requires Node.js 20.19 or newer.

```bash
git clone --branch v0.2.0 https://github.com/kujolang/intake.git
cd intake
npm ci
npm link
intake init
intake item create --title "Client asked about pricing" --body "Follow up with details" --queue sales
intake items
intake doctor
```

## What you get

Local state under `.intake/`, a token-authenticated localhost dashboard, source health, actions, approvals, audit logs, backups, retention controls, and Strata or TotalRecall-compatible learning exports.

## Boundary

Intake 0.2.0 is the first tagged GitHub source release. It is a JavaScript app, not a native Kujo package. The npm manifest remains private, and the app is not enrolled in Kennel.

Use it for local operation and adapter development. Direct sending is blocked by default. Validate live providers, deployment access controls, and recovery requirements before relying on it in a shared environment.

## Recovery

Receiver retries preserve classification and operator changes. Interrupted configuration imports and restores leave journals that block ordinary access until recovery. Stop writers, repair filesystem errors, and run `intake store recover --dir STORE`. Keep corrupt metadata for inspection; `--force` does not bypass schema or journal validation.

Recovery never replays outbound actions. Reconcile any uncertain external effect before approving another attempt. See the [upgrade notes](https://github.com/kujolang/intake/blob/v0.2.0/docs/releases/0.2.0.md).

## Reference

- [Intake 0.2.0 release](https://github.com/kujolang/intake/releases/tag/v0.2.0)
- [Website overview](https://kujolang.ai/ecosystem/intake/)


See the [Intake repository](https://github.com/kujolang/intake).
