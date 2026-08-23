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
last_updated: 2026-08-23
scope: local-first
source_repo: ssg
previous: /showcases/ai-chat/
next: /showcases/totalrecall/
tags: [showcase, static, publishing]
---


## Use it when…

You need a transparent, deterministic static publishing pipeline whose content, templates, assets, and generated outputs stay visible.

## Interface overview

| Surface | What is available |
| --- | --- |
| Inputs | Markdown content, YAML/JSON config, templates, assets, and custom collections |
| Build | Output/content/template overrides, draft previews, minification, aliases, and parallel shards |
| Publishing | Clean routes, feeds, sitemap, robots, `llms.txt`, local search, SEO, and social metadata |
| Extensions | Reusable docs starter, template overrides, fonts, image mirroring, and DocGen bridge |

## Main workflows

- Scaffold a config, add Markdown and templates, then build through the standard Kujo VM path.
- Override site URL and output directory for preview or production without changing file defaults.
- Validate generated links, metadata, XML, and assets before serving the static output.
- Use the DocGen bridge or custom collections when source docs need first-class routes and navigation.

## Five-minute example

```bash
kujo run build.kujo -- --site-url https://example.com
bash scripts/validate-generated-output.sh output
kujo serve output --port 8080
```

## What you get

Markdown routes, custom collections, templates, local search, feeds, sitemap, robots, `llms.txt`, and validation scripts.

## How it fits

This docs site uses the reusable SSG docs starter and vendors the Kujo Site Kit assets directly.

## Boundaries

SSG is a generator, not a hosted publishing service or a guarantee of SEO/accessibility outcomes. Review generated output.

## Reference

See the [SSG repository](https://github.com/kujolang/ssg) for config fields, CLI flags, and starter structure.
