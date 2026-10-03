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
version: 1.1.0
last_updated: 2026-09-29
scope: local-first
source_repo: ssg
previous: /showcases/ai-chat/
next: /showcases/presentations/
tags: [showcase, static, publishing]
---


## Use it when…

You need a transparent, deterministic static publishing pipeline whose content, templates, assets, and generated outputs stay visible.

[Release 1.1.0](https://github.com/kujolang/ssg/releases/tag/v1.1.0), published September 29, 2026, adds default-on experimental WebMCP, ten executable local Ability workflows, safer cleanup and metadata handling, smaller featured images, and plain sitemap XML.

## Interface overview

| Surface | What is available |
| --- | --- |
| Inputs | Markdown content, YAML/JSON config, templates, assets, and custom collections |
| Build | Output/content/template overrides, draft previews, minification, aliases, and parallel shards |
| Publishing | Clean routes, feeds, sitemap, robots, `llms.txt`, local search, SEO, and social metadata |
| Browser agents | Default-on experimental static WebMCP; four public read-only tools |
| Local agents | Ability pack 1.0.0: ten bounded workflows with approved, idempotent writes |
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

## Browser agents and local execution

WebMCP emits `.well-known/kujo-site-index.json` and a same-origin adapter exposing `get_site_info`, `search_site`, `list_content`, and `get_content`. It needs no server after deployment and leaves unsupported browsers unchanged. To omit both artifacts:

```bash
kujo run build.kujo -- --site-url https://example.com --no-webmcp
```

Or set `webmcp: false` in the site config. Drafts never enter the public index, including preview builds. `search_exclude: true` removes search visibility but does not restrict list or exact retrieval. `nav_hide` only affects navigation.

The executable local Ability pack covers project/source inspection, validation, full and sharded builds with approved draft previews, output inspection, comparison, deployment readiness, and deterministic artifact export. Pack 1.0.0 and its pinned Ability 1.0.1 dependency are versioned independently of SSG 1.1.0. Writes require explicit approval and keyed idempotency. MCP hosts bind these operations in a trusted local process or authenticated gateway; generated pages cannot execute them. No publish or deploy Ability is included.

See the [WebMCP guide](https://github.com/kujolang/ssg/blob/v1.1.0/docs/webmcp.md) and [Ability integration](https://github.com/kujolang/ssg/blob/v1.1.0/docs/ability-integration.md).

## How it fits

This docs site uses the reusable SSG docs starter and vendors the Kujo Site Kit assets directly.

## Boundaries

SSG is a generator, not a hosted publishing service or a guarantee of SEO/accessibility outcomes. Review generated output.

## Reference

See the [SSG repository](https://github.com/kujolang/ssg) for config fields, CLI flags, and starter structure.
