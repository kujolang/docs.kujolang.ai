---
title: Kujo
description: Write and run local-first Kujo programs.
template: docs
section: Tools
nav_title: Kujo
order: 10
audience: developer
difficulty: beginner
status: stable v1.2.3
version: 1.2.3
last_updated: 2026-09-05
scope: local-first
source_repo: kujo
next: /tools/kennel/
tags: [tool, foundation, language]
---


## Use it when…

You want to write a small program, check it, and run it with the same VM-first CLI path used by the rest of the ecosystem.

## Interface overview

| Surface | What is available |
| --- | --- |
| Run and inspect | `kujo run <file>`, `kujo check <file>`, `kujo doctor` |
| Test and document | `kujo test`, `kujo test-run <file>`, `kujo docgen <path>` |
| Projects and packages | `kujo init`, `kujo package-add`, `kujo package-install --frozen` |
| Agent Projects | `kujo agent new`, `kujo agent inspect`, `kujo agent run`, `kujo agent eval` |
| Runtime modes | VM by default; tree-walking interpreter fallback with `--interpreter` |

## Main workflows

- Run ordinary programs on the VM path and use `check` for validation without execution.
- Use `--untrusted` with explicit capability flags when a script should not inherit trusted access.
- Create reproducible package state with a manifest and `kujo.lock`, then verify it with frozen installs.
- Use `doctor` and JSON output when automation needs structured environment diagnostics.

## Five-minute example

```bash
kujo check hello.kujo
kujo run hello.kujo
kujo doctor --json
```

## What you get

A `kujo.toml` project, a source entry point, and explicit CLI output you can inspect or capture.

## How it fits

Start here, then add [Kennel](/tools/kennel/) when the project needs dependencies.

## Boundaries

Kujo `v1.2.3` is the current published stable release. The CLI now coordinates repository-owned Agent Projects, but their provider, runtime, retrieval, evaluation, observability, and package capabilities remain explicit ecosystem dependencies rather than hidden core services.

## Native runtime upgrades (unreleased)

[`kujo upgrade`](/upgrade/) is implemented on main but is not in v1.2.3. It will let supported standalone installations check or install official stable runtime binaries, with exact-version selection, JSON output, and retained backups. Package-manager installations use their original manager. Read the guide for bootstrap and recovery boundaries.

## Reference

Use `kujo --help`, `kujo agent --help`, `kujo doctor --json`, the [language basics](/learn/language-basics/) guide, the [Agent Projects guide](/build/owned-agent-projects/), and the [Kujo repository](https://github.com/kujolang/kujo).
