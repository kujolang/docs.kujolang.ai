---
title: Software Factory
description: Turn a software brief or GitHub issue into a locally tested candidate with evidence you can review and verify offline.
template: docs
section: Showcases
nav_title: Software Factory
order: 49
audience: developer
difficulty: intermediate
status: local scope verified
version: 0.2.0
last_updated: "2026-11-20"
scope: local software construction and independent release checks
source_repo: software-factory
tags: [showcase, agents, workcell, testing, evidence]
---

Start with an idea, a reviewed spec, a supported local repository, or a GitHub issue. Software Factory 0.2.0 gives you a candidate you can inspect, the checks that ran against it, and an evidence bundle a second operator can verify offline.

## What you can do

- Freeze requirements and acceptance criteria with Spec before construction. The pinned catalog includes all 28 Chain of Command roles and 136 skills, and each mission selects the roles it needs.
- Build Node APIs and static interfaces, use the locked React 18 static profile, or build a CLI with a qualified Python, TypeScript, Go, Rust, or Kujo profile. Separate routes cover repository repairs, documentation review, locked dependency upgrades, and disposable SQLite migrations.
- Run independent API and browser checks inside rootless Workcell. Dispatch coordinates work, while Eval, Lens, ShipCheck, RunLedger, and Casefile contribute evaluation, release checks, usage records, and retained failure evidence.
- Inspect the run in the local Factory Floor or use the default read-only stdio MCP server. Export the result for offline verification and keep release approval tied to the exact tested source.

## Install the tagged release

Use Git and Node 26.12.1 or a later 26.x release. Live software execution requires a local rootless Docker engine with seccomp. Configure a provider separately for model-backed work.

```sh
git clone --branch 0.2.0 https://github.com/kujolang/software-factory.git
cd software-factory
npm ci
npm run setup
npm run doctor -- --offline
```

Follow the versioned [setup guide](https://github.com/kujolang/software-factory/blob/0.2.0/docs/AGENT-SETUP.md) to configure the engine, build the image, and run the first mission. Start the loopback Factory Floor with `npm start`. For a compatible local MCP host, run `node bin/software-factory.mjs mcp` from the checkout.

## Review the boundaries

The runtime and integration profiles cover documented project shapes. Independent local acceptance gives you a candidate for review. Pull request publication, merge, deployment, and production migrations require separate authorization. Signed exports authenticate a manifest against a trusted key, while tests and execution records document what was observed.

See the [0.2.0 release](https://github.com/kujolang/software-factory/releases/tag/0.2.0), [release qualification](https://github.com/kujolang/software-factory/blob/0.2.0/docs/RELEASE-QUALIFICATION.md), [evidence guide](https://github.com/kujolang/software-factory/blob/0.2.0/docs/EVIDENCE.md), and [known limitations](https://github.com/kujolang/software-factory/blob/0.2.0/docs/KNOWN-LIMITATIONS.md).
