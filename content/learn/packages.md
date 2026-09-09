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
last_updated: 2026-09-09
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

From a Kennel checkout, use its entrypoint with an explicit path:

```bash
kujo run /path/to/kennel/kennel.kujo --interpreter -- init --name my-project
kujo run /path/to/kennel/kennel.kujo --interpreter -- add file:../some-local-package --alias some-local-package
kujo run /path/to/kennel/kennel.kujo --interpreter -- install
kujo run /path/to/kennel/kennel.kujo --interpreter -- validate
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

As checked on September 9, the latest published Kennel client is **1.0.1**. The merged **1.1.0 candidate** contains the new native bootstrap and global tool-command work and awaits its own release. Kujo 1.4.0 supplies the compatible runtime primitives; upgrading Kujo does not release or install that Kennel candidate. Consult [Kennel's release notes](https://github.com/kujolang/kennel/releases) before relying on candidate commands.

Read [Kennel](/tools/kennel/) for local/source workflows and the [provider index](/ecosystem/providers/) for pinned provider packages. Third-party accounts, scoped publishing, and private-package services remain future work.
