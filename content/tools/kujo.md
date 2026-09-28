---
title: Kujo
description: Write and run local-first Kujo programs.
template: docs
section: Tools
nav_title: Kujo
order: 10
audience: developer
difficulty: beginner
status: stable v1.6.0
version: 1.6.0
last_updated: 2026-09-28
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

Kujo `v1.6.0` is the current published stable release. The CLI now coordinates repository-owned Agent Projects, but their provider, runtime, retrieval, evaluation, observability, and package capabilities remain explicit ecosystem dependencies rather than hidden core services.

## What changed in 1.6

Kujo 1.6.0 hardens closures and captured variables, generator/task/async behavior, and VM/interpreter parity. It fixes conditional early returns from loops in optimized VM bytecode, including nested control flow. Runtime measurement provides an observability foundation.

Durable review, checkpoints, restart/resume and external-effect replay control are implemented with companion tools such as Dispatch. Watchdog and RunLedger observe and correlate evidence; they do not become workflow authority.

### Experimental companion contracts

Wave C effect assurance remains **experimental beta, opt-in, required/deny within a bounded single-effect domain**, with alpha compatibility retained. SQLite, Workcell Git CAS and Ability application profiles supply effect-specific predicates; Dispatch owns replay admission.

Wave D generic interoperability and participant SDK APIs remain **experimental alpha** under a **trusted-local-host model**. Six participant forms, including independent TypeScript and Python implementations, have been exercised. Participant SDK packages remain **private/unpublished**. A correlation match is not permission to replay.

This release does not promise exactly-once execution, universal rollback, general machine-loss recovery, remote authenticated participant trust, multi-effect assurance or stable participant SDK APIs. Source-blind agent adopter rehearsal passed; human adopter usability remains post-release validation.

See the [1.6.0 release and checksums](https://github.com/kujolang/kujo/releases/tag/v1.6.0) and [publication evidence](https://github.com/kujolang/kujo/blob/main/docs/KUJO_1_6_RELEASE.md).

## Runtime maintenance

Use [`kujo upgrade`](/upgrade/) to update a supported standalone runtime from official stable binaries. `kujo upgrade --check --json` reports availability without changing files. Exact-version selection, downgrade policy, managed-install guidance, and recovery are documented in the guide. The command updates only the runtime; package-manager installations use their original manager.

## Native scripting

Kujo v1.6.0 supports isolated imports and native package-installer primitives, alongside bounded web-data processing and confined file publication. Read [How the runtime works](/learn/runtime/) for usage and Linux/macOS boundaries. Kennel remains a separate installation and release.

## Reference

Use `kujo --help`, `kujo agent --help`, `kujo doctor --json`, the [language basics](/learn/language-basics/) guide, the [Agent Projects guide](/build/owned-agent-projects/), and the [Kujo repository](https://github.com/kujolang/kujo).
