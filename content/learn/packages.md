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
last_updated: 2026-09-13
previous: /learn/capabilities/
next: /learn/editor-support/
tags: [packages, kennel, lockfiles]
---


Kujo's built-in package commands and the separate Kennel client have different manifests. Choose one deliberately; their lockfiles are not interchangeable.

| Tool | Manifest | Lockfile | Purpose |
| --- | --- | --- | --- |
| Kujo built-in package commands | `kujo.toml` | `kujo.lock` | Project metadata and the runtime's dependency snapshot |
| Kennel | `kennel.toml` | `kennel.lock` | Dependency resolution, installation, source policy, and trust verification |

## Kennel project dependencies

Install the separate [Kennel client](/tools/kennel/), then run:

```bash
kennel init --name my-project
kennel add changebucket
kennel install
kennel validate
```

Commit the manifest and lockfile. Follow the pinned client's frozen-install and trust policy when reproducing a build.

## Built-in runtime commands

```bash
kujo package-add <package>
kujo package-install
kujo package-install --frozen
```

These commands manage the runtime's `kujo.toml` / `kujo.lock` contract. They do not install or update the separate Kennel client.

## Official registry and release status

[The official Kennel registry](https://kennel.kujolang.ai/) distributes immutable first-party package releases. GitHub remains the development and release source. Public package reads need no account.

Kennel **1.1.0** is the native registry client and requires **Kujo 1.4.0 or newer**. Install Kujo, install Kennel, then use package names such as `kennel add changebucket` or exact versions such as `kennel add changebucket@1.0.0`. The resulting lockfile records the exact version and verified artifact. Local development still supports `kennel add file:../some-local-package --alias some-local-package`.

Read [Kennel](/tools/kennel/) for local/source workflows and the [provider index](/ecosystem/providers/) for pinned provider packages. Third-party accounts, scoped publishing, and private-package services remain future work.
