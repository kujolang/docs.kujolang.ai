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
last_updated: 2026-09-09
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


## Native scripting and installed tools

Kujo v1.4.0 adds the runtime operations needed for package installers and command launchers written in Kujo. On Linux and macOS, `file_lock` and `file_unlock` coordinate cooperating processes, `path_owned` checks ownership, `symlink_atomic` publishes a command link, and `exec_process` replaces the launcher with an exact argument vector. These POSIX operations require their documented host capabilities; they are not Windows installer support or a sandbox.

Installed tools can opt into imports that do not search the caller's working directory or lockfile:

```bash
kujo run --isolated-imports /path/to/tool/main.kujo -- argument
```

`KUJO_ISOLATED_IMPORTS=1` enables the same mode for inherited launches. Entry and configured roots still apply; ordinary `kujo run` keeps its existing import behavior. Arguments, including empty strings, reach the program unchanged.

The runtime also provides bounded HTTP downloads, HTML and XML processing, JSON/JSONL artifacts, digests, and confined file publication. Callback and lexical-scope corrections keep VM and interpreter workflows consistent. See the [v1.4.0 changelog](https://github.com/kujolang/kujo/blob/v1.4.0/CHANGELOG.md) and [standard library contracts](https://github.com/kujolang/kujo/blob/v1.4.0/docs/STANDARD_LIBRARY.md) for exact signatures, limits, capabilities, and platform boundaries.

These runtime features support the upcoming native Kennel client. Installing or upgrading Kujo does not install or release Kennel; follow the separate [Kennel guide](/tools/kennel/) for its current package workflow.
