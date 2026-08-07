---
title: Kujo Doctor
description: Check the local Kujo environment and explain what needs attention.
template: docs
section: Tools
nav_title: Kujo Doctor
order: 110
audience: developer
difficulty: beginner
status: follows Kujo artifact availability
version: current
scope: local-first
source_repo: kujo/tools/kujo-doctor
next: /tools/scout/
tags: [tool, diagnostics, environment]
---

# Kujo Doctor

## Use it when…

The local environment is not behaving as expected and you want structured diagnostics before opening a bug report.

## Five-minute example

```bash
kujo doctor --json
```

## What you get

Machine-readable checks for the CLI, runtime, paths, and available local dependencies.

## How it fits

Run it before [Support](/support/) or [CaseFile](/tools/casefile/).

## Boundaries

Doctor explains the current workstation; it does not certify a deployment or a release artifact.

## Reference

See the [Kujo Doctor source](https://github.com/kujolang/kujo/tree/main/tools/kujo-doctor).

