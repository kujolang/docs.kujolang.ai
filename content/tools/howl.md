---
title: Howl
description: Render verified examples into Markdown, HTML, SVG, gallery, and caption assets.
template: docs
section: Tools
nav_title: Howl
order: 250
audience: developer
difficulty: beginner
status: local scope verified
version: current
scope: local-first
source_repo: howl
previous: /tools/ward/
next: /showcases/
tags: [tool, examples, publishing]
---


## Use it when…

Examples need deterministic cards, captions, galleries, or HTML artifacts that can be reviewed beside the source.

## Interface overview

| Surface | What is available |
| --- | --- |
| Setup | `howl init` scaffolds `howl.json` and starter examples without overwriting |
| Review | `validate`, `list`, `show <id>`, and `caption <id>` |
| Render | SVG, Markdown, HTML cards, and a static gallery under `dist/howl/` |
| Control | Manifest, output directory, selected format, and platform-bounded captions |

## Main workflows

- Define cards in `howl.json` and keep their referenced `.kujo` examples in source control.
- Validate the manifest and referenced files before rendering.
- Preview a card or generate a deterministic sharing caption by ID.
- Render all assets into a static output directory suitable for review or SSG publication.

## Five-minute example

```bash
howl validate
howl render
```

## What you get

Verified example assets in Markdown, HTML, SVG, gallery, and caption forms.

## How it fits

Use with [SSG](/showcases/ssg/) when examples need to become published documentation.

## Boundaries

Howl renders examples; it is not a scheduler or an AI caller.

## Reference

See the [Howl repository](https://github.com/kujolang/howl).
