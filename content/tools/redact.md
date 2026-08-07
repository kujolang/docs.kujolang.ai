---
title: Redact
description: Remove or transform sensitive values before context leaves the workspace.
template: docs
section: Tools
nav_title: Redact
order: 240
audience: developer
difficulty: intermediate
status: preview; supported input policy visible
version: current
scope: local-first
source_repo: redact
next: /tools/howl/
tags: [tool, privacy, security]
---

# Redact

## Use it when…

Logs, context packs, screenshots, or evidence bundles may contain secrets or personal data that should not travel with the handoff.

## Five-minute example

```bash
redact scan --input casefile.json --output casefile.redacted.json
```

## What you get

A transformed output, match summary, and policy evidence for the supported input type.

## How it fits

Use before [Scent](/tools/scent/), [CaseFile](/tools/casefile/), or [Lens](/tools/lens/) artifacts leave the workspace.

## Boundaries

Supported input policy matters. Redaction is not proof that every sensitive value was identified.

## Reference

See the [Redact repository](https://github.com/kujolang/redact).

