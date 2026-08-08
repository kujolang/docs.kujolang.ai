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
version: current
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
