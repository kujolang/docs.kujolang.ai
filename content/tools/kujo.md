---
title: Kujo
description: Write and run local-first Kujo programs.
template: docs
section: Tools
nav_title: Kujo
order: 10
audience: developer
difficulty: beginner
status: release-candidate scope
version: current
scope: local-first
source_repo: kujo
next: /tools/kennel/
tags: [tool, foundation, language]
---

# Kujo

## Use it when…

You want to write a small program, check it, and run it with the same VM-first CLI path used by the rest of the ecosystem.

## Five-minute example

```bash
kujo init --name hello-kujo
cd hello-kujo
kujo check src/main.kujo
kujo run src/main.kujo
```

## What you get

A `kujo.toml` project, a source entry point, and explicit CLI output you can inspect or capture.

## How it fits

Start here, then add [Kennel](/tools/kennel/) when the project needs dependencies.

## Boundaries

This page keeps release-candidate onboarding visible until public artifacts, checksums, and clean-machine download proof are complete.

## Reference

Use `kujo --help`, `kujo doctor --json`, and the [language basics](/learn/language-basics/) guide.

