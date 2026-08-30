---
title: CMS
description: A framework-neutral content backend with first-class administration, extensions, SEO, identity, AI abilities, MCP, and WebMCP.
template: docs
section: Showcases
nav_title: CMS
order: 10
audience: developer
difficulty: intermediate
status: released
version: 1.1.0
last_updated: 2026-08-30
scope: framework-neutral backend
source_repo: cms
previous: /tools/
next: /showcases/crud-api/
tags: [showcase, cms, content, agents, webmcp, extensions]
---


Kujo CMS 1.1.0 is a server-first content backend for human administration, custom frontends, integrations, terminal workflows, and agents. The core owns portable content behavior; the separate CMS Example shows one complete Next.js-based administration and publication experience without making that framework part of the CMS contract.

## Use it when…

You need structured publishing that can serve a custom website, application, CLI, or agent without rebuilding the same identity, editorial, SEO, extension, and permission rules in every client.

## Interface overview

| Surface | What is available |
| --- | --- |
| Runtime | `backend/runtime/main.kujo`; no separate CMS CLI wrapper |
| Editorial core | Content types, entries, taxonomies, terms, media, menus, revisions, rollback, locking, and scheduling |
| Identity and access | Users, profiles, roles, registration policy, trusted identity exchange, revocable sessions, API tokens, and effective administration capabilities |
| SEO and sharing | Filterable SEO inventory, issue signals, focused edits, bulk updates, network selection, and per-network account attribution |
| Themes and plugins | Versioned manifests, validation, verified ZIP ingestion, installation receipts, activation, export, settings, branded artwork, and ordered administration links |
| Agent access | Schema-described Abilities API, permission-scoped execution, confirmation-gated mutations, audit receipts, plugin abilities, connectors, MCP-ready descriptors, and built-in WebMCP |
| Clients | Dependency-free JavaScript and PHP clients plus documented adapter boundaries for other frameworks and languages |
| Discovery and delivery | `/health`, `/v1`, `/v1/contract`, `/v1/openapi.json`, published content, feeds, sitemap, robots, `llms.txt`, and WebMCP discovery |
| Operations | Rate limits, idempotency, jobs, webhooks, migrations, audit logs, backup, restore, dead-letter replay, and release gates |

## One contract for people and agents

The administration UI, API, terminal helpers, and agent integrations share the same backend rules. An editor can correct SEO metadata in the CMS Example while an authorized agent can make the equivalent focused or bulk update through the API. A plugin can register an ability or connector, and compatible clients can inspect its schema, permission, and mutation boundary before calling it.

WebMCP is enabled by default. Its public browser tools expose site information, search, published-content listings, and exact published records. Drafts and mutations remain behind the CMS authorization boundary. Traditional MCP clients can use the CMS tool descriptors and connector layer alongside WebMCP.

## Portable themes and plugins

Theme packages describe frontend entrypoints, templates, assets, settings, content types, menu locations, author links, branded artwork, and administration navigation. Plugin packages can declare connector, webhook, browser, or hybrid runtimes plus events, abilities, connectors, settings, and administration links.

ZIP installation verifies compressed and expanded size, file count, package structure, manifest location, and SHA-256 integrity before registering the package. Uploading a package does not execute its code. The standalone [Field Notes theme](https://github.com/kujolang/cms-field-notes-theme) and [contact form plugin](https://github.com/kujolang/cms-contact-form) provide forkable package examples.

## Five-minute example

```bash
git clone https://github.com/kujolang/cms.git
cd cms
cp .env.example .env
kujo run --interpreter backend/runtime/main.kujo
curl http://127.0.0.1:4200/v1/openapi.json
```

To run the full site and administration showcase, clone [CMS Example](https://github.com/kujolang/cms-example), install its dependencies, then start the backend, seed data, and launch the frontend in separate terminals:

```bash
npm run cms:start
npm run cms:seed
npm run dev
```

Local startup generates a private development token. Production deployments must use rotated secrets, a trusted identity adapter, explicit ingress and rate limits, durable storage, backups, and the documented security review.

## API and terminal parity

The core repository includes focused terminal helpers for SEO and social settings, content and media workflows, extension packages, and AI abilities and connectors. There is intentionally no second all-purpose CMS CLI that could drift from the HTTP contract.

## How it fits

Use the CMS when content needs an ongoing editorial and administration backend. Compare it with [CRUD API](/showcases/crud-api/) for a smaller application API pattern and [SSG](/showcases/ssg/) for deterministic file-based publishing.

## Boundaries

CMS 1.1.0 supplies production-oriented application contracts and release gates; it does not make every deployment enterprise-complete. Infrastructure, compliance, observability, storage, recovery targets, provider credentials, and governance still require environment-specific proof. The default WebMCP tools are intentionally read-only, and extension code is not executed during package installation.

## Reference

- [CMS 1.1.0 release](https://github.com/kujolang/cms/releases/tag/v1.1.0)
- [CMS repository](https://github.com/kujolang/cms)
- [CMS Example 1.1.0 release](https://github.com/kujolang/cms-example/releases/tag/v1.1.0)
- [Framework adapter guidance](https://github.com/kujolang/cms/blob/main/docs/framework-adapters.md)
- [Extension package contract](https://github.com/kujolang/cms/blob/main/docs/extensions.md)
- [WebMCP contract](https://github.com/kujolang/cms/blob/main/docs/webmcp.md)
