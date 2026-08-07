---
title: PackWrite
description: Compile repeatable agent execution packs from context and prompts.
template: docs
section: Tools
nav_title: PackWrite
order: 140
audience: developer
difficulty: intermediate
status: launch scope; local/team workflow
version: current
scope: local-first
source_repo: packwrite
next: /tools/muzzle/
tags: [tool, agents, packs]
---

# PackWrite

## Use it when…

A team repeats the same agent workflow and needs the context, prompt, model configuration, and evidence contract to be inspectable.

## Five-minute example

```bash
kujo run packwrite.kujo prompt --config packwrite.toml
```

## What you get

An execution pack, prompt, config, doctor output, and deterministic validation result.

## How it fits

Compile from [Scent](/tools/scent/) and run quietly with [Muzzle](/tools/muzzle/).

## Boundaries

PackWrite is a local/team workflow compiler; provider and hosted execution remain separate concerns.

## Reference

See the [PackWrite repository](https://github.com/kujolang/packwrite).

