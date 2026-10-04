---
title: Editor and CLI support
description: Use the CLI, LSP, and editor adapters to keep feedback close to the file you are editing.
custom_url: editor-support
template: docs
section: Learn Kujo
nav_title: Editor and CLI support
order: 50
audience: developer
difficulty: beginner
status: stable
version: current
last_updated: 2026-10-04
previous: /learn/packages/
next: /learn/ai-runtime/
tags: [editor, lsp, cli]
---


The CLI is the compatibility baseline. LSP and editor adapters add completion, definition, references, hover, diagnostics, rename, and code actions where the adapter is available.

Kujo 1.8 shares one immutable analyzed-program model between `kujo check` and
the LSP. Hover and completion can expose inferred variables, callable
signatures, struct fields, methods and imported namespace members. Optional
checker findings remain warnings: genuinely dynamic values still use gradual
fallback instead of becoming runtime type gates.

Open files are analyzed once per content revision and reused across diagnostics,
hover and completion. Editing an imported module refreshes open direct and
transitive dependents, including unsaved buffers; closing the buffer returns
analysis to disk state. Stale results after an edit are a bug, not an accepted
cache tradeoff.

Keep the command loop close to the file:

```bash
kujo check src/main.kujo
kujo format src/main.kujo
kujo lint src/main.kujo
```

When an editor integration behaves differently from the CLI, reproduce the issue with the CLI first and capture the exact version and command.
