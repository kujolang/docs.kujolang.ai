---
title: BB Kujo
description: Install the Kujo light and dark theme plugin for BB.
custom_url: bb-kujo
template: docs
section: Tools
nav_title: BB Kujo
order: 76
audience: developer
difficulty: beginner
status: released
version: 0.2.2
last_updated: 2026-10-21
scope: BB theme integration
source_repo: bb-kujo
tags: [tool, theme, integration]
---

## Install

BB Kujo 0.2.2 requires BB 0.43.x. Install through BB rather than Kennel:

```sh
bb plugin install git:https://github.com/kujolang/bb-kujo.git@v0.2.2 --yes
bb theme set plugin:bb-kujo:kujo
```

The package includes light and dark workspace themes, code and terminal colors, bundled Departure Mono and Tabler icons, and reduced-motion-aware decoration. Some third-party panels retain their own styling.

## Update or remove

For an existing installation, use BB's plugin update flow. Review the selected version before applying it. Remove the plugin with `bb plugin remove bb-kujo`.

## Release

The [0.2.2 GitHub release](https://github.com/kujolang/bb-kujo/releases/tag/v0.2.2) includes built frontend and server bundles. Generated assets, TypeScript checks, 14 contract tests and isolated Chromium checks passed on Node 26.12.1. These browser checks cover the theme fixture, not whole-application performance.

See the [repository guide](https://github.com/kujolang/bb-kujo/tree/v0.2.2) for development and known host limitations.
