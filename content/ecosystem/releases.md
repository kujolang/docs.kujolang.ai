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
last_updated: 2026-10-10
tags: [ecosystem, releases, versions, installation]
---

This inventory was checked against all **86 public kujolang repositories on September 9, 2026**, with Scout and ReaderSignal refreshed from their September 26 releases, the first companion batch from September 28, Workcell/Ability/MCP, Dispatch and SSG from September 29, Kujo from October 4, Tribunal from October 7, and Commerce from October 10. Product releases, protocol versions, repository tags, and the docs site's version are separate. The table lists the latest non-draft, non-prerelease **GitHub Release** found for each package; it does not claim that every current default-branch feature exists in that release.

## Start here

Install [Kujo 1.8.0](/install/) for the current runtime. A standalone binary runs ordinary Kujo programs without Python, Node.js, or Rust. Individual applications and tools retain their own dependencies, supported platforms, runtime pins, and update procedures.

[Kennel's official registry](https://kennel.kujolang.ai/) distributes first-party package artifacts. Kennel 1.1.0 is published separately; Kujo 1.8.0 does not change its version or historical package artifacts. See [package workflows](/learn/packages/) before assuming that upgrading Kujo also updates Kennel or other tools.

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
| [ability](https://github.com/kujolang/ability) | [v1.2.0](https://github.com/kujolang/ability/releases/tag/v1.2.0) | 2026-09-29 |
| [agents-sdk](https://github.com/kujolang/agents-sdk) | [v1.1.2](https://github.com/kujolang/agents-sdk/releases/tag/v1.1.2) | 2026-09-28 |
| [ai-chat](https://github.com/kujolang/ai-chat) | [v1.3.0](https://github.com/kujolang/ai-chat/releases/tag/v1.3.0) | 2026-10-06 |
| [ai-sdk](https://github.com/kujolang/ai-sdk) | [v1.1.1](https://github.com/kujolang/ai-sdk/releases/tag/v1.1.1) | 2026-09-28 |
| [anthropic](https://github.com/kujolang/anthropic) | [v0.1.2](https://github.com/kujolang/anthropic/releases/tag/v0.1.2) | 2026-08-27 |
| [assetworks](https://github.com/kujolang/assetworks) | [v0.2.0](https://github.com/kujolang/assetworks/releases/tag/v0.2.0) | 2026-08-14 |
| [bluepencil](https://github.com/kujolang/bluepencil) | [v0.2.0](https://github.com/kujolang/bluepencil/releases/tag/v0.2.0) | 2026-08-14 |
| [casefile](https://github.com/kujolang/casefile) | [v1.0.0](https://github.com/kujolang/casefile/releases/tag/v1.0.0) | 2026-08-08 |
| [changebucket](https://github.com/kujolang/changebucket) | [v1.0.0](https://github.com/kujolang/changebucket/releases/tag/v1.0.0) | 2026-08-08 |
| [cms](https://github.com/kujolang/cms) | [v1.1.0](https://github.com/kujolang/cms/releases/tag/v1.1.0) | 2026-08-30 |
| [cms-contact-form](https://github.com/kujolang/cms-contact-form) | [v1.0.0](https://github.com/kujolang/cms-contact-form/releases/tag/v1.0.0) | 2026-08-29 |
| [cms-example](https://github.com/kujolang/cms-example) | [v1.1.0](https://github.com/kujolang/cms-example/releases/tag/v1.1.0) | 2026-08-30 |
| [cms-field-notes-theme](https://github.com/kujolang/cms-field-notes-theme) | [v1.0.2](https://github.com/kujolang/cms-field-notes-theme/releases/tag/v1.0.2) | 2026-08-29 |
| [commerce](https://github.com/kujolang/commerce) | [v0.5.0](https://github.com/kujolang/commerce/releases/tag/v0.5.0) | 2026-10-10 |
| [concord](https://github.com/kujolang/concord) | [v1.0.0](https://github.com/kujolang/concord/releases/tag/v1.0.0) | 2026-08-08 |
| [contentgraph](https://github.com/kujolang/contentgraph) | [v0.3.0](https://github.com/kujolang/contentgraph/releases/tag/v0.3.0) | 2026-08-13 |
| [crud-api](https://github.com/kujolang/crud-api) | [v1.0.0](https://github.com/kujolang/crud-api/releases/tag/v1.0.0) | 2026-06-11 |
| [dispatch](https://github.com/kujolang/dispatch) | [v1.3.0](https://github.com/kujolang/dispatch/releases/tag/v1.3.0) | 2026-09-29 |
| [dossier](https://github.com/kujolang/dossier) | [v0.2.0](https://github.com/kujolang/dossier/releases/tag/v0.2.0) | 2026-08-14 |
| [eval](https://github.com/kujolang/eval) | [v1.0.0](https://github.com/kujolang/eval/releases/tag/v1.0.0) | 2026-08-08 |
| [fence](https://github.com/kujolang/fence) | [v1.0.0](https://github.com/kujolang/fence/releases/tag/v1.0.0) | 2026-08-08 |
| [galleypack](https://github.com/kujolang/galleypack) | [v0.2.0](https://github.com/kujolang/galleypack/releases/tag/v0.2.0) | 2026-08-14 |
| [howl](https://github.com/kujolang/howl) | [v1.1.0](https://github.com/kujolang/howl/releases/tag/v1.1.0) | 2026-08-11 |
| [kennel](https://github.com/kujolang/kennel) | [v1.1.1](https://github.com/kujolang/kennel/releases/tag/v1.1.1) | 2026-09-29 |
| [kujo](https://github.com/kujolang/kujo) | [v1.8.0](https://github.com/kujolang/kujo/releases/tag/v1.8.0) | 2026-10-04 |
| [kujo-agents](https://github.com/kujolang/kujo-agents) | [v1.4.0](https://github.com/kujolang/kujo-agents/releases/tag/v1.4.0) | 2026-09-07 |
| [kujo-pi](https://github.com/kujolang/kujo-pi) | [v1.1.0](https://github.com/kujolang/kujo-pi/releases/tag/v1.1.0) | 2026-09-26 |
| [kujo-skills](https://github.com/kujolang/kujo-skills) | [v0.7.0](https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0) | 2026-09-08 |
| [kujo-workflows](https://github.com/kujolang/kujo-workflows) | [v0.6.0](https://github.com/kujolang/kujo-workflows/releases/tag/v0.6.0) | 2026-09-07 |
| [lens](https://github.com/kujolang/lens) | [v1.1.0](https://github.com/kujolang/lens/releases/tag/v1.1.0) | 2026-09-07 |
| [mcp](https://github.com/kujolang/mcp) | [v1.2.0](https://github.com/kujolang/mcp/releases/tag/v1.2.0) | 2026-09-29 |
| [muzzle](https://github.com/kujolang/muzzle) | [v1.1.0](https://github.com/kujolang/muzzle/releases/tag/v1.1.0) | 2026-08-30 |
| [ollama](https://github.com/kujolang/ollama) | [v0.1.10](https://github.com/kujolang/ollama/releases/tag/v0.1.10) | 2026-08-27 |
| [packwrite](https://github.com/kujolang/packwrite) | [v1.1.0](https://github.com/kujolang/packwrite/releases/tag/v1.1.0) | 2026-08-30 |
| [paperclip](https://github.com/kujolang/paperclip) | [v0.1.7](https://github.com/kujolang/paperclip/releases/tag/v0.1.7) | 2026-09-04 |
| [patchbrief](https://github.com/kujolang/patchbrief) | [v1.0.1](https://github.com/kujolang/patchbrief/releases/tag/v1.0.1) | 2026-08-30 |
| [presswire](https://github.com/kujolang/presswire) | [v0.2.0](https://github.com/kujolang/presswire/releases/tag/v0.2.0) | 2026-08-14 |
| [rag](https://github.com/kujolang/rag) | [v1.0.0](https://github.com/kujolang/rag/releases/tag/v1.0.0) | 2026-08-08 |
| [readersignal](https://github.com/kujolang/readersignal) | [v0.3.0](https://github.com/kujolang/readersignal/releases/tag/v0.3.0) | 2026-09-26 |
| [redact](https://github.com/kujolang/redact) | [v1.0.0](https://github.com/kujolang/redact/releases/tag/v1.0.0) | 2026-08-09 |
| [relay](https://github.com/kujolang/relay) | [v1.1.0](https://github.com/kujolang/relay/releases/tag/v1.1.0) | 2026-08-27 |
| [runledger](https://github.com/kujolang/runledger) | [v1.2.0](https://github.com/kujolang/runledger/releases/tag/v1.2.0) | 2026-09-28 |
| [scent](https://github.com/kujolang/scent) | [v1.0.0](https://github.com/kujolang/scent/releases/tag/v1.0.0) | 2026-08-08 |
| [scout](https://github.com/kujolang/scout) | [v1.1.0](https://github.com/kujolang/scout/releases/tag/v1.1.0) | 2026-09-26 |
| [searchbridge](https://github.com/kujolang/searchbridge) | [v1.0.0](https://github.com/kujolang/searchbridge/releases/tag/v1.0.0) | 2026-09-04 |
| [shipcheck](https://github.com/kujolang/shipcheck) | [v1.0.0](https://github.com/kujolang/shipcheck/releases/tag/v1.0.0) | 2026-08-08 |
| [site-kit](https://github.com/kujolang/site-kit) | [v1.0.0](https://github.com/kujolang/site-kit/releases/tag/v1.0.0) | 2026-08-09 |
| [siteprobe](https://github.com/kujolang/siteprobe) | [v0.3.0](https://github.com/kujolang/siteprobe/releases/tag/v0.3.0) | 2026-09-07 |
| [spec](https://github.com/kujolang/spec) | [v1.0.1](https://github.com/kujolang/spec/releases/tag/v1.0.1) | 2026-08-30 |
| [ssg](https://github.com/kujolang/ssg) | [v1.1.0](https://github.com/kujolang/ssg/releases/tag/v1.1.0) | 2026-09-29 |
| [storydesk](https://github.com/kujolang/storydesk) | [v0.2.0](https://github.com/kujolang/storydesk/releases/tag/v0.2.0) | 2026-08-14 |
| [tribunal](https://github.com/kujolang/tribunal) | [v1.0.2](https://github.com/kujolang/tribunal/releases/tag/v1.0.2) | 2026-10-07 |
| [versionseal](https://github.com/kujolang/versionseal) | [v0.2.0](https://github.com/kujolang/versionseal/releases/tag/v0.2.0) | 2026-08-14 |
| [watchdog](https://github.com/kujolang/watchdog) | [v1.2.0](https://github.com/kujolang/watchdog/releases/tag/v1.2.0) | 2026-09-29 |
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

Kujo 1.8 does not republish or silently upgrade companion tools. RunLedger 1.2.0, AI SDK 1.1.1 and Agents SDK 1.1.2 remain published. AI SDK live-provider smoke was explicitly deferred for that release. Workcell, Ability and MCP 1.2.0 distribute the controlled-execution cohort while retaining experimental assurance/interoperability boundaries. Dispatch 1.3.0 completes this controller release cohort with the same experimental boundaries. Stop older workers and follow its backup/upgrade instructions before changing persisted-state versions.
