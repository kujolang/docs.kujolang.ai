---
title: SSG
description: Deterministic Markdown-to-site publishing with templates, feeds, sitemap, and llms.txt.
template: docs
section: Showcases
nav_title: SSG
order: 40
audience: developer
difficulty: intermediate
status: local scope verified
version: current
scope: local-first
source_repo: ssg
previous: /showcases/ai-chat/
next: /showcases/totalrecall/
tags: [showcase, static, publishing]
---


## Use it when…

You need a transparent, deterministic static publishing pipeline whose content, templates, assets, and generated outputs stay visible.

## Five-minute example

```bash
kujo run build.kujo -- --site-url https://example.com
bash scripts/validate-generated-output.sh output
```

## What you get

Markdown routes, custom collections, templates, local search, feeds, sitemap, robots, `llms.txt`, and validation scripts.

## How it fits

This docs site uses the reusable SSG docs starter and vendors the Kujo Site Kit assets directly.

## Boundaries

SSG is a generator, not a hosted publishing service or a guarantee of SEO/accessibility outcomes. Review generated output.
