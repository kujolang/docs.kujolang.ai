---
title: Muzzle
description: Run noisy workflows quietly while preserving complete logs and summaries.
template: docs
section: Tools
nav_title: Muzzle
order: 150
audience: developer
difficulty: intermediate
status: local scope verified
version: 1.1.2
last_updated: 2026-10-12
scope: local-first
source_repo: muzzle
previous: /tools/leash/
next: /tools/runledger/
tags: [tool, workflows, logs]
---


## Use it when…

A trusted workflow produces too much console noise but its complete log and outcome still need to remain available.

## Interface overview

| Surface | What is available |
| --- | --- |
| Setup | `muzzle init` and workflow definitions under `.muzzle/workflows/` |
| Execution | `muzzle run <name>`, arguments, timeouts, dry-run, JSON, and verbose modes |
| Review | Workflow listing, complete logs, summaries, and report paths |
| Maintenance | Manifests, meaningful exit codes, loop mode, and `muzzle clean` |

## Main workflows

- Initialize repo-local workflow definitions and review the command each one will run.
- Execute a named workflow with compact output while preserving the complete log.
- Use `--dry-run` before risky or environment-specific workflows and `--json` in automation.
- Open the report or rerun with `--verbose` when the compact summary is not enough.

## Install or update

Muzzle **v1.1.2** is the current release. With [Kennel](/tools/kennel/) installed:

```bash
kennel tool install muzzle
# Update an existing unpinned installation:
kennel tool update muzzle
muzzle version
```

The version output starts with `Muzzle v1.1.2`. Use `kennel add muzzle` for a project dependency. Source installations can check out [v1.1.2](https://github.com/kujolang/muzzle/releases/tag/v1.1.2) and run `bash scripts/install.sh --prefix /absolute/prefix`; use `--force` only to replace an existing launcher intentionally.

## Five-minute example

```bash
muzzle init
muzzle run hello-bash --dry-run
muzzle run hello-bash --json
```

## What you get

Quiet terminal output, a complete log, a summary, and an exit status that remains meaningful to automation.

## How it fits

Use Muzzle around [PackWrite](/tools/packwrite/) or a bounded [Dispatch](/tools/dispatch/) run.

## Boundaries

Run trusted scripts only. Quiet output is not a sandbox. Raw logs can contain secrets; redaction applies to summaries. Serialize loop commands: concurrent loop writers are not coordinated.

Version 1.1.2 fixes unsafe initialization and cleanup paths, ambiguous options, invalid loop writes, and failure-excerpt handling. It preserves the CLI and versioned JSON contracts. New projects ignore all `.muzzle/state/`; existing projects should add `state/` to `.muzzle/.gitignore`. Existing files are never silently rewritten. Ignore rules do not untrack files already committed.

## Reference

See the [Muzzle repository](https://github.com/kujolang/muzzle).
