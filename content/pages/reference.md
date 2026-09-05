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
status: stable source-backed links
version: current
last_updated: 2026-09-05
next: /security/
tags: [reference, cli, generated]
---


Reference material is deliberately secondary to the first-time path. Use it when you know the concept or symbol you need to look up.

## Core surfaces

- **Runtime upgrade (unreleased):** [`kujo upgrade` syntax, checks, JSON, and recovery](/upgrade/). Not included in v1.2.3.
- **CLI reference:** `kujo --help`, `kujo doctor --json`, and command-specific help.
- **Language specification:** source-backed syntax, values, functions, modules, and errors.
- **Standard library:** the stable library and builtin reference generated from source.
- **Configuration:** `kujo.toml`, lockfiles, runtime capability flags, and docs-site configuration.
- **Generated reference:** DocGen can emit HTML, Markdown, JSON, or all formats from a selected source path.

## Generate source reference

```bash
kujo docgen . --out-dir .docgen/output
```

DocGen emits the stable `docgen-summary/v1` result alongside the selected output formats. This site does not currently publish a generated API-reference subtree, so use the repository source references and generate exact-version output locally when symbol-level detail matters.
