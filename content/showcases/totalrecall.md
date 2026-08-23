---
title: TotalRecall
description: A local-first ingestion showcase for meetings, chat exports, Slack threads, and GitHub activity.
template: docs
section: Showcases
nav_title: TotalRecall
order: 50
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: showcase
source_repo: totalrecall
previous: /showcases/ssg/
next: /collections/
tags: [showcase, ingestion, knowledge]
---

## Use it when…

You want to normalize work artifacts into a stable model and write them to local destinations such as Strata, Markdown, static HTML, or a JSON index.

## Interface overview

| Surface | What is available |
| --- | --- |
| Providers | Fathom meetings, chat exports, Slack threads, and GitHub activity exports |
| Destinations | Strata, Markdown folders, static HTML, and a local JSON index |
| CLI | Provider import commands, `config validate`, `doctor`, and state inspect/prune |
| Reliability | Dry-run, plans, JSON reports, checkpoints, retries, deduplication, reconciliation, and audit logs |

## Main workflows

- Validate local configuration and destination health before importing anything.
- Preview a live or exported provider run with `--dry-run` and machine-readable reporting.
- Import into the selected destination, then repeat the command to verify idempotent duplicate protection.
- Inspect or prune checkpointed state deliberately when reconciling an existing destination.

## Local example

```bash
./scripts/totalrecall config validate
./scripts/totalrecall doctor --output json
./scripts/totalrecall chat-export import --dry-run
```

## What it proves

TotalRecall demonstrates provider-to-artifact-to-destination ingestion, filtering, mapping, deduplication, reconciliation, checkpoints, and idempotent local state.

For live Fathom ingestion use `fathom pull`; local sources use `chat-export import`, `slack import`, or `github-activity import`. Run `./scripts/totalrecall --help` for the full flag surface.

## Boundaries

Live Fathom and Strata destination checks require approved credentials or a running local destination. It is a local-first proof app, not a hosted sync service.

## Reference

See the [TotalRecall repository](https://github.com/robertdevore/totalrecall).
