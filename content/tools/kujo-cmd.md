---
title: Kujo CMD
description: Install Kujo Abilities, scoped agents, approvals, receipts, and browser QA in Command Code.
template: docs
section: Tools
nav_title: Kujo CMD
order: 235
audience: developer
difficulty: intermediate
status: released
version: 0.2.0
last_updated: 2026-10-06
scope: local-first Command Code integration
source_repo: kujo-cmd
previous: /tools/lens/
next: /tools/ward/
tags: [tool, command-code, mcp, agents, integration]
---

## Use it when…

You want Command Code to discover and run a broad set of Kujo tools through
one local MCP server while preserving Kujo approvals, receipts, identities,
and project boundaries.

## Install

```bash
cd /path/to/your/project
npx github:kujolang/kujo-cmd#v0.2.0 setup
command-code
```

The GitHub release is live. npm publication is temporarily pending restoration
of the package's trusted-publisher or `NPM_TOKEN` authorization, so the command
above runs the same tagged package directly from GitHub. Use
`npx @kujolang/kujo-cmd@0.2.0 setup` after the registry release appears.

The first setup downloads 25 pinned Kujo source projects and the Kujo runtime.
Normal execution is local and works offline. No Kujo account or hosted Kujo
service is required.

## Choose the exposed surface

Setup installs the complete catalog. Profiles only control what Command Code
can see; they do not weaken Command Code permission prompts or Kujo's own
request-bound approvals.

| Profile | Tools | Intended surface |
| --- | ---: | --- |
| Essentials | 5 | Catalog, receipts, repository inspection, change summary, release scan |
| Review | 18 | Architecture, task, context, drift, decision, showcase, and flow review |
| Ship | 29 | Evaluation, durable evidence, privacy, telemetry, rendering, and browser QA |
| Full | 38 | All installed tools, including approved workflow, package, and ingest operations |

```bash
kujo-cmd profiles
kujo-cmd profile kujo.profile.review
kujo-cmd abilities
```

Restart Command Code after changing the active profile.

## What is projected

- One project STDIO MCP server backed by the canonical Kujo Ability runtime.
- Canonical Agent Skills for the installed sources.
- Seven task-scoped Command Code agents with explicit Kujo MCP allowlists.
- A trust-gated Command Code mod for metadata-only Watchdog correlation,
  optional RunLedger recording, subagent correlation, and a one-shot Jidoka
  continuation after a failed Kujo tool call.

Kujo CMD does not choose or proxy the model. It works with any provider that
Command Code supports, including local Ollama configurations.

## Approvals and evidence

Read-only Abilities run under local policy. Write, delete, or external effects
return `ability_approval_required` with the exact approval command. Approvals
expire, are bound to the principal, Ability digest, invocation, and input, and
can be used once.

Every call returns structured content plus a durable local receipt. Session,
run, agent, and model identifiers can be carried through for correlation.
Command Code's host permission prompt remains a separate outer boundary.

## Optional browser checks

Lens flow validation does not require a browser. Real-page checks use an
explicit dependency lifecycle:

```bash
kujo-cmd browser status
kujo-cmd browser install
kujo-cmd doctor --json
```

The install command uses Lens's lockfile-pinned dependencies and Chromium
build. It is intentionally not hidden inside the normal setup path.

## Operate and upgrade

```bash
kujo-cmd status
kujo-cmd doctor --json
kujo-cmd repair
kujo-cmd update
```

Kujo CMD 0.2.0 is verified against Command Code 1.75.1. See the
[0.2.0 release](https://github.com/kujolang/kujo-cmd/releases/tag/v0.2.0) and
[repository](https://github.com/kujolang/kujo-cmd) for the complete catalog,
security boundaries, and troubleshooting guidance.
