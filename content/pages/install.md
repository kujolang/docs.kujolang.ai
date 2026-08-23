---
title: Install Kujo
description: Install the current stable CLI or build it from source, then verify the local toolchain.
custom_url: install
template: docs
section: Start here
nav_title: Install Kujo
order: 20
audience: developer
difficulty: beginner
status: stable
version: current
last_updated: 2026-08-23
previous: /start-here/
next: /quickstart/
prerequisites:
  - A supported macOS or Linux workstation
  - Git, Rust, and a writable terminal workspace
tags: [install, cli, stable]
---


Kujo `v1.0.1` is the current stable release. GitHub Releases provides prebuilt Linux x64, macOS x64/arm64, and Windows x64 archives, per-asset SHA-256 files, and a consolidated `checksums.txt`. Verify the checksum before placing the binary on `PATH`.

## Release install

Download the archive for your platform from the [Kujo v1.0.1 release](https://github.com/kujolang/kujo/releases/tag/v1.0.1), verify it against the matching SHA-256 file or `checksums.txt`, then install the `kujo` executable in a directory on `PATH`.

## Source install

```bash
git clone https://github.com/kujolang/kujo.git
cd kujo
cargo build --release
cargo install --path .
```

## Optional ecosystem install

The source-backed ecosystem installer can place the CLI and selected ecosystem profiles in your local user directory. It is intentionally separate from this docs site so every installed profile remains reviewable.

```bash
curl -fsSL https://raw.githubusercontent.com/kujolang/kujo/main/install.sh | bash -s -- --source
export PATH="$HOME/.local/bin:$PATH"
```

## Verify

```bash
kujo --version
kujo doctor --json
```

## Troubleshooting

- **Rust is missing:** install the stable Rust toolchain, then rerun `cargo build --release`.
- **`kujo` is not found:** add `$HOME/.local/bin` or Cargo's bin directory to PATH and open a new shell.
- **The wrong binary runs:** use `command -v kujo` and compare it with the path printed by `cargo install`.
- **Platform notes:** use the published release matrix for supported archives; build from source for other targets.
