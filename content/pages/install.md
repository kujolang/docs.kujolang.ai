---
title: Install Kujo
description: Install Kujo v1.1.0 and the tool group you need, or build the CLI from source.
custom_url: install
template: docs
section: Start here
nav_title: Install Kujo
order: 20
audience: developer
difficulty: beginner
status: stable
version: 1.1.0
last_updated: 2026-08-30
previous: /start-here/
next: /quickstart/
prerequisites:
  - A supported macOS, Linux, or Windows workstation
  - A writable terminal workspace
tags: [install, cli, stable]
---


Kujo `v1.1.0` is the current stable release. The public installer selects the
correct archive for your platform, verifies its SHA-256 checksum, and places the
CLI and requested ecosystem tools under your user directory.

## Install Kujo

```bash
curl -fsSL https://kujolang.ai/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"
```

Use a focused group when you want Kujo and the tools for one job. For the Agent
Development Platform:

```bash
curl -fsSL https://kujolang.ai/install.sh | bash -s -- --group agent
```

Run `curl -fsSL https://kujolang.ai/install.sh | bash -s -- --help` to review
available groups and installer options before making changes. Direct archives
and checksums remain available from the [Kujo v1.1.0 release](https://github.com/kujolang/kujo/releases/tag/v1.1.0).

## Source install

```bash
git clone https://github.com/kujolang/kujo.git
cd kujo
cargo build --release
cargo install --path .
```

## Verify

```bash
kujo --version
kujo doctor --json
```

An agent-focused install can be verified with `kujo doctor agent`. Continue to
[Repository-owned Agent Projects](/build/owned-agent-projects/) to create and
run one locally.

## Troubleshooting

- **Rust is missing during a source build:** install the stable Rust toolchain, then rerun `cargo build --release`.
- **`kujo` is not found:** add `$HOME/.local/bin` or Cargo's bin directory to PATH and open a new shell.
- **The wrong binary runs:** use `command -v kujo` and compare it with the path printed by `cargo install`.
- **Platform notes:** use the published release matrix for supported archives; build from source for other targets.
