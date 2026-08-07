---
title: Browser, architecture, and privacy checks
description: Keep browser evidence, dependency boundaries, and redaction in the same release conversation.
custom_url: review/browser-architecture-and-privacy
template: docs
section: Keep work reviewable
nav_title: Browser, architecture, and privacy
order: 50
audience: developer
difficulty: advanced
status: preview-aware
version: current
previous: /review/quality-and-release-gates/
tags: [browser, architecture, privacy]
---

# Browser, architecture, and privacy checks

Browser QA is evidence from the browsers and viewport matrix actually run. Architecture checks are evidence from the configured boundary graph. Privacy checks are evidence from the input policy and redaction run.

Keep the three claims separate, then link them in the release handoff. This prevents a passing visual smoke from implying a security review, or a clean import graph from implying a hosted deployment is ready.

See [Lens](/tools/lens/), [Fence](/tools/fence/), and [Redact](/tools/redact/) for the smallest local workflows.

