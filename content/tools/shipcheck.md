---
title: ShipCheck
description: Scan release readiness and produce a gate report.
template: docs
section: Tools
nav_title: ShipCheck
order: 210
audience: developer
difficulty: intermediate
status: preview / experimental wording visible
version: current
scope: local-first
source_repo: shipcheck
next: /tools/fence/
tags: [tool, release, gates]
---

# ShipCheck

## Use it when…

You want a release checklist and gate report that makes missing proof visible.

## Five-minute example

```bash
kujo run shipcheck.kujo scan
kujo run shipcheck.kujo gate
```

## What you get

Release-readiness checks, a checklist, gate verdict, and release-note material.

## How it fits

Use [Concord](/tools/concord/) for drift and [Fence](/tools/fence/) for architecture boundaries.

## Boundaries

Preview/experimental wording stays visible. A gate report is not a production certification.

## Reference

See the [ShipCheck repository](https://github.com/kujolang/shipcheck).

