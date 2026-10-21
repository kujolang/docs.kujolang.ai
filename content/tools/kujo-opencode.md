---
title: Kujo OpenCode
description: Install Kujo tools in OpenCode 2, choose a specialist, review approvals, and inspect receipts.
custom_url: kujo-opencode
template: docs
section: Tools
nav_title: Kujo OpenCode
order: 236
audience: developer
difficulty: intermediate
status: released
version: 0.2.1
last_updated: "2026-10-21"
scope: local OpenCode 2 integration
source_repo: kujo-opencode
tags: [tool, opencode, agents, ability, integration]
---

## Use it when

You want OpenCode to inspect a repository, build and test Kujo programs, review changes, check browser workflows, or collect release evidence. Kujo OpenCode provides a native plugin, six focused specialists, and a local MCP fallback. OpenCode owns the model connection; Kujo runs supported tools locally.

## Install and verify

Requirements: Node.js 22.23.4+, 24.22.1+, or 26.12.1+ on those release lines, npm, Git, and OpenCode 2 version 2.0.31 or newer. OpenCode 1 is not supported.

```sh
npm install --global @kujolang/kujo-opencode@0.2.1
cd /path/to/your/project
kujo-opencode setup
kujo-opencode doctor
kujo-opencode demo
opencode
```

Setup downloads 28 pinned Kujo source repositories and the runtime, so allow several minutes, internet access, and disk space. A separate global Kujo install is not required. Doctor reports readiness and suggested fixes. The demo performs a read-only ShipCheck scan and returns a receipt without a model call. A successful scan alone does not certify your project for release.

Open `/kujo` in OpenCode to choose a profile, manage individual capabilities, select a specialist, review a pending approval, or inspect evidence.

## Choose a profile

| Profile | Capabilities | Use it for |
| --- | ---: | --- |
| Essentials | 5 | Repository understanding and change inspection |
| Review | 18 | Architecture, task contracts, context, and change size |
| Build | 17 | Source inspection, reviewed execution, and starter projects |
| Ship | 30 | Verification and durable release evidence |
| Full | 62 | All supported operations, including optional service tools |

You can also manage exposure from the terminal:

```sh
kujo-opencode profiles
kujo-opencode profile review
kujo-opencode enable lens
kujo-opencode abilities
```

Restart OpenCode after CLI exposure changes. Native capability changes refresh immediately after host permission. Overrides survive profile changes and updates. Neither a profile nor an enabled capability grants permission to execute effects.

## Pick a specialist

| Specialist | Work |
| --- | --- |
| Understand | Scout repository inspection and Scent context packs |
| Build | Kujo source inspection, starter creation, and reviewed source/test execution |
| Review | PatchBrief summaries, ChangeBucket measurements, and scoped checks |
| Browser | Lens flow validation and optional real-browser checks |
| Workflow | Dispatch validation, execution, run inspection, and checkpoint decisions |
| Ship | ShipCheck scans, Eval runs, and linked RunLedger evidence |

Give the specialist a concrete task in a trusted project. For example: “Review my current changes and explain the receipts,” or “Create a small Kujo starter, show me the proposed files, then run its checks after I approve.” Ship gathers evidence; it does not publish a release for you.

## Included projects

- **Repository context:** Scout, Scent, RAG, and Kujo Skills.
- **Build and integration:** Ability, Agents SDK, MCP, CRUD API, and Kennel.
- **Review and checks:** PatchBrief, ChangeBucket, Fence, Spec, Eval, Concord, and Lens.
- **Workflow and tracking:** Dispatch, RunLedger, Watchdog, Muzzle, and PackWrite.
- **Evidence and release work:** Casefile, Dossier, Redact, Tribunal, VersionSeal, ShipCheck, and Howl.

The adapter exposes supported operations, not each project's entire interface. For exact schemas and scope, see the [released catalog](https://github.com/kujolang/kujo-opencode/tree/v0.2.1/catalog).

## Review approvals and receipts

Before an effectful operation, OpenCode opens the Kujo operation review. Inspect the input, effects, destination, and approval identity. Return to the permission choice and select Allow once or Reject. Closing the review grants nothing. Kujo binds approval to the exact request and records the result as a receipt.

Use `/kujo` to review pending approvals or inspect evidence. After a lost Dispatch response, inspect the retained run before retrying; an uncertain response does not prove that execution failed.

The explicit MCP fallback uses terminal review instead:

```sh
kujo-opencode approve REQUEST_ID
```

This command requires an interactive human decision. Agents must not approve their own actions. OpenCode's own permission checks remain separate.

## Connect a provider

Use OpenCode's provider controls to select an account and model. For ChatGPT, choose OpenAI, select Sign in with ChatGPT, and finish the browser sign-in. Requests use that connection's allowance. Kujo does not copy credentials, proxy model traffic, or silently choose a paid provider.

Live acceptance used an explicitly configured local Hermes connection with `reflection/beam-1.0-501b-a23b:free` on macOS x64 with OpenCode 2.1.2: six specialists and 50 operation checks passed. Model availability depends on your account. The free GLM and DeepSeek routes returned HTTP 403 for scoped specialist requests; their listing does not establish that they work here.

## Optional browser and services

Lens flow validation does not need Chromium. Real browser checks require an explicit installation:

```sh
kujo-opencode browser install
```

Watchdog delivery and RunLedger lifecycle tracking are opt-in. Setup does not start services or turn on background telemetry. Remote Ability gateways, Leash, and other private services require their own configuration and authorization. Read the [service support boundaries](https://github.com/kujolang/kujo-opencode/blob/v0.2.1/docs/SERVICE-SUPPORT.md) before enabling them.

## Update and recover

Install the desired published npm version, then run `kujo-opencode update` in each project. Updates preserve profiles, overrides, and receipts. Projects on older versions retain their own projections.

- `kujo-opencode status` shows the active installation.
- `kujo-opencode doctor` reports missing prerequisites and repair guidance.
- `kujo-opencode recover` handles an interrupted source/runtime transaction; it refuses to take over a live installer.
- `kujo-opencode repair` restores owned plugin, MCP, skill, and command projections.
- `kujo-opencode uninstall` removes the project's integration and retains shared data. Review the released guide before using `--purge`.

Install this host integration through npm, not `kennel add kujo-opencode`. Kennel remains available inside the integration for supported Kujo dependency operations; it does not replace npm or OpenCode's host setup.

## Verified release scope

Native and rendered host checks passed on Linux, macOS, and Windows with OpenCode 2.0.31 and 2.1.2. Linux coverage uses glibc Ubuntu; it does not establish musl compatibility. Live model testing is scoped to macOS and the Hermes provider as above. Registry installation, upgrade, signatures, provenance, and the GitHub release archive were verified separately. Later host or provider versions need their own compatibility checks.

- [Ecosystem overview](https://kujolang.ai/ecosystem/kujo-opencode/)
- [Kujo OpenCode 0.2.1 release and evidence](https://github.com/kujolang/kujo-opencode/releases/tag/v0.2.1)
- [Daily-use guide](https://github.com/kujolang/kujo-opencode/blob/v0.2.1/docs/USER-GUIDE.md)
- [Compatibility and troubleshooting](https://github.com/kujolang/kujo-opencode/blob/v0.2.1/docs/COMPATIBILITY.md)
- [Walkthrough and demo source](https://github.com/kujolang/kujo-opencode/tree/v0.2.1/docs/walkthrough)
