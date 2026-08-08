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
scope: local-first
source_repo: kennel
previous: /tools/kujo/
next: /tools/spec/
tags: [tool, packages, dependencies]
---


## Use it when…

Your project needs a dependency manifest, resolved lockfile, source policy, or trust decision that should be reviewable.

## Five-minute example

```bash
kujo package-add example-package
kujo package-install
kujo package-install --frozen
```

## What you get

An explicit manifest and lockfile-backed resolution result.

## How it fits

Read [Packages with Kennel](/learn/packages/) before choosing registry or file dependency behavior.

## Boundaries

This is local/source workflow scope, not a managed package registry promise.

## Reference

See the [Kennel repository](https://github.com/kujolang/kennel) for manifest and trust policy details.

