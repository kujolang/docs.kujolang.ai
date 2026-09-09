---
title: Commerce
description: Add provider-agnostic catalog and checkout contracts to Kujo static sites.
template: docs
section: Tools
nav_title: Commerce
order: 265
audience: developer
difficulty: intermediate
status: preview 0.4.0
version: 0.4.0
last_updated: 2026-09-09
scope: static-site integration
source_repo: commerce
tags: [tool, commerce, ssg, web]
---

## Use it when…

A static site needs validated product metadata, catalog assets, a browser cart, and a checkout boundary that resolves trusted product data on the server.

## Five-minute example

```bash
npm install @kujolang/commerce@0.4.0
git clone --depth 1 --branch v1.0.0 https://github.com/kujolang/ssg vendor/ssg
npx kujo-commerce init --site .
npx kujo-commerce validate --site .
npx kujo-commerce build --site . --ssg vendor/ssg/build.kujo
```

## What you get

Commerce 0.4.0 provides catalog validation, zero-runtime hosted purchase links, optional dynamic checkout and customer portals, and verified webhook normalization. `init` defaults to static mode; hybrid deployments explicitly add a runtime.

## Boundaries

The package remains pre-1.0 while provider sandbox evidence is completed; its v1 catalog, cart, and event wire formats have a compatibility policy. Providers remain authoritative for payments, inventory, tax, and fulfillment. For dynamic checkout, the browser submits only SKU and quantity; the runtime checkout must resolve canonical pricing and product data. Payment-provider credentials and production checkout deployment remain integrator-owned.

## Reference

See the [Commerce repository](https://github.com/kujolang/commerce).
