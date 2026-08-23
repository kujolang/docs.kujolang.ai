---
title: How the runtime works
description: Understand the VM-first execution path, interpreter fallback, and the role of the CLI.
custom_url: runtime
template: docs
section: Learn Kujo
nav_title: Runtime
order: 20
audience: developer
difficulty: beginner
status: stable
version: current
last_updated: 2026-08-23
previous: /learn/language-basics/
next: /learn/capabilities/
tags: [runtime, vm, interpreter]
---


The normal path is the VM. It keeps the command developers use in production-like checks aligned with the command they use while learning.

```bash
kujo run app.kujo
```

Use the interpreter when a compatibility or debugging workflow calls for it:

```bash
kujo run --interpreter app.kujo
```

The CLI also owns project initialization, checks, formatting, linting, packages, DocGen, and serving static output. That common surface is why the first-time path introduces the language before the larger ecosystem.

