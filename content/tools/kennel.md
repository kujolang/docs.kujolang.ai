---
title: Kennel
description: Manage deterministic manifests, dependencies, lockfiles, and trust policy.
template: docs
section: Tools
nav_title: Kennel
order: 20
audience: developer
difficulty: intermediate
status: local scope verified
version: current
last_updated: 2026-09-09
scope: local-first
source_repo: kennel
previous: /tools/kujo/
next: /tools/spec/
tags: [tool, packages, dependencies]
---


## Use it when…

Your project needs a dependency manifest, resolved lockfile, source policy, or trust decision that should be reviewable.

## Interface overview

| Surface | What is available |
| --- | --- |
| Project setup | `new`, `init`, and manifest generation |
| Dependencies | `add`, `install`, and frozen lockfile validation |
| Sources | Local file dependencies, static indexes, mirrors, and semver resolution |
| Policy | Source allowlists, trust rules, checksums, and lockfile integrity |

## Main workflows

- Initialize a package manifest and add local or indexed dependencies deliberately.
- Resolve dependencies into a reproducible lockfile, then use frozen mode in CI.
- Validate source and trust policy before accepting artifacts from a mirror or index.
- Keep Git development separate from release distribution; official release automation builds immutable registry artifacts.

## Five-minute example

```bash
kujo run kennel.kujo --interpreter -- init --name kennel-demo
kujo run kennel.kujo --interpreter -- add file:../some-local-package --alias some-local-package
kujo run kennel.kujo --interpreter -- install
kujo run kennel.kujo --interpreter -- validate
```

## What you get

An explicit manifest and lockfile-backed resolution result.

## How it fits

Read [Packages with Kennel](/learn/packages/) before choosing registry or file dependency behavior.

## Boundaries

The official static registry is available at [kennel.kujolang.ai](https://kennel.kujolang.ai/). The latest published client remains 1.0.1; merged native bootstrap and global tool commands belong to the unreleased 1.1.0 candidate. Use `kennel.toml` and `kennel.lock` for this client. Kujo 1.4.0 does not automatically upgrade Kennel. Accounts and third-party publishing are not available.

## Reference

See the [Kennel repository](https://github.com/kujolang/kennel) for manifest and trust policy details.
