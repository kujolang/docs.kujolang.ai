---
title: VersionSeal
description: Bind human approval and authority to an exact checksum-verified version.
template: docs
section: Tools
nav_title: VersionSeal
order: 315
audience: all
difficulty: advanced
status: production-oriented local scope
version: current
last_updated: 2026-08-23
scope: local-first approval evidence
source_repo: versionseal
tags: [tool, approval, checksums, governance]
---

## Use it when…

An approval must identify an exact artifact version, actor authority, policy, expiry, quorum, separation of duties, and revocation state.

## Five-minute example

```bash
versionseal init --state .versionseal --json
versionseal approve --input fixtures/core.json --actor approver --json
versionseal validate --json
versionseal export --output versionseal-export.json --json
```

## What you get

Immutable approval and revocation records, checksum verification, audit events, policy evaluation, optional RSA/HMAC evidence, and portable exports.

## Boundaries

VersionSeal does not provide hosted identity. Authority, key custody, and organization-specific approval policy must be established by the deployment.

## Reference

See the [VersionSeal repository](https://github.com/kujolang/versionseal).
