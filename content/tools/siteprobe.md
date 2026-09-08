---
title: SiteProbe
description: Crawl websites in native Kujo with bounded same-origin requests, immutable artifacts, manifest verification, and deterministic comparisons.
template: docs
section: Tools
nav_title: SiteProbe
order: 270
audience: developer
difficulty: intermediate
status: released 0.3.0
version: 0.3.0
last_updated: 2026-09-07
scope: read-only website intelligence
source_repo: siteprobe
tags: [tool, web, crawl, evidence]
---

## Use it when…

A website needs a bounded, same-origin inventory of URLs, status, canonicals, metadata, structured data, links, sitemaps, and change evidence.

[SiteProbe 0.3.0](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0) is written in native Kujo.

## Install the qualified runtime

The release ZIPs are platform-qualified source packages, not standalone binaries. They require the exact Kujo revision recorded in `KUJO_REVISION`: [`2be1f04b89dbecd591ef1af0d68974c05586900e`](https://github.com/kujolang/kujo/tree/2be1f04b89dbecd591ef1af0d68974c05586900e). An older installed runtime may lack the bounded web-data primitives.

With Git and the Rust toolchain installed, build that revision beside SiteProbe. This Unix example starts in a directory without existing `siteprobe` or `kujo` checkouts:

```bash
git clone --branch v0.3.0 --depth 1 https://github.com/kujolang/siteprobe.git
git clone https://github.com/kujolang/kujo.git
git -C kujo checkout "$(cat siteprobe/KUJO_REVISION)"
cargo build --release --locked --manifest-path kujo/Cargo.toml
cd siteprobe
export KUJO_BIN="$(cd ../kujo && pwd)/target/release/kujo"
bash siteprobe doctor
bash siteprobe version
```

If you already have the qualified runtime, set `KUJO_BIN` to its absolute path. On Windows, point it at `kujo.exe` and use `siteprobe.cmd` or `siteprobe.ps1`. Downloaded ZIPs have matching SHA-256 files; verify them before extraction. Use `bash siteprobe` on Unix if extraction does not preserve executable permissions.

## Crawl and verify

```bash
bash siteprobe crawl https://example.com --out .siteprobe/example
bash siteprobe validate .siteprobe/example
bash siteprobe verify .siteprobe/example
bash siteprobe report .siteprobe/example
```

An immutable run contains versioned JSON/JSONL evidence, a bounded report, and a SHA-256 manifest. Runs can be signed with HMAC-SHA-256 and compared against a baseline. The existing `siteprobe.run/v1`, page, findings, and manifest contracts remain compatible.

## What changed in 0.3.0

- Native Kujo owns crawling, robots policy, extraction, analysis, validation, comparison, signing, and reporting.
- Bounded streaming supports large artifacts and compressed sitemaps without unbounded buffering.
- Isolated async workers perform overlapping requests at the configured concurrency while preserving ordered evidence and origin pacing.
- The pinned runtime fixes loop/exception scope cleanup, reduces measured regex/capture overhead, and enforces Windows no-replace publication.

The [release qualification](https://github.com/kujolang/siteprobe/blob/v0.3.0/docs/release-qualification-0.3.0.md) records passing Linux, macOS Intel/ARM64, and Windows checks. The [audit](https://github.com/kujolang/siteprobe/blob/v0.3.0/docs/audits/repository-hardening.md) includes native 10,000-page fixtures at concurrency 1, 4, 8, and 16; these measurements are not universal throughput guarantees.

## Boundaries

SiteProbe is read-only and GET-only. It blocks private and special-use network targets by default, enforces same-origin checks at every redirect, respects robots rules and bounded crawl/output budgets, and refuses an existing output path. Private-network access and robots overrides require explicit operator options.

It handles static and server-rendered HTML. It does not render JavaScript, submit forms, or replace browser verification with [Lens](/tools/lens/). Use [ContentGraph](/tools/contentgraph/) for relationship analysis and [SearchBridge](/tools/searchbridge/) for provider-backed search evidence.

## Reference

- [SiteProbe repository and command reference](https://github.com/kujolang/siteprobe/tree/v0.3.0)
- [Release downloads and checksums](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0)
- [SiteProbe ecosystem overview](https://kujolang.ai/ecosystem/siteprobe/)
