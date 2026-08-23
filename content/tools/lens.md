---
title: Lens
description: Review browser behavior with screenshots, accessibility, links, and flows.
template: docs
section: Tools
nav_title: Lens
order: 230
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: lens
previous: /tools/casefile/
next: /tools/ward/
tags: [tool, browser, visual-qa]
---


## Use it when…

A browser surface needs deterministic flow, screenshot, accessibility, link, or visual baseline checks.

## Interface overview

| Surface | What is available |
| --- | --- |
| Checks | Page load, screenshots, assertions, links, accessibility, performance, and crawls |
| Inspection | `lens inspect` for semantic browser state and safe selector evidence |
| Flows | Validated JSON flows with execution, recording, and walkthrough artifacts |
| Review | `lens-report.json`, screenshots, HTML reports, baselines, and Agent Repair Briefs |

## Main workflows

- Run a one-page check first, then opt into link, accessibility, or bounded crawl checks.
- Inspect the live page before authoring selectors for an interactive flow.
- Validate a flow definition before execution, then record proof for review.
- Save and compare baselines only when the browser and viewport are intentionally controlled.

## Five-minute example

```bash
lens check http://localhost:3000 --check-links --accessibility
lens flow flow.json --validate
```

## What you get

Run artifacts, screenshots, accessibility findings, link checks, and an Agent Repair Brief when a flow fails.

## How it fits

Use after the SSG or application build and alongside [Fence](/tools/fence/) and [Scent](/tools/scent/).

## Boundaries

Browser proof is limited to the browsers, viewports, and flows actually run. This page remains preview-aware.

## Reference

See the [Lens repository](https://github.com/kujolang/lens).
