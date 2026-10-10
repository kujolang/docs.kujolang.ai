---
title: Commerce
description: Add hosted checkout, verified payment events, and optional durable Square payment workflows to static or dynamic sites.
template: docs
section: Tools
nav_title: Commerce
order: 265
audience: developer
difficulty: intermediate
status: pre-1.0 release 0.5.0
version: 0.5.0
last_updated: 2026-10-10
scope: static and dynamic commerce with optional durable payment processing
source_repo: commerce
tags: [tool, commerce, ssg, web, square, stripe]
---

## Use it when…

A site needs validated products, hosted purchase links, a cart, or checkout that resolves trusted product data on the server. Start with Static Mode; add a runtime and durable processing only when needed.

## Install the released version

Requires Node.js 20 or later. Version 0.5.0 is published on GitHub with a package tarball, SBOM, and build provenance. npm registry publication is pending: the registry still serves 0.4.0 as checked on October 10, 2026. Install the exact release tarball:

```bash
npm install https://github.com/kujolang/commerce/releases/download/v0.5.0/kujolang-commerce-0.5.0.tgz
git clone --depth 1 --branch v1.1.0 https://github.com/kujolang/ssg vendor/ssg
npx kujo-commerce init --site .
npx kujo-commerce validate --site .
npx kujo-commerce build --site . --ssg vendor/ssg/build.kujo
npx kujo-commerce doctor --site .
```

Kujo SSG also needs the [Kujo runtime](/install/). Other generators can use Commerce's catalog/build functions and browser components; see [generic static integration](https://github.com/kujolang/commerce/blob/v0.5.0/docs/generic-static.md).

`init` defaults to Static Mode: pre-created HTTPS purchase links need no server or browser JavaScript. Use `init --mode hybrid` for a browser cart and dynamic checkout. The browser sends only SKU and quantity; the runtime resolves trusted prices and provider identifiers.

## What 0.5.0 adds

| Feature | Released scope |
| --- | --- |
| Durable processing | Optional PostgreSQL persistence, webhook receipts, worker leases, retries, dead letters, audited replay, and signed downstream events |
| Square payments | Scoped orders, direct payments, partial/full refunds, delayed capture/cancellation, and recovery for uncertain outcomes |
| Embedded checkout | Square SDK tokenization, server-controlled prices, transient tokens, duplicate-submit protection, and explicit restarts |
| Saved cards and subscriptions | Separate storage/recurring consent and supported static monthly plans with lifecycle actions |
| Invoices | Approved draft/publication/cancellation, deposits, and partial-payment observations; automatic saved-card charging remains disabled |
| Merchant connections | Encrypted Square OAuth tokens, one-use state, serialized refresh, location selection, and revocation |
| Optional integrations | Application fees, catalog/inventory tools, Terminal, and read-only dispute/payout reporting; off by default |

Hosted checkout, customer portals, and verified webhook normalization remain available. Run `npx kujo-commerce providers --json` for each adapter's exact capabilities.

## Upgrade from 0.4.0

1. Replace the dependency with the 0.5.0 tarball and retain the updated application lockfile.
2. Static and hosted-link users need no configuration changes. Existing v1 catalog, cart, checkout, and normalized-event contracts remain valid.
3. Runtime and custom-provider users should follow the [migration guide](https://github.com/kujolang/commerce/blob/v0.5.0/docs/migration-0.5.md). Preserve existing operation keys and v1 tables. New durable modules use additive persistence; deploy their migrations before receivers and workers.
4. If using Square subscriptions, review monthly cadence, trusted plan mapping, customer/card resolution, consent, and durable idempotency requirements. The Square protocol pins API version `2026-09-16`.
5. Validate the store, verify intended provider products, and exercise the enabled checkout/webhook and recovery paths before deployment.

## Deployment and acceptance

The maintainer has confirmed working Square and Stripe integrations. This does not establish acceptance of every provider or optional feature. Multi-seller OAuth, stored-card/recurring/invoice flows, fees, and Terminal still require the checks listed in the [acceptance status](https://github.com/kujolang/commerce/blob/v0.5.0/docs/square-implementation-status.md).

Dynamic deployments supply authentication, exact allowed origins, rate limits, secrets, durable storage, workers, backups, and monitoring. In-memory stores are test fixtures. Providers remain authoritative for payment outcomes; the application owns fulfillment policy. A successful browser redirect does not authorize fulfillment.

Use the [owned-payment example](https://github.com/kujolang/commerce/blob/v0.5.0/examples/owned-payments/README.md), [PostgreSQL topology](https://github.com/kujolang/commerce/blob/v0.5.0/examples/postgres-production/README.md), [production checklist](https://github.com/kujolang/commerce/blob/v0.5.0/docs/production-checklist.md), and [staging runbook](https://github.com/kujolang/commerce/blob/v0.5.0/docs/staging-runbook.md).

## Installation boundary

Commerce is a JavaScript/npm package, not a native Kennel package. Install the released tarball with npm; `kennel add commerce` is not a supported installation route. The public Kujo MCP catalog provides read-only release and installation guidance, not payment execution.

## Reference

- [Commerce 0.5.0 release](https://github.com/kujolang/commerce/releases/tag/v0.5.0)
- [Changelog](https://github.com/kujolang/commerce/blob/v0.5.0/CHANGELOG.md)
- [Compatibility policy](https://github.com/kujolang/commerce/blob/v0.5.0/docs/compatibility.md)
- [Owned payments](https://github.com/kujolang/commerce/blob/v0.5.0/docs/owned-payments.md)
- [Encrypted merchant connections](https://github.com/kujolang/commerce/blob/v0.5.0/docs/square-connections.md)
