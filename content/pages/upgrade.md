---
title: Upgrade the Kujo runtime
description: Learn kujo upgrade syntax, read-only checks, JSON output, package-manager boundaries, and backup recovery. The command is implemented but unreleased.
custom_url: upgrade
template: docs
section: Start here
nav_title: Upgrade Kujo
order: 25
audience: developer
difficulty: intermediate
status: implemented — unreleased
version: source main
last_updated: 2026-09-05
scope: standalone runtime executable only
source_repo: kujo
previous: /install/
next: /quickstart/
prerequisites:
  - A Kujo release containing the native upgrade command
  - A supported standalone installation with a writable destination
tags: [upgrade, runtime, cli, installation]
---

`kujo upgrade` updates the running standalone Kujo executable from official GitHub release binaries. It does not update ecosystem tools, source snapshots, install profiles, package pins, or project dependencies.

## Availability and first upgrade

**As of September 5, 2026, the command is implemented on the Kujo repository's main branch but is not in the latest published runtime, [v1.2.3](https://github.com/kujolang/kujo/releases/tag/v1.2.3).** This guide documents that unreleased implementation. It does not announce a new runtime release.

Releases that predate the command cannot run it. First use your [existing installer](/install/) or original package manager to install a release containing `kujo upgrade`, once one is published. Check `kujo --version` and `kujo upgrade --help`. A local `kujo-upgrade` helper is a separate custom tool; this native command does not invoke or replace it.

## Check or install an update

Once your runtime includes the command, inspect the latest stable release without writing files:

```bash
kujo upgrade --check
kujo upgrade --check --json
```

Install the latest stable release:

```bash
kujo upgrade
```

Running the install command authorizes replacement without an interactive confirmation. It downloads a prebuilt archive, verifies its published SHA-256, and reports the actual executable destination. Supported targets are Linux x64 and arm64, macOS x64 and arm64, and Windows x64.

| Request | Behavior |
| --- | --- |
| `kujo upgrade` | Install the latest published stable release; preserve a newer local runtime. |
| `kujo upgrade VERSION` | Select one exact stable version, optionally prefixed by `v`. |
| `--check` | Resolve availability without installation, staging, backup, receipt, or lock-file writes. |
| `--json` | Write one success object to stdout; progress and errors go to stderr. |
| `--allow-downgrade` | Allow installation of an explicitly selected older version. |

`VERSION` must be an exact `MAJOR.MINOR.PATCH`. Ranges, prereleases, and build metadata are rejected. Same-version requests succeed without replacement. Missing releases, archives, or checksums fail without building from source.

These exact-version examples illustrate syntax; **v1.2.4 is not a published-release claim**:

```bash
kujo upgrade 1.2.4 --check
kujo upgrade v1.2.4
```

An intentional downgrade requires an explicit older target:

```bash
kujo upgrade 1.2.3 --allow-downgrade
```

Downgrading to a release without this command removes the ability to upgrade natively until you bootstrap again. `--check` can inspect an older target without downgrade permission. Latest never downgrades, even with `--allow-downgrade`.

## Package managers and executable paths

Use the original package manager for npm, Cargo, or other managed installations. Native installation refuses recognized managed paths and development `target` binaries, while `--check` can still report availability and installation kind. Examples below use `VERSION` as a placeholder for a published package version:

```bash
npm install --global @kujolang/kujo-runtime@VERSION
cargo install kujolang --version VERSION --locked --force
```

For project-local npm dependencies, use the project's package manager and scope. Recognized Homebrew, Nix, Scoop, Chocolatey, Snap, WinGet, WindowsApps, and system binary locations also receive a refusal instead of replacement.

The destination is the resolved path of the executable actually running. Invoking through a symlink preserves that link and updates its target. Legacy standalone binaries, including `~/.local/bin/kujo`, are recognized by executable name and the absence of known manager metadata. That heuristic is not proof of ownership; relocated package binaries or custom managers may evade recognition. Keep using their original manager.

## JSON output and exit codes

Successful checks, no-ops, and installations exit `0`. The object contains `current_version`, `target_version`, `status`, `changed`, `platform`, `destination`, `installation`, `upgrade_available`, and `backup`.

- `status` is `upgrade_available`, `up_to_date`, `newer_local`, `upgraded`, or `downgraded`.
- `changed` is true only after replacement. `upgrade_available` compares the target with the original installed version, including after installation.
- Versions omit the `v` prefix. `installation` is `standalone`, `npm`, `cargo`, `development`, or `managed`.
- `destination` is the resolved executable path. `backup` is null until successful replacement, then contains the retained prior executable's path.

Malformed arguments exit `2`; resolution, ownership, transport, verification, permission, and replacement failures exit `4`; an internal blocking-worker failure exits `6`. Errors use normal stderr diagnostics, with no failure JSON. See the [machine-readable contract](https://github.com/kujolang/kujo/blob/main/docs/CLI_MACHINE_READABLE_CONTRACTS.md#kujo-upgrade-version---json) for the complete example object.

## Verification and recovery

HTTPS requests, downloads, extraction, and staged version checks have time and size limits. The published checksum is verified before extraction or execution. This provides integrity through the official release channel, not independent artifact signing.

The replacement is staged beside the destination, and its `--version` must match the selected release. An OS lock prevents overlapping cooperating upgrades; the destination's identity and ownership are rechecked before replacement. The `.kujo-upgrade.lock` file remains after exit, but the OS releases its lock.

A successful upgrade retains a `kujo-backup-UUID` file beside the destination (`.exe` on Windows) and reports its path. Keep it until the new runtime is confirmed usable. To recover, stop Kujo processes and move the reported backup to the reported destination, preserving executable permissions on Unix.

Unix preserves a copy before renaming the replacement. Windows moves the running executable to its backup and then renames the staged replacement into place. Ordinary failures attempt rollback; **a crash between the two Windows renames can require manual recovery from the backup**. Universal crash atomicity and power-loss durability are not promised. Kujo does not elevate privileges automatically.

For archive restrictions, exact resource limits, ownership detection, and validation evidence, read the [source runtime-upgrade documentation](https://github.com/kujolang/kujo/blob/main/docs/RUNTIME_UPGRADE.md). For package and ecosystem changes, use their own [package workflows](/learn/packages/).
