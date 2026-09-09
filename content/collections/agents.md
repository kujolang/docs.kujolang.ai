---
title: Agents
description: Reusable role contracts, chain of command, and evidence expectations.
template: docs
section: Collections
nav_title: Agents
order: 30
audience: developer
difficulty: intermediate
status: local scope verified
version: 1.4.0
last_updated: 2026-09-09
scope: local-first
source_repo: kujo-agents
previous: /collections/workflows/
next: /collections/benchmarks/
tags: [collection, agents, roles]
---


Agent roles should carry a clear objective, boundary, handoff format, and evidence expectation. Use them with [Spec](/tools/spec/) and [Scent](/tools/scent/) rather than treating a role prompt as a complete workflow.

See the [Kujo Agents repository](https://github.com/kujolang/kujo-agents).

## Current distribution

[Kujo Agents 1.4.0](https://github.com/kujolang/kujo-agents/releases/tag/v1.4.0) includes versioned VideoOps production requests, provider authorization evidence, and exact-candidate review contracts. Shared media tools and schemas live in `kujo-agents/videoops/tools`; workflow and skill packages consume that canonical implementation.

Use it alongside [Workflows 0.6.0](/collections/workflows/) and [Skills 0.7.0](/collections/skills/). The operator owns provider permissions and publication authority. Incomplete review stays explicit, and offline fixtures do not establish live-provider support. This role distribution is separate from the [Agents SDK](/tools/agents-sdk/) runtime library.
