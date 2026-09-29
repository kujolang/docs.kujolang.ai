---
title: MCP
description: Generate guarded MCP servers with roots, limits, auth, and safety tiers.
template: docs
section: Tools
nav_title: MCP
order: 70
audience: developer
difficulty: advanced
status: local scope verified
version: 1.2.0
last_updated: 2026-09-29
scope: local-first
source_repo: mcp
previous: /tools/dispatch/
next: /tools/rag/
tags: [tool, mcp, integrations]
---


## Use it when…

An agent needs a deliberate server boundary for tools or resources with roots, limits, auth, and a visible safety tier.

## Interface overview

| Surface | What is available |
| --- | --- |
| Generator | `make <repo>` with output and artifact-directory controls |
| Profiles | Repo-specific discovery plus profile-only or artifacts-only generation |
| Contracts | `mcp-server.json`, tool/resource registries, and `mcp.manifest.json` |
| Safety | Roots, auth metadata, safety tiers, validation, dry-run, and no-AI mode |

## Main workflows

- Inspect a repository and generate an MCP server scaffold matched to its visible capabilities.
- Review tool and resource registrations before exposing them to an agent client.
- Use dry-run and validation modes to check the generated profile without mutating the target.
- Keep high-risk operations behind explicit authentication, roots, and safety-tier policy.

## Five-minute example

```bash
kujo run mcp.kujo --interpreter make ./repo-folder --dry-run
kujo run mcp.kujo --interpreter make ./repo-folder --validate
```

## What you get

A repo-specific MCP scaffold, manifest, tool/resource registry, and safety metadata.

## How it fits

Pair MCP with [Agents SDK](/tools/agents-sdk/) and [Scent](/tools/scent/) before exposing context.

## Boundaries

This is a guarded local/server scaffold, not managed enterprise infrastructure.

## Reference

See the [MCP repository](https://github.com/kujolang/mcp).

## Portable operation contracts

Use [Ability](/tools/ability/) to preserve an operation’s identity, schemas, effects, and retry semantics across application and agent surfaces. Its SDK previews and fixture development kit help check contracts; the application retains execution authority.

## Public catalog and application gateways

The public endpoint at [mcp.kujolang.ai/mcp](https://mcp.kujolang.ai/mcp) is a separate read-only catalog of Kujo projects, skills, workflows, installation guidance, and release boundaries. Its catalog revision identifies the deployed snapshot; its service version is not the programming-language version. Use `get_catalog_item` with `slug: "kujo"` for the runtime release, and `get_installation` for the `core`, `agent`, `ai`, `quality`, `showcases`, or `operating` profile.

The latest published MCP framework release is [1.2.0](https://github.com/kujolang/mcp/releases/tag/v1.2.0). Its application Ability gateways, host certification receipts, and operator controls remain separate from public catalog discovery. Certification applies to the exact tested source revisions and host tiers; newer Agents SDK or Kujo Pi source changes are not automatically certified by older receipts.

## Version 1.2.0 and Kujo 1.6

MCP 1.2.0 requires Kujo 1.6.0 and includes experimental controlled local STDIO Ability handoffs, one-use host admission and bounded evidence references. Lost completion remains uncertain until the effect owner verifies it; Dispatch alone decides replay. Standalone MCP behavior remains available.

See the [1.2.0 release](https://github.com/kujolang/mcp/releases/tag/v1.2.0) for the exact source and release evidence. Assurance beta remains opt-in, required/deny and single-effect; controlled handoffs remain alpha. These package releases do not stabilize remote trust or participant SDKs.
