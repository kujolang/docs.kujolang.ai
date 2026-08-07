---
title: Capabilities and safe execution
description: Grant only the filesystem, clock, network, or process access a local task actually needs.
custom_url: capabilities
template: docs
section: Learn Kujo
nav_title: Capabilities
order: 30
audience: developer
difficulty: intermediate
status: stable
version: current
previous: /learn/runtime/
next: /learn/packages/
tags: [security, capabilities, safe-execution]
---

# Capabilities and safe execution

Trusted mode is convenient for local development. Untrusted mode makes host effects explicit and is useful when a workflow needs a visible boundary.

```bash
kujo run --untrusted \
  --allow-fs-read --allow-fs-write \
  --allow-clock app.kujo
```

Add `--allow-net-client` for deliberate network access and process capabilities only when the task requires them. Keep credentials in the runtime's secret path; do not put them in source, fixtures, or evidence bundles.

For a fuller boundary discussion, read the [security model](/security/).

