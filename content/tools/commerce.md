---
title: Commerce
description: Add provider-agnostic catalog and checkout contracts to Kujo static sites.
template: docs
section: Tools
nav_title: Commerce
order: 265
audience: developer
difficulty: intermediate
status: preview 0.2.0
version: current
last_updated: 2026-08-23
scope: static-site integration
source_repo: commerce
tags: [tool, commerce, ssg, web]
---

## Use it when…

A static site needs validated product metadata, catalog assets, a browser cart, and a checkout boundary that resolves trusted product data on the server.

## Five-minute example

```bash
npm install github:kujolang/commerce#v0.2.0
git clone --depth 1 --branch v1.0.0 https://github.com/kujolang/ssg vendor/ssg
npx kujo-commerce validate --site .
npx kujo-commerce build --site . --ssg vendor/ssg/build.kujo
```

## What you get

Validated commerce metadata plus generated catalog and browser assets for an SSG output.

## Boundaries

The browser submits only SKU and quantity; the runtime checkout must resolve canonical pricing and product data. Payment-provider credentials and production checkout deployment remain integrator-owned.

## Reference

See the [Commerce repository](https://github.com/kujolang/commerce).
