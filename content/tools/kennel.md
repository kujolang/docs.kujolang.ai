---
title: Kennel
description: Manage deterministic manifests, dependencies, lockfiles, and trust policy.
template: docs
section: Tools
nav_title: Kennel
order: 20
audience: developer
difficulty: intermediate
status: stable
version: 1.1.0
last_updated: 2026-09-13
scope: official registry and local development
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
| Sources | Official HTTPS registry, local file dependencies, custom static indexes, and SemVer resolution |
| Global tools | `tool install`, `update`, `list`, `run`, and `remove` |
| Client updates | `self update` |
| Policy | Source allowlists, trust rules, checksums, and lockfile integrity |

## Main workflows

- Initialize a package manifest and add local or indexed dependencies deliberately.
- Resolve dependencies into a reproducible lockfile, then use frozen mode in CI.
- Validate source and trust policy before accepting artifacts from a mirror or index.
- Keep Git development separate from release distribution; official release automation builds immutable registry artifacts.

## Five-minute example

Install [Kujo 1.4.0 or newer](/install/) first. On macOS or Linux:

```sh
curl -fsSL https://kennel.kujolang.ai/install.sh -o /tmp/kennel-install.sh
sh /tmp/kennel-install.sh
. "$HOME/.kennel/env"
kennel --version
kennel init --name kennel-demo
kennel add changebucket
kennel install
kennel tool install shipcheck
shipcheck --help
```

The installer adds a managed PATH entry to your shell profiles. No Git or Python is required for official package installation. Use `kennel self update` for the client and `kennel tool update` for installed unpinned tools.

## What you get

An explicit manifest and lockfile-backed resolution result.

## How it fits

Read [Packages with Kennel](/learn/packages/) before choosing registry or file dependency behavior.

## Boundaries

The official static registry is available at [kennel.kujolang.ai](https://kennel.kujolang.ai/). Kennel 1.1.0 provides the native bootstrap and global tool commands, using Kujo 1.4.0 or newer. Native Windows bootstrap is not supported. Use `kennel.toml` and `kennel.lock` for this client. Kujo 1.4.0 does not automatically upgrade Kennel. Accounts and third-party publishing are not available.

## Reference

See the [Kennel repository](https://github.com/kujolang/kennel) for manifest and trust policy details.
