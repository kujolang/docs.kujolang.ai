---
title: Kujo Pi
description: Install the opt-in Kujo integration for Pi, with Ability tools, Watchdog metadata, and bounded operation receipts.
custom_url: kujo-pi
template: docs
section: Tools
nav_title: Kujo Pi
order: 75
audience: developer
difficulty: intermediate
status: released
version: 1.1.0
last_updated: 2026-09-26
scope: opt-in Pi integration
source_repo: kujo-pi
tags: [tool, pi, integrations, telemetry, ability]
---

## Install and start

Kujo Pi 1.1.0 is a separate npm package for the Pi host. It requires Node.js 22.19.0 or newer, npm 10 or newer, and Pi 0.84.3 or newer within the 0.x line. Install the [Kujo runtime](/install/) separately for Kujo-backed operations.

```bash
pi install npm:@kujolang/kujo-pi@1.1.0
```

Start Pi in a trusted repository, configure `KUJO_BIN` or put Kujo on PATH, then run:

```text
/kujo setup
/kujo enable understand
```

Use `kujo_doctor` to inspect available integrations and configuration. Installation alone does not install Kujo, start service daemons, activate optional tools, or send lifecycle telemetry. Enable only the task packs you need.

## Ability tools

Configure `KUJO_ABILITY_GATEWAY_URL` and a least-privilege `KUJO_ABILITY_GATEWAY_TOKEN` through your host environment. Remote gateways require HTTPS. Then enable:

```text
/kujo enable kujo_ability_list kujo_ability_call
```

Discovery returns principal-visible Abilities. Execution requires Pi project trust and Pi approval; the application gateway still owns authorization, request-bound approval, idempotency and audit policy. Enabling a tool does not grant application permission. See [Ability](/tools/ability/).

## Watchdog lifecycle metadata

For a configured Watchdog service supporting the `watchdog.telemetry.v2` intake contract:

```bash
export KUJO_WATCHDOG_URL=http://127.0.0.1:7700
export KUJO_WATCHDOG_TELEMETRY=metadata
```

Only trusted projects activate the bridge. It records allowlisted lifecycle metadata, not prompts, responses, tool arguments, shell text or file contents. Provider correlation headers go only to the configured Watchdog proxy provider. Watchdog's own service release and configuration remain separate from the Pi package version.

The local spool defaults to 2,000 committed bundles and 5 MiB. The same limits independently bound each process's pending queue. New batches are rejected when that queue is full; Doctor exposes cumulative loss and write-failure counters. This is best-effort telemetry, not a lossless audit sink.

At initialization, owned temporary files can be recovered when their local process no longer exists. Live writers, uncertain owners and symlinks are preserved. Busy or inaccessible orphans produce deferred-cleanup diagnostics. Legacy, unowned and foreign-scope temporary files require manual removal after all relevant writers stop. Use a local spool, not a shared network filesystem.

## Receipts and compatibility

Optional receipts (`KUJO_PI_RECEIPTS=1`) keep v1 result and receipt contracts. A successful operation remains successful if receipt storage fails; inspect the warning rather than rerunning a side effect solely to repair its receipt.

Artifact snapshots cover at most 128 files, 10,000,000 content bytes and 4,096 enumerated entries by default. Wide or changing trees can produce a digest warning. These are bounded diagnostics, not complete integrity proofs. Existing tool inputs and CLI flags remain compatible; Doctor diagnostics and Ability tools are additive.

## Reference

- [Kujo Pi 1.1.0 release](https://github.com/kujolang/kujo-pi/releases/tag/v1.1.0)
- [Pinned onboarding guide](https://github.com/kujolang/kujo-pi/blob/v1.1.0/docs/pi-onboarding.md)
- [Telemetry configuration and recovery](https://github.com/kujolang/kujo-pi/blob/v1.1.0/docs/watchdog-telemetry-bridge.md)
- [Operation and receipt contracts](https://github.com/kujolang/kujo-pi/blob/v1.1.0/docs/contracts.md)
