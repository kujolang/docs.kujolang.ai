---
title: Kujo for Paperclip
description: "Verify agent work with approved execution, browser checks, acceptance decisions and retained evidence in Paperclip."
template: docs
section: Tools
nav_title: Paperclip
order: 255
audience: developer
difficulty: beginner
status: released
version: 0.3.0
last_updated: "2026-11-12"
scope: local Paperclip integration
source_repo: paperclip
previous: /tools/howl/
next: /tools/site-kit/
tags: [tool, agents, context, review, evidence]
---

## Included features

Kujo for Paperclip brings repository understanding, project knowledge, native quality checks and human-approved workflows into the project and issue views.

- **Understand a repository:** Scout maps its structure; Scent selects bounded context; ChangeBucket and PatchBrief explain a change.
- **Ask your project:** explicitly select local files, build a private offline index, ask questions with snapshot citations, inspect freshness and delete retained indexes. No provider key is required.
- **Check quality:** inspect architecture boundaries, artifact drift, task contracts, release-readiness signals and package declarations using canonical Kujo tools.
- **Build with Kujo:** preview script, AI-agent, SQLite API and MCP starters. Separately enabled project creation and source run/test actions require exact human approval.
- **Run approved work:** opt-in Eval execution and shipped offline Dispatch examples use human approval, bounded execution, checkpoints and retained receipts.
- **Keep evidence:** inspect, compare and export bounded redacted history; explicitly attach evidence to an issue.

## Verification Center in 0.3.0

The issue Verification Center connects approved execution, recorded results and human acceptance to Paperclip's existing tasks, agents and runs. All 21 previous tools remain available; `manage-kujo-assurance` adds the new workflows.

- **Run approved checks:** opt into local Docker execution with Workcell, loopback browser checks with Lens, named Muzzle workflows and PackWrite validation or supplied-plan compilation.
- **Review evidence:** inspect logs, browser screenshots, failed and corrected attempts, recorded approval and native agent/run identity. Import RunLedger receipts and available Watchdog metadata; imported claims remain explicitly unverified.
- **Decide acceptance:** distinguish current, stale, missing and failed evidence, request human review and record authorized waivers. These decisions do not override native issue status.
- **Inspect delegated work:** browse native child assignments in bounded 50-issue pages; restart when tree membership changes.

The real-host demonstration uses four deterministic process agents and retains failures, human review and evidence across restart. It does not claim autonomous LLM staffing or provider cost measurement. See the [release notes](https://github.com/kujolang/paperclip/blob/v0.3.0/docs/RELEASE_0_3_0.md) and [configuration guide](https://github.com/kujolang/paperclip/blob/v0.3.0/docs/ACCOUNTABILITY.md).

## Install and upgrade

Use official Paperclip **2026.1012.0** or later and Node.js **24.22.1** on the 24.x line or **26.12.1** and later. Version 0.3.0 is qualified against official Paperclip 2026.1106.0. No custom host fork, separate Kujo installation, provider key or manual installation of bundled tools is needed.

```bash
npx paperclipai plugin install @kujolang/paperclip
```

Back up your Paperclip data before upgrading, upgrade the host first, install the plugin and restart Paperclip. Open an issue, check runtime health, then select **Try the Kujo example**. Next try **Understand this repository** or index explicitly selected files with **Ask your project**. Execution features are separately enabled in company settings; requesting approval never starts execution automatically.

## Boundaries

Quality reports and suggested checks are not proof that tests ran. Approved Eval and source execution run trusted code and can affect the host or network; they are not an operating-system sandbox. Starter previews do not install dependencies or start services. Dispatch workflow support is limited to the shipped offline examples; live providers and general recovery of uncertain external effects are not included.

The new assurance execution workflows require macOS or Linux; existing compatible Windows tools remain available. Workcell requires a configured local Docker environment and approved immutable image; remote sandboxes are not exposed. Lens requires optional browser dependencies and unauthenticated loopback targets. PackWrite uses supplied plans, and Watchdog imports metadata only. The official 2026.1106.0 host does not mount plugin run tabs; use the issue Verification Center and scoped run-evidence tools.

The plugin ships 19 pinned, checksummed component snapshots and Kujo 1.8.1. Its offline RAG subset has separate plugin qualification; the standalone RAG 1.1.0 candidate remains unpublished pending its required review evidence. This does not certify arbitrary hosted RAG deployments.

See the [0.3.0 release](https://github.com/kujolang/paperclip/releases/tag/v0.3.0), [usage guide](https://github.com/kujolang/paperclip/blob/v0.3.0/docs/USAGE.md), [execution boundaries](https://github.com/kujolang/paperclip/blob/v0.3.0/docs/EXECUTION.md) and [knowledge guide](https://github.com/kujolang/paperclip/blob/v0.3.0/docs/KNOWLEDGE.md).

## Agent access and install compatibility

Agents can discover the available workflows with `kujolang.paperclip:list-capabilities`. Use `kujolang.paperclip:get-context` to select bounded context, then `kujolang.paperclip:get-context-content` to read only approved selected content. `kujolang.paperclip:review-changes` and `kujolang.paperclip:capture-failure` retain the original review and evidence workflows. New execution tools may request human approval but cannot approve their own requests.

Use the unversioned scoped package name in the install command above. The official host's exact-version scoped-package parsing fix remains under review in [paperclipai/paperclip#12745](https://github.com/paperclipai/paperclip/pull/12745); the normal installation command avoids that issue.

### Upgrading from 0.1.x

Back up Paperclip data. As an instance administrator, uninstall the existing Kujo plugin with **data retention enabled (do not purge)**, then immediately use the install command above to install the new release, then restart Paperclip. Review the expanded permissions: scheduled jobs, private database storage, local workflow folders and issue interaction/document actions support the new features. The official 2026.1012.0 host's dedicated Upgrade action rejects added capabilities; use its administrator install flow for this release. Do not select permanent data removal. The upgrade rehearsal preserves the existing plugin identity and retained failure evidence across restart.
