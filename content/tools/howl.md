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
version: 1.2.0
last_updated: 2026-10-16
scope: local-first
source_repo: howl
previous: /tools/ward/
next: /tools/paperclip/
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

## Install Howl 1.2.0

Howl requires Kujo 1.3.1 or newer. For global installation, use Kennel 1.1.0
or newer and its supported Kujo runtime:

```bash
kennel tool install howl@1.2.0
howl version
```

Use `kennel add howl@1.2.0` for a project dependency. The repository launcher
also supports an explicit `KUJO` executable.

## Five-minute example

```bash
howl init
howl validate
howl render
```

## Input and output guarantees

Manifests must be regular JSON files; symlinks to regular manifests are supported.
Examples and assets must remain inside the manifest directory, including symlink
targets. The `index` ID is reserved for the gallery. Output targets cannot be
symlinks or collide with input files.

Changed artifacts are replaced atomically; identical output retains its mtime.
Forced init checks both destinations before replacing an example. A render is
atomic per file, not a multi-file transaction; directories and ancestors must
remain trusted.

Metadata commands avoid loading unused example/asset contents. Rendering loads
one card at a time, and SVG wrapping stops once overflow is proven. Standard SVG
skips unused assets; transparent social SVG skips its background. Full public
card models retain requested assets.

For IDs beginning with `--`, end option parsing first:

```bash
howl show -- --format
howl caption --platform x -- --format
```

## What you get

Reviewable example assets in Markdown, HTML, SVG, gallery, and caption forms.

## How it fits

Use with [SSG](/showcases/ssg/) when examples need to become published documentation.

## Boundaries

Howl renders examples; it is not a scheduler or an AI caller.

## Reference

See the [Howl 1.2.0 release](https://github.com/kujolang/howl/releases/tag/v1.2.0)
and [Howl repository](https://github.com/kujolang/howl).
