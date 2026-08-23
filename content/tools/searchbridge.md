---
title: SearchBridge
description: Normalize search, analytics, performance, keyword, backlink, and submission providers.
template: docs
section: Tools
nav_title: SearchBridge
order: 275
audience: developer
difficulty: advanced
status: preview 0.3.0
version: current
last_updated: 2026-08-23
scope: fixture-first external-data gateway
source_repo: searchbridge
tags: [tool, search, analytics, web]
---

## Use it when…

A WebOps workflow needs one bounded contract for search performance, analytics, URL inspection, PageSpeed, CrUX, backlinks, keyword data, or explicit index submission.

## Five-minute example

```bash
./searchbridge doctor
./searchbridge capabilities --deterministic
./searchbridge search-performance --fixture --offline --deterministic
./searchbridge batch --fixture --offline --commands pagespeed,crux
```

## What you get

Credential-redacted, bounded evidence that can use fixtures, caches, protected replay, or explicitly configured provider adapters.

## Boundaries

SearchBridge `0.3.0` currently pins a prepared Kujo `v1.0.2` source commit until that runtime is released. Live provider credentials, quotas, property access, and active submission remain explicit operator boundaries.

## Reference

See the [SearchBridge repository](https://github.com/kujolang/searchbridge).
