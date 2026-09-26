---
title: ReaderSignal
description: Record privacy-bounded audience measurements, feedback, comparisons, and learning.
template: docs
section: Tools
nav_title: ReaderSignal
order: 325
audience: all
difficulty: advanced
status: production-oriented local scope
version: 0.3.0
last_updated: 2026-09-26
scope: local-first measurement
source_repo: readersignal
tags: [tool, analytics, privacy, learning]
---

## Use it when…

Audience learning needs immutable measurement snapshots, feedback, compatible comparisons, and evidence links. Statistical sampling, retention decisions, and adapter privacy checks are Kujo module APIs; the CLI operates on stored records.

## Install 0.3.0

```bash
git clone --branch v0.3.0 https://github.com/kujolang/readersignal.git
cd readersignal
export KUJO_BIN=/absolute/path/to/kujo
export PATH="$PWD/bin:$PATH"
readersignal --version --json
```

Requires POSIX Kujo 1.5.0 at revision
`d501c2c46c51718ee10c4434f6cf9750bbd81453` or a compatible newer build. The
version number alone does not guarantee the preview locking, paging, bounded
read, confined write, and directory-sync APIs. The validation script probes the
required capabilities. Existing 0.1.0 and 0.2.0 records remain readable under
contract 1.0.0; new records identify tool version 0.3.0. Stop older writers and
run `init` before using an existing state directory.

## Five-minute example

```bash
readersignal init --state .readersignal --json
readersignal snapshot --input fixtures/core.json --actor analyst --json
readersignal validate --json
readersignal export --output readersignal-export.json --json
```

## What you get

Bounded snapshots, feedback and comparison records, validated audit history, optional PressWire verification, portable exports, resumable query pages, journal-backed crash recovery, and trusted checkpoint backup/restore.

## Recovery and checkpoints

```bash
readersignal recovery-status --state .readersignal --id snapshot-example --json
readersignal recover --state .readersignal --id snapshot-example --actor operator --dry-run --json
readersignal recover --state .readersignal --id snapshot-example --actor operator --json
readersignal backup --state .readersignal --id snapshot-example --output /trusted-backups/snapshot-example.json --json
readersignal restore --state .readersignal-restored --id snapshot-example --input /trusted-backups/snapshot-example.json --actor operator --dry-run --json
readersignal restore --state .readersignal-restored --id snapshot-example --input /trusted-backups/snapshot-example.json --actor operator --json
readersignal validate --state .readersignal-restored --id snapshot-example --json
```

Use an actual record ID from `snapshot` or `report`; the example ID is a placeholder.
The external backup parent must already exist. A checkpoint preserves one original
record and its creation event, not all history, metadata, or attachments. Restore
refuses existing destination evidence and never invents missing history; provenance
must be trusted independently of checksums. Both checkpoint commands support
`--dry-run`. Resume an interrupted restore with `recover`.

Directory sync barriers order intent, record, history, and cleanup publication.
An uncertain durability error may follow a successful namespace change: inspect
and recover instead of blindly retrying a create. The guarantee assumes the OS,
filesystem, and hardware honor sync. The state root and its parents remain trusted.

## Boundaries

ReaderSignal does not claim causal attribution, hosted identity, or distributed multi-host coordination. External measurement providers remain optional adapters.

## Reference

See the [0.3.0 release](https://github.com/kujolang/readersignal/releases/tag/v0.3.0), [contracts](https://github.com/kujolang/readersignal/blob/v0.3.0/docs/contracts.md), and [durability and backup guide](https://github.com/kujolang/readersignal/blob/v0.3.0/docs/audits/durability-and-backups.md).
