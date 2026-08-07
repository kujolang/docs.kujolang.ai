---
title: SSG
description: Deterministic Markdown-to-site publishing with templates, feeds, sitemap, and llms.txt.
template: docs
section: Showcases
nav_title: SSG
order: 40
audience: developer
difficulty: intermediate
status: launch scope
version: current
scope: local-first
source_repo: ssg
next: /showcases/intake/
tags: [showcase, static, publishing]
---

# SSG

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

This docs site uses the reusable [docs starter](../starters/docs-site/README.md) and vendors the [Site Kit](/ecosystem/site-kit/) bundle.

## Boundaries

SSG is a generator, not a hosted publishing service or a guarantee of SEO/accessibility outcomes. Review generated output.

