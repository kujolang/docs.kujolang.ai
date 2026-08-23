---
title: Tribunal
description: Turn consequential proposals into adversarial, replayable decision evidence.
template: docs
section: Tools
nav_title: Tribunal
order: 125
audience: all
difficulty: advanced
status: stable 1.0 operator-controlled scope
version: current
last_updated: 2026-08-23
scope: local and operator-controlled
source_repo: tribunal
tags: [tool, decisions, review, evidence]
---

## Use it when…

A consequential proposal needs independent specialist testimony, cross-examination, a fatal-flaw pass, a ruling, and an execution-ready decision packet.

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

## Reference

See the [Tribunal repository](https://github.com/kujolang/tribunal).
