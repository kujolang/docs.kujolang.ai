---
title: Security model
description: Understand capability gates, local boundaries, secrets, network access, and safe execution wording.
custom_url: security
template: docs
section: Reference
nav_title: Security model
order: 80
audience: developer
difficulty: intermediate
status: stable
version: current
next: /release-boundaries/
tags: [security, capabilities, local-first]
---


Kujo gates host effects such as filesystem, network, and process access behind explicit runtime capabilities. The trusted path is convenient for local development; untrusted mode makes the allow-list visible.

## Make access explicit

```bash
kujo run --untrusted \
  --allow-fs-read --allow-fs-write \
  --allow-clock app.kujo
```

Add network or process capabilities only when the program needs them. A capability flag changes the runtime mode, so enumerate the full set required by the command.

## Boundary language

- Local-first does not mean hosted.
- A preview receipt is not a security certification.
- Security and network showcases use authorized, inert fixtures.
- Redaction belongs before context leaves the workspace.

See [Scent](/tools/scent/) and [MCP](/tools/mcp/) for boundary-specific workflows.
