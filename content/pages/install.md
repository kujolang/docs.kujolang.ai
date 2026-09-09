---
title: Install Kujo
description: Install Kujo v1.4.0 and the tool group you need, or build the CLI from source.
custom_url: install
template: docs
section: Start here
nav_title: Install Kujo
order: 20
audience: developer
difficulty: beginner
status: stable
version: 1.4.0
last_updated: 2026-09-09
previous: /start-here/
next: /quickstart/
prerequisites:
  - A supported macOS, Linux, or Windows workstation
  - A writable terminal workspace
tags: [install, cli, stable]
---


Kujo `v1.4.0` is the current stable release. On Linux and macOS, the public ecosystem installer selects the correct archive, verifies its SHA-256 checksum, and places the CLI and requested ecosystem tools under your user directory. On Windows, use the Windows archive from the release or the npm installation path described in the runtime repository.

## Install Kujo

```bash
curl -fsSL https://kujolang.ai/install.sh | bash
export PATH="$HOME/.local/bin:$PATH"
```

Use a focused group when you want Kujo and the tools for one job. For the Agent Development Platform:

```bash
curl -fsSL https://kujolang.ai/install.sh | bash -s -- --group agent
```

Run `curl -fsSL https://kujolang.ai/install.sh | bash -s -- --help` to review available groups and installer options before making changes. Direct archives and checksums remain available from the [Kujo v1.4.0 release](https://github.com/kujolang/kujo/releases/tag/v1.4.0).

## Upgrade an existing runtime

Use [`kujo upgrade`](/upgrade/) to update a standalone runtime, or `kujo upgrade --check --json` to inspect availability without changing files. The command is available in v1.3.0 and later. Users of v1.2.3 or older must first install a current release through the installer or original package manager.

Native upgrades replace only the runtime executable. Ecosystem tools and package pins keep their own update workflows. Read the guide for exact-version selection, managed installations, and backup recovery.

## Runtime requirements

The prebuilt Kujo CLI does not require Python, Node.js, or Rust to run ordinary Kujo programs. Source builds require Rust; npm installation requires Node.js. Individual tools may have additional requirements. Kujo v1.4.0 supplies the Linux/macOS runtime primitives for the upcoming native Kennel installer; that client has a separate release and installation step.

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

An agent-focused install can be verified with `kujo doctor agent`. Continue to [Repository-owned Agent Projects](/build/owned-agent-projects/) to create and run one locally.

## Troubleshooting

- **Rust is missing during a source build:** install the stable Rust toolchain, then rerun `cargo build --release`.
- **`kujo` is not found:** add `$HOME/.local/bin` or Cargo's bin directory to PATH and open a new shell.
- **The wrong binary runs:** use `command -v kujo` and compare it with the path printed by `cargo install`.
- **Platform notes:** use the published release matrix for supported archives; build from source for other targets.
