---
title: Support
description: Find the right place to ask for help, report a problem, or verify a local failure.
custom_url: support
template: docs
section: Reference
nav_title: Support
order: 90
audience: all
difficulty: beginner
status: stable
version: current
tags: [support, troubleshooting]
---


Start with the smallest reproducible command and the local artifact it leaves behind.

## Before asking for help

```bash
kujo --version
kujo doctor --json
kujo check path/to/file.kujo
```

Capture the exact command, platform, Kujo version, and relevant output. Remove secrets before sharing it.

## Useful evidence tools

- [CaseFile](/tools/casefile/) captures a failure bundle.
- [RunLedger](/tools/runledger/) records run metadata and verdicts.
- [PatchBrief](/tools/patchbrief/) prepares a diff handoff.
- [Scent](/tools/scent/) creates bounded context packs before context leaves the workspace.
