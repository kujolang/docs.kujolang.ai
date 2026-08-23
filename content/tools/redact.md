---
title: Redact
description: Produce deterministic, review-required redactions for local text and Markdown.
template: docs
section: Tools
nav_title: Redact
order: 115
audience: developer
difficulty: intermediate
status: stable 1.0 local scope
version: current
last_updated: 2026-08-23
scope: local-first
source_repo: redact
tags: [tool, privacy, redaction]
---

## Use it when…

Text or Markdown must be sanitized before it enters an AI context pack, evidence bundle, or external handoff.

## Five-minute example

```bash
kujo run redact.kujo scan fixtures/sample.md --policy fixtures/sample.policy.yaml
kujo run redact.kujo sanitize fixtures/sample.md --policy fixtures/sample.policy.yaml --out /tmp/sample.redacted.md
kujo run redact.kujo verify /tmp/sample.redacted.md --policy fixtures/sample.policy.yaml
```

## What you get

A sanitized file and an audit run tied to the selected policy.

## Boundaries

Redact is a deterministic aid, not a promise of complete PII detection. It supports local `.txt` and `.md` paths in its stable scope, rejects unsafe paths and overwrites, and requires human review before sharing.

## Reference

See the [Redact repository](https://github.com/kujolang/redact).
