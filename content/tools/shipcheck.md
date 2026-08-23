---
title: ShipCheck
description: Scan release readiness and produce a gate report.
template: docs
section: Tools
nav_title: ShipCheck
order: 200
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: shipcheck
previous: /tools/concord/
next: /tools/packwrite/
tags: [tool, release, gates]
---


## Use it when…

You want a release checklist and gate report that makes missing proof visible.

## Interface overview

| Surface | What is available |
| --- | --- |
| Discovery | `scan` a repository for release-readiness evidence |
| Checklist | Generate the applicable release checks and missing items |
| Enforcement | `gate` with process-friendly exit semantics |
| Communication | JSON/YAML-style reports and release-note material |

## Main workflows

- Scan the current or selected repository to inventory available release proof.
- Review the generated checklist and close missing evidence deliberately.
- Run `gate` in CI to convert the catalog into an enforceable verdict.
- Generate release-note material from verified repository state, then edit it for users.

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
