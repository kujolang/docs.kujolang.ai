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
scope: showcase
source_repo: totalrecall
previous: /showcases/ssg/
next: /collections/
tags: [showcase, ingestion, knowledge]
---

## Use it when…

You want to normalize work artifacts into a stable model and write them to local destinations such as Strata, Markdown, static HTML, or a JSON index.

## Local example

```bash
./scripts/totalrecall config validate
./scripts/totalrecall doctor --output json
./scripts/totalrecall chat-export import --dry-run
```

## What it proves

TotalRecall demonstrates provider-to-artifact-to-destination ingestion, filtering, mapping, deduplication, reconciliation, checkpoints, and idempotent local state.

## Boundaries

Live Fathom and Strata destination checks require approved credentials or a running local destination. It is a local-first proof app, not a hosted sync service.

## Reference

See the [TotalRecall repository](https://github.com/robertdevore/totalrecall).
