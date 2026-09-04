---
title: SearchBridge
description: Fetch normalized search, analytics, page-performance, backlink, keyword, and indexing evidence through bounded provider contracts.
template: docs
section: Tools
nav_title: SearchBridge
order: 275
audience: developer
difficulty: advanced
status: stable 1.0.0
version: 1.0.0
last_updated: 2026-09-04
scope: local CLI and SDK evidence gateway
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

Credential-redacted, bounded `searchbridge.result/v1` evidence that can use deterministic fixtures, caches, protected replay, or explicitly configured provider adapters. The supported release channel is a checksum-verified self-contained GitHub release bundle; TypeScript, Rust, and Go SDK archives ship with the release.

## Provider status in 1.0.0

| Tier | Providers |
| --- | --- |
| `stable-live` | Google Search Console, Google Analytics 4, PageSpeed Insights, Chrome UX Report |
| `fixture-only` | Cloudflare, IndexNow, Bing Webmaster, Ahrefs, DataForSEO, SerpApi |
| `external-reference` | Plausible signed adapter package |
| `disabled` | Semrush |

The stable-live tier passed an owner-authorized 16-case live matrix before release. Cloudflare and IndexNow remain fixture-only until the separately documented v1.1 review; no live success or indexing outcome is claimed for either provider.

## Boundaries

SearchBridge fetches and normalizes provider evidence; it does not interpret SEO performance. Missing access degrades individual capabilities instead of disabling the entire tool. Live provider credentials, quotas, property access, paid-call authorization, and every submission remain explicit operator boundaries. Evidence commands are read-only; submission is separate and requires the exact capability plus `--act --yes` on every invocation. A submission receipt never claims indexing.

## Reference

See the [SearchBridge v1.0.0 release](https://github.com/kujolang/searchbridge/releases/tag/v1.0.0), [repository](https://github.com/kujolang/searchbridge), and [support matrix](https://github.com/kujolang/searchbridge/blob/v1.0.0/docs/support-matrix.md).
