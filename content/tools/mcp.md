---
title: MCP
description: Generate guarded MCP servers with roots, limits, auth, and safety tiers.
template: docs
section: Tools
nav_title: MCP
order: 90
audience: developer
difficulty: advanced
status: launch scope
version: current
scope: local-first
source_repo: mcp
next: /tools/rag/
tags: [tool, mcp, integrations]
---

# MCP

## Use it when…

An agent needs a deliberate server boundary for tools or resources with roots, limits, auth, and a visible safety tier.

## Five-minute example

```bash
kujo run mcp.kujo --interpreter make
```

## What you get

A repo-specific MCP scaffold, manifest, tool/resource registry, and safety metadata.

## How it fits

Pair MCP with [Agents SDK](/tools/agents-sdk/) and [Redact](/tools/redact/) before exposing context.

## Boundaries

This is a guarded local/server scaffold, not managed enterprise infrastructure.

## Reference

See the [MCP repository](https://github.com/kujolang/mcp).

