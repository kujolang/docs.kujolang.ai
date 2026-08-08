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
scope: local-first
source_repo: lens
previous: /tools/casefile/
next: /tools/ward/
tags: [tool, browser, visual-qa]
---


## Use it when…

A browser surface needs deterministic flow, screenshot, accessibility, link, or visual baseline checks.

## Five-minute example

```bash
kujo run lens.kujo check --config .lens.toml
```

## What you get

Run artifacts, screenshots, accessibility findings, link checks, and an Agent Repair Brief when a flow fails.

## How it fits

Use after the SSG or application build and alongside [Fence](/tools/fence/) and [Scent](/tools/scent/).

## Boundaries

Browser proof is limited to the browsers, viewports, and flows actually run. This page remains preview-aware.

## Reference

See the [Lens repository](https://github.com/kujolang/lens).
