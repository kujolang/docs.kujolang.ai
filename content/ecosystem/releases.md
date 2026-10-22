---
title: Ecosystem releases
description: Current published Kujo ecosystem versions, recent source changes, and explicit installation boundaries.
custom_url: releases
template: docs
section: Ecosystem
nav_title: Ecosystem releases
order: 15
audience: all
difficulty: beginner
status: dated release inventory
version: current
last_updated: 2026-10-21
tags: [ecosystem, releases, versions, installation]
---

This inventory was checked against all **86 public kujolang repositories on September 9, 2026**, with Scout and ReaderSignal refreshed from their September 26 releases, the first companion batch from September 28, Workcell/Ability/MCP and Dispatch from September 29, SSG from October 12, Kujo from October 4, Tribunal from October 7, Commerce from October 10, and AI SDK and Agents SDK from October 13. Product releases, protocol versions, repository tags, and the docs site's version are separate. The table lists the latest non-draft, non-prerelease **GitHub Release** found for each package; it does not claim that every current default-branch feature exists in that release.

## Source 0.1.0 — October 14, 2026

[Source 0.1.0](https://github.com/kujolang/source/releases/tag/v0.1.0) is the first public MIT release of the Git review and evidence platform. Its Node.js server, CLI and browser UI connect agent proposals to authorized decisions. Install through Git and npm; Source is not a Kennel package. The [Source guide](/tools/source/) covers local demos, Cloudflare integration and experimental deployment boundaries.

## October 21 companion updates

Ability 1.3.0, AI Chat 1.3.1, CaseFile 1.0.2, Concord 1.1.2, ShipCheck 1.0.2, RunLedger 1.2.1, PatchBrief 1.0.3, Spec 1.0.2, SSG 1.2.1, Source 0.1.1, Muzzle 1.1.3 and Watchdog 1.2.2 are published. The table and linked guides identify the current versions. Each project retains its documented installation and deployment boundaries.

## Start here

Install [Kujo 1.8.2](/install/) for the current runtime. A standalone binary runs ordinary Kujo programs without Python, Node.js, or Rust. Individual applications and tools retain their own dependencies, supported platforms, runtime pins, and update procedures.

[Kennel's official registry](https://kennel.kujolang.ai/) distributes first-party package artifacts. Kennel 1.2.1 is published separately; Kujo 1.8.2 does not change its version or historical package artifacts. See [package workflows](/learn/packages/) before assuming that upgrading Kujo also updates Kennel or other tools.

## What changed in 1.8

Kujo 1.8.0 shares optional program analysis between CLI checking and the LSP, improves gradual inference and editor information, adds struct generator methods, and retains one measured generator-resume optimization. It strengthens VM/interpreter and optimizer-safety evidence without changing the v1 language contract.

Durable review, checkpoints, restart/resume and external-effect replay control are implemented with companion tools such as Dispatch. Watchdog and RunLedger observe and correlate evidence; they do not become workflow authority.

### Experimental companion contracts

Wave C effect assurance remains **experimental beta, opt-in, required/deny within a bounded single-effect domain**, with alpha compatibility retained. SQLite, Workcell Git CAS and Ability application profiles supply effect-specific predicates; Dispatch owns replay admission.

Wave D generic interoperability and participant SDK APIs remain **experimental alpha** under a **trusted-local-host model**. Six participant forms, including independent TypeScript and Python implementations, have been exercised. Participant SDK packages remain **private/unpublished**. A correlation match is not permission to replay.

This release does not promise exactly-once execution, universal rollback, general machine-loss recovery, remote authenticated participant trust, multi-effect assurance or stable participant SDK APIs. Source-blind agent adopter rehearsal passed; human adopter usability remains post-release validation.

See the [1.8.0 release and checksums](https://github.com/kujolang/kujo/releases/tag/v1.8.0), [release-readiness evidence](https://github.com/kujolang/kujo/blob/v1.8.0/docs/KUJO_1_8_RELEASE_READINESS.md), and [publication record](https://github.com/kujolang/kujo/blob/main/release/kujo-1.8.0-publication.json).

## Published package releases

| Package | Latest published release | Published (UTC) |
| --- | --- | --- |
| [ability](https://github.com/kujolang/ability) | [v1.3.0](https://github.com/kujolang/ability/releases/tag/v1.3.0) | 2026-10-21 |
| [agents-sdk](https://github.com/kujolang/agents-sdk) | [v1.1.3](https://github.com/kujolang/agents-sdk/releases/tag/v1.1.3) | 2026-10-13 |
| [ai-chat](https://github.com/kujolang/ai-chat) | [v1.3.1](https://github.com/kujolang/ai-chat/releases/tag/v1.3.1) | 2026-10-21 |
| [ai-sdk](https://github.com/kujolang/ai-sdk) | [v1.2.0](https://github.com/kujolang/ai-sdk/releases/tag/v1.2.0) | 2026-10-13 |
| [anthropic](https://github.com/kujolang/anthropic) | [v0.1.2](https://github.com/kujolang/anthropic/releases/tag/v0.1.2) | 2026-08-27 |
| [assetworks](https://github.com/kujolang/assetworks) | [v0.2.0](https://github.com/kujolang/assetworks/releases/tag/v0.2.0) | 2026-08-14 |
| [bb-kujo](https://github.com/kujolang/bb-kujo) | [v0.2.2](https://github.com/kujolang/bb-kujo/releases/tag/v0.2.2) | 2026-10-21 |
| [bluepencil](https://github.com/kujolang/bluepencil) | [v0.2.0](https://github.com/kujolang/bluepencil/releases/tag/v0.2.0) | 2026-08-14 |
| [casefile](https://github.com/kujolang/casefile) | [v1.0.2](https://github.com/kujolang/casefile/releases/tag/v1.0.2) | 2026-10-21 |
| [changebucket](https://github.com/kujolang/changebucket) | [v1.1.0](https://github.com/kujolang/changebucket/releases/tag/v1.1.0) | 2026-09-22 |
| [cms](https://github.com/kujolang/cms) | [v1.2.0](https://github.com/kujolang/cms/releases/tag/v1.2.0) | 2026-10-12 |
| [cms-contact-form](https://github.com/kujolang/cms-contact-form) | [v1.0.0](https://github.com/kujolang/cms-contact-form/releases/tag/v1.0.0) | 2026-08-29 |
| [cms-example](https://github.com/kujolang/cms-example) | [v1.1.0](https://github.com/kujolang/cms-example/releases/tag/v1.1.0) | 2026-08-30 |
| [cms-field-notes-theme](https://github.com/kujolang/cms-field-notes-theme) | [v1.0.2](https://github.com/kujolang/cms-field-notes-theme/releases/tag/v1.0.2) | 2026-08-29 |
| [commerce](https://github.com/kujolang/commerce) | [v0.5.0](https://github.com/kujolang/commerce/releases/tag/v0.5.0) | 2026-10-10 |
| [concord](https://github.com/kujolang/concord) | [v1.1.2](https://github.com/kujolang/concord/releases/tag/v1.1.2) | 2026-10-21 |
| [contentgraph](https://github.com/kujolang/contentgraph) | [v0.3.0](https://github.com/kujolang/contentgraph/releases/tag/v0.3.0) | 2026-08-13 |
| [crud-api](https://github.com/kujolang/crud-api) | [v1.0.1](https://github.com/kujolang/crud-api/releases/tag/v1.0.1) | 2026-10-14 |
| [dispatch](https://github.com/kujolang/dispatch) | [v1.4.1](https://github.com/kujolang/dispatch/releases/tag/v1.4.1) | 2026-10-22 |
| [dossier](https://github.com/kujolang/dossier) | [v0.2.0](https://github.com/kujolang/dossier/releases/tag/v0.2.0) | 2026-08-14 |
| [eval](https://github.com/kujolang/eval) | [v1.1.0](https://github.com/kujolang/eval/releases/tag/v1.1.0) | 2026-10-14 |
| [fence](https://github.com/kujolang/fence) | [v1.1.0](https://github.com/kujolang/fence/releases/tag/v1.1.0) | 2026-10-14 |
| [galleypack](https://github.com/kujolang/galleypack) | [v0.2.0](https://github.com/kujolang/galleypack/releases/tag/v0.2.0) | 2026-08-14 |
| [howl](https://github.com/kujolang/howl) | [v1.2.0](https://github.com/kujolang/howl/releases/tag/v1.2.0) | 2026-10-16 |
| [kennel](https://github.com/kujolang/kennel) | [v1.2.1](https://github.com/kujolang/kennel/releases/tag/v1.2.1) | 2026-10-21 |
| [kujo](https://github.com/kujolang/kujo) | [v1.8.2](https://github.com/kujolang/kujo/releases/tag/v1.8.2) | 2026-10-19 |
| [kujo-agents](https://github.com/kujolang/kujo-agents) | [v1.4.0](https://github.com/kujolang/kujo-agents/releases/tag/v1.4.0) | 2026-09-07 |
| [kujo-opencode](https://github.com/kujolang/kujo-opencode) | [v0.2.1](https://github.com/kujolang/kujo-opencode/releases/tag/v0.2.1) | 2026-10-21 |
| [kujo-pi](https://github.com/kujolang/kujo-pi) | [v1.2.1](https://github.com/kujolang/kujo-pi/releases/tag/v1.2.1) | 2026-10-21 |
| [kujo-skills](https://github.com/kujolang/kujo-skills) | [v0.7.0](https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0) | 2026-09-08 |
| [kujo-workflows](https://github.com/kujolang/kujo-workflows) | [v0.6.0](https://github.com/kujolang/kujo-workflows/releases/tag/v0.6.0) | 2026-09-07 |
| [lens](https://github.com/kujolang/lens) | [v1.1.1](https://github.com/kujolang/lens/releases/tag/v1.1.1) | 2026-10-22 |
| [mcp](https://github.com/kujolang/mcp) | [v1.3.2](https://github.com/kujolang/mcp/releases/tag/v1.3.2) | 2026-10-14 |
| [muzzle](https://github.com/kujolang/muzzle) | [v1.1.3](https://github.com/kujolang/muzzle/releases/tag/v1.1.3) | 2026-10-21 |
| [ollama](https://github.com/kujolang/ollama) | [v0.1.10](https://github.com/kujolang/ollama/releases/tag/v0.1.10) | 2026-08-27 |
| [packwrite](https://github.com/kujolang/packwrite) | [v1.1.1](https://github.com/kujolang/packwrite/releases/tag/v1.1.1) | 2026-10-13 |
| [paperclip](https://github.com/kujolang/paperclip) | [v0.2.1](https://github.com/kujolang/paperclip/releases/tag/v0.2.1) | 2026-10-21 |
| [patchbrief](https://github.com/kujolang/patchbrief) | [v1.0.3](https://github.com/kujolang/patchbrief/releases/tag/v1.0.3) | 2026-10-21 |
| [presswire](https://github.com/kujolang/presswire) | [v0.2.0](https://github.com/kujolang/presswire/releases/tag/v0.2.0) | 2026-08-14 |
| [rag](https://github.com/kujolang/rag) | [v1.0.0](https://github.com/kujolang/rag/releases/tag/v1.0.0) | 2026-08-08 |
| [readersignal](https://github.com/kujolang/readersignal) | [v0.3.0](https://github.com/kujolang/readersignal/releases/tag/v0.3.0) | 2026-09-26 |
| [redact](https://github.com/kujolang/redact) | [v1.0.0](https://github.com/kujolang/redact/releases/tag/v1.0.0) | 2026-08-09 |
| [relay](https://github.com/kujolang/relay) | [v1.1.0](https://github.com/kujolang/relay/releases/tag/v1.1.0) | 2026-08-27 |
| [runledger](https://github.com/kujolang/runledger) | [v1.2.1](https://github.com/kujolang/runledger/releases/tag/v1.2.1) | 2026-10-21 |
| [scent](https://github.com/kujolang/scent) | [v1.1.0](https://github.com/kujolang/scent/releases/tag/v1.1.0) | 2026-10-14 |
| [scout](https://github.com/kujolang/scout) | [v1.1.0](https://github.com/kujolang/scout/releases/tag/v1.1.0) | 2026-09-26 |
| [searchbridge](https://github.com/kujolang/searchbridge) | [v1.0.2](https://github.com/kujolang/searchbridge/releases/tag/v1.0.2) | 2026-10-22 |
| [shipcheck](https://github.com/kujolang/shipcheck) | [v1.0.2](https://github.com/kujolang/shipcheck/releases/tag/v1.0.2) | 2026-10-21 |
| [site-kit](https://github.com/kujolang/site-kit) | [v1.1.1](https://github.com/kujolang/site-kit/releases/tag/v1.1.1) | 2026-10-22 |
| [siteprobe](https://github.com/kujolang/siteprobe) | [v0.3.0](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0) | 2026-09-07 |
| [spec](https://github.com/kujolang/spec) | [v1.0.2](https://github.com/kujolang/spec/releases/tag/v1.0.2) | 2026-10-21 |
| [ssg](https://github.com/kujolang/ssg) | [v1.2.1](https://github.com/kujolang/ssg/releases/tag/v1.2.1) | 2026-10-21 |
| [storydesk](https://github.com/kujolang/storydesk) | [v0.2.0](https://github.com/kujolang/storydesk/releases/tag/v0.2.0) | 2026-08-14 |
| [tribunal](https://github.com/kujolang/tribunal) | [v1.0.2](https://github.com/kujolang/tribunal/releases/tag/v1.0.2) | 2026-10-07 |
| [versionseal](https://github.com/kujolang/versionseal) | [v0.2.0](https://github.com/kujolang/versionseal/releases/tag/v0.2.0) | 2026-08-14 |
| [watchdog](https://github.com/kujolang/watchdog) | [v1.2.2](https://github.com/kujolang/watchdog/releases/tag/v1.2.2) | 2026-10-21 |
| [workcell](https://github.com/kujolang/workcell) | [v1.2.0](https://github.com/kujolang/workcell/releases/tag/v1.2.0) | 2026-09-29 |

The Kujo Pi row was refreshed on September 26, 2026. Other entries retain their individually documented inventory dates.

## Recent changes worth checking

- **Kujo Pi 1.1.0:** approval-gated Ability tools, opt-in Watchdog v2 metadata, bounded telemetry and artifact inspection, and receipt-failure recovery. Read [Kujo Pi](/tools/kujo-pi/).

- **AI Chat 1.3.0:** live code review, durable supervision, isolated worktrees, scoped MCP connections, an attention inbox, a command palette, and persistent chat tabs. Follow its Node, storage, permission, and worktree upgrade requirements; the historical eight-hour soak remains incomplete. Read [AI Chat](/showcases/ai-chat/).
- **Workcell 1.2.0:** Docker/Podman execution and failure preservation, with Git assurance/process correlation experimental and remote adapters still alpha. Use the package's qualified Kujo 1.6.0 runtime. Read [Workcell](/tools/workcell/).
- **SiteProbe 0.3.0:** native Kujo product commands and platform-qualified source archives; its test tooling can still require Python. Read [SiteProbe](/tools/siteprobe/).
- **Skills 0.7.0, Workflows 0.6.0, Agents 1.4.0:** 135 skills, 44 local workflows, and canonical VideoOps tools and schemas. Live media permission and provider limits remain explicit. Read [skills](/collections/skills/) and [workflows](/collections/workflows/).
- **Commerce 0.5.0:** adds optional PostgreSQL processing, Square payments/refunds, embedded checkout, billing workflows, OAuth connections, and recovery. Static hosted links remain lightweight. Install the GitHub tarball while npm publication is pending; advanced features retain their acceptance gates. Read [Commerce](/tools/commerce/).
- **Scout 1.1.0:** bounded rooted reads, aggregate limits, security exports, deterministic performance and labeled-corpus gates, stable CI diagnostics, and native Windows contract coverage. It requires Kujo 1.5.0 or newer. Read [Scout](/tools/scout/).
- **Watchdog 1.1.0:** canonical v2 telemetry, JSONL/OTLP projections, Connected Sources management, and named proxy-profile changes that apply to new requests without restart. Read [Watchdog](/tools/watchdog/).
- **Agents SDK 1.1.2 and RunLedger 1.2.0:** released lifecycle telemetry and evidence-correlation work accompanies Kujo 1.6. RAG and Eval retain separately documented source work beyond their published releases.
- **Dispatch 1.3.0:** durable review, policy-preserving resume and restart-safe control with Kujo 1.6.0. Wave C beta and Wave D alpha remain experimental; a separate selected-effect operator API does not authorize parent replay. Read [Dispatch](/tools/dispatch/).
- **CaseFile, Fence, Scent, ShipCheck, Howl, Redact, and Dossier:** recent source hardening has its own verification evidence. Pin the reviewed source when adopting those fixes; an unchanged release archive does not acquire later commits.

## Tags and source-only packages

The [25-provider index](/ecosystem/providers/) records pinned source tags and driver compatibility. Many provider tags have no corresponding GitHub Release. Their tag-based installation instructions remain valid; do not substitute an older GitHub Release solely because it has a release page. AI SDK's documented 1.1.0 provider baseline is likewise distinct from its latest GitHub Release.

Kujo Pi 1.1.0 is published on GitHub and npm; install `npm:@kujolang/kujo-pi@1.1.0` through Pi. See [Kujo Pi](/tools/kujo-pi/) for its separate host and runtime requirements. Repositories without a GitHub Release, including infrastructure and some application sources, are not assigned invented release versions here. Private projects retain their documented access boundaries.

## Agent discovery

The public [Kujo MCP catalog](https://mcp.kujolang.ai/mcp) exposes read-only project, skill, workflow, and installer guidance. It is separate from the MCP framework and from private application gateways. Refreshes publish a reviewed static snapshot; they do not execute installer commands or grant application permissions.

## Kujo 1.8 runtime and companion delivery

Kujo 1.8 does not republish or silently upgrade companion tools. RunLedger 1.2.0, AI SDK 1.2.0 and Agents SDK 1.1.2 are published independently. AI SDK 1.2.0 adds state persistence, strict accounting, and transport controls; its release notes distinguish offline verification from live-provider evidence. Workcell, Ability and MCP 1.2.0 distribute the controlled-execution cohort while retaining experimental assurance/interoperability boundaries. Dispatch 1.3.0 completes this controller release cohort with the same experimental boundaries. Stop older workers and follow its backup/upgrade instructions before changing persisted-state versions.

SSG 1.2.0 requires pinned esbuild 0.28.2 for minified builds and adds explicit private-image opt-in and a separate DocGen repository-CI budget. See the [SSG upgrade notes](/showcases/ssg/#upgrade-and-integration-notes).

## Agents SDK 1.1.3

The October 13 patch hardens approval, handoff, state, storage, retry, and token-accounting behavior while preserving public contracts. It supersedes 1.1.2 for new installations. See the [Agents SDK guide](/tools/agents-sdk/) for compatibility notes and the remaining cost-unit conversion limit.

## October 14 capability updates

PatchBrief 1.0.2, CaseFile 1.0.1, MCP 1.3.2, ShipCheck 1.0.1, Scent 1.1.0, Kennel 1.2.0, Fence 1.1.0, Concord 1.1.1, Eval 1.1.0, CRUD API 1.0.1 and Dispatch 1.4.0 are published. Dispatch 1.4.0 requires Kujo 1.8.1. RAG 1.1.0 remains an unpublished candidate pending required review evidence; local functional tests do not certify hosted deployments.

## Kujo OpenCode launch — 2026-10-18

[Kujo OpenCode 0.2.0](/tools/kujo-opencode/) is published on npm and GitHub. It brings six specialists, 62 supported capabilities, native approvals and inspectable receipts to OpenCode 2. Registry installation and upgrade checks passed. Native host checks cover Linux, macOS and Windows; live specialist evidence uses macOS and ChatGPT. Install through npm, not Kennel.

## Kujo 1.8.2 maintenance release

[Kujo 1.8.2](https://github.com/kujolang/kujo/releases/tag/v1.8.2) resolves ZIP security advisories and retired YAML, credential-store and bincode dependencies. It preserves Kujo archive behavior, stored credentials and legacy hyphenation dictionaries, corrects native dictionary handling and tightens capability and filesystem boundaries. Bounded HTTP stream collection is available. Rust embedders accessing `Value::ZipArchive.writer` must follow the [ZIP 9 migration guide](https://github.com/kujolang/kujo/blob/v1.8.2/docs/ZIP_9_RUST_MIGRATION.md); Kujo scripts require no archive API migration.

See the [release notes](https://github.com/kujolang/kujo/blob/main/docs/RELEASE_NOTES_1_8_2.md). Rust 1.89 remains the source-build minimum; experimental companion protocols and participant SDKs are not promoted by this patch.
