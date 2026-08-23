---
title: SiteProbe
description: Crawl a bounded website surface and preserve deterministic intelligence evidence.
template: docs
section: Tools
nav_title: SiteProbe
order: 270
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: read-only website intelligence
source_repo: siteprobe
tags: [tool, web, crawl, evidence]
---

## Use it when…

A website needs a bounded, same-origin inventory of URLs, status, canonicals, metadata, schema, links, sitemaps, content, and change evidence.

## Five-minute example

```bash
./siteprobe crawl https://example.com --out .siteprobe/example
./siteprobe validate .siteprobe/example
./siteprobe report .siteprobe/example
```

## What you get

An immutable run that can be validated, digest-verified, compared with a baseline, reported, or signed with HMAC-SHA-256.

## Boundaries

SiteProbe is read-only. It blocks private and special-use network targets by default, enforces same-origin crawling and redirect checks, respects bounded crawl and output budgets, and refuses an existing output path.

## Reference

See the [SiteProbe repository](https://github.com/kujolang/siteprobe).
