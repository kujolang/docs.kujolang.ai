---
title: Tribunal
description: Turn consequential proposals into adversarial, replayable decision evidence.
template: docs
section: Tools
nav_title: Tribunal
order: 125
audience: all
difficulty: advanced
status: stable 1.0.1 operator-controlled scope
version: current
last_updated: 2026-09-05
scope: local and operator-controlled
source_repo: tribunal
tags: [tool, decisions, review, evidence]
---

## Use it when…

A consequential proposal needs independent specialist testimony, cross-examination, a fatal-flaw pass, a ruling, and an execution-ready decision packet.

## Current release: 1.0.1

[Tribunal 1.0.1](https://github.com/kujolang/tribunal/releases/tag/v1.0.1) is a patch release for local and operator-controlled review. It strengthens credential redaction, bridge failure handling, bundle integrity, and concurrent index coordination, and reduces repeated prompt and memory work. The v1 library API and evidence formats are unchanged.

Download the release archive and its receipt, then follow [release verification](https://github.com/kujolang/tribunal/blob/v1.0.1/docs/RELEASE_VERIFICATION.md) before running it. Use the pinned Kujo runtime and integrations in the [integration matrix](https://github.com/kujolang/tribunal/blob/v1.0.1/docs/INTEGRATION_MATRIX.md) to reproduce release checks.

## Five-minute example

```bash
./bin/tribunal doctor
./bin/tribunal validate examples/product-decision.md
./bin/tribunal review examples/product-decision.md --panel fast-two-model
./bin/tribunal list --status completed --limit 5
```

Mock mode is the deterministic, offline, credential-free default.

## What you get

Structured, replayable, SHA-256-sealed evidence with optional RSA signing and a portable decision packet.

## Boundaries

Tribunal does not certify hosted, regulated, shared-filesystem, identity, signing-custody, remote-storage, or provider deployments. Windows is outside the documented v1 platform scope.

## Recover an interrupted index update

An interrupted index mutation can leave a lock or dirty marker. Follow the [index recovery procedure](https://github.com/kujolang/tribunal/blob/v1.0.1/docs/OPERATIONS.md) before rebuilding; confirm that no writer is active. Do not run older Tribunal versions against the same storage concurrently because they bypass the new index coordination. Preserve sealed run evidence during recovery.

## Reference

See the [Tribunal repository](https://github.com/kujolang/tribunal).
