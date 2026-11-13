---
title: SiteKit
description: Vendor an accessible, semantic, token-driven design system for static sites.
template: docs
section: Tools
nav_title: SiteKit
order: 260
audience: developer
difficulty: intermediate
status: stable v1 consumer contract
version: 1.2.0
last_updated: 2026-11-12
scope: source and vendored distribution
source_repo: site-kit
previous: /tools/paperclip/
tags: [tool, design-system, accessibility, web]
---

## Use it when…

A static site needs shared tokens, themes, component CSS, templates, recipes, and progressive enhancement without a framework runtime.

## Install or vendor

Build with a supported patched Node.js branch (22.23.4+, 24.22.1+, or 26.12.1+, within its corresponding major) and copy the generated `dist/` directory into the consumer, or vendor the `dist/` directory from an exact GitHub release archive. Keep its directory structure intact so font paths remain valid.

## What you get

CSS, fonts, schemas, templates, component metadata, and optional `sitekit.js` behavior for `kujo-light`, `kujo-dark`, and `personal-dark` themes. The legacy `bzby` theme is an explicit opt-in compatibility stylesheet.

## New in 1.2.0

The complete distribution includes four optional runnable recipes in `dist/recipes/`: documentation code panels, catalog filtering, documentation workspaces, and token references. Load their CSS and behavior explicitly; core component APIs remain unchanged. Copying preserves canonical source, catalog instances remain independent, and token references show light/dark values and direct consumers.

Code-block colors and native slider accents now use semantic theme tokens. See the [v1.2.0 release](https://github.com/kujolang/site-kit/releases/tag/v1.2.0) and bundled recipe README for integration and lifecycle contracts.

## Boundaries

SiteKit remains `private: true`; npm publication is not part of v1. WCAG 2.2 AA is the source-component and tested-reference baseline, not certification of arbitrary downstream pages.

## Reference

See the [SiteKit repository](https://github.com/kujolang/site-kit).
