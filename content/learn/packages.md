---
title: Packages with Kennel
description: Keep manifests, lockfiles, source policy, and trust decisions deterministic.
custom_url: packages
template: docs
section: Learn Kujo
nav_title: Packages with Kennel
order: 40
audience: developer
difficulty: intermediate
status: stable
version: current
last_updated: 2026-08-23
previous: /learn/capabilities/
next: /learn/editor-support/
tags: [packages, kennel, lockfiles]
---


`kujo.toml` describes a project and `kujo.lock` records the resolved dependency graph. Kennel keeps package indexes, file dependencies, trust policy, and source policy visible.

```bash
kujo package-add <package>
kujo package-install
kujo package-install --frozen
```

Use the frozen path in verification when the lockfile is part of the contract. Start with [Kennel](/tools/kennel/) when you need registry or dependency behavior details.

