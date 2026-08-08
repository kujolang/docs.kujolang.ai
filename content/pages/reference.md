---
title: Reference
description: Find CLI, language, standard-library, configuration, and generated source reference surfaces.
custom_url: reference
template: docs
section: Reference
nav_title: Reference
order: 70
audience: developer
difficulty: reference
status: generated-ready
version: current
next: /security/
tags: [reference, cli, generated]
---


Reference material is deliberately secondary to the first-time path. Use it when you know the concept or symbol you need to look up.

## Core surfaces

- **CLI reference:** `kujo --help`, `kujo doctor --json`, and command-specific help.
- **Language specification:** source-backed syntax, values, functions, modules, and errors.
- **Standard library:** the stable library and builtin reference generated from source.
- **Configuration:** `kujo.toml`, lockfiles, runtime capability flags, and docs-site configuration.
- **Generated reference:** DocGen output bridged into SSG Markdown under `content/reference/generated/`.

## Generate source reference

```bash
kujo docgen --output .docgen/output
```

The docs bridge turns the stable `docgen-summary/v1` result into reviewable Markdown. Treat generated files as outputs of the source tree, not as hand-authored narrative.

