---
title: SiteKit
description: Vendor an accessible, semantic, token-driven design system for static sites.
template: docs
section: Tools
nav_title: SiteKit
order: 260
audience: developer
difficulty: intermediate
status: stable 1.0 consumer contract
version: current
last_updated: 2026-08-23
scope: source and vendored distribution
source_repo: site-kit
tags: [tool, design-system, accessibility, web]
---

## Use it when…

A static site needs shared tokens, themes, component CSS, templates, recipes, and progressive enhancement without a framework runtime.

## Install or vendor

Build with Node 20 or newer and copy the generated `dist/` directory into the consumer, or vendor the `dist/` directory from an exact GitHub release archive. Keep its directory structure intact so font paths remain valid.

## What you get

CSS, fonts, schemas, templates, component metadata, and optional `sitekit.js` behavior for `kujo-light`, `kujo-dark`, `personal-dark`, and `bzby` themes.

## Boundaries

SiteKit remains `private: true`; npm publication is not part of v1. WCAG 2.2 AA is the source-component and tested-reference baseline, not certification of arbitrary downstream pages.

## Reference

See the [SiteKit repository](https://github.com/kujolang/site-kit).
