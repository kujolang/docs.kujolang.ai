---
title: Quality and release gates
description: Check drift, boundaries, release readiness, browser behavior, and sensitive values before shipping.
custom_url: review/quality-and-release-gates
template: docs
section: Keep work reviewable
nav_title: Quality and release gates
order: 40
audience: developer
difficulty: advanced
status: launch scope
version: current
previous: /review/evidence-and-run-history/
next: /review/browser-architecture-and-privacy/
tags: [quality, release, gates]
---

# Quality and release gates

Use the narrowest gate that answers the question:

- [Concord](/tools/concord/) finds drift across code, docs, examples, specs, and generated artifacts.
- [Fence](/tools/fence/) checks architecture boundaries and import rules.
- [ShipCheck](/tools/shipcheck/) scans release readiness.
- [Lens](/tools/lens/) reviews browser behavior and visual/accessibility contracts.
- [Redact](/tools/redact/) transforms sensitive values before context leaves the workspace.

```bash
kujo run shipcheck.kujo gate
```

Preview labels remain visible where broader proof is still in progress.

