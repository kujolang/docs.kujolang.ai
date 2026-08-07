---
title: Install Kujo
description: Build or install the CLI, add it to PATH, and verify the local toolchain.
custom_url: install
template: docs
section: Start here
nav_title: Install Kujo
order: 20
audience: developer
difficulty: beginner
status: release-candidate onboarding
version: current
previous: /start-here/
next: /quickstart/
prerequisites:
  - A supported macOS or Linux workstation
  - Git, Rust, and a writable terminal workspace
tags: [install, cli, release-candidate]
---

# Install Kujo

The final public artifact status is still a visible boundary in this launch draft. Until release binaries, checksums, and a clean-machine download smoke are complete, use the source-backed release-candidate path.

## Source install

```bash
git clone https://github.com/kujolang/kujo.git
cd kujo
cargo build --release
cargo install --path .
```

## Optional ecosystem install

The installer can place the CLI and selected ecosystem profiles in your local user directory. It is intentionally separate from this docs site so profiles remain source-backed.

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
- **Platform notes:** treat this source path as the compatibility baseline until the release artifact matrix is published.

