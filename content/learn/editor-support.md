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
status: launch scope
version: current
previous: /learn/packages/
next: /learn/ai-runtime/
tags: [editor, lsp, cli]
---

# Editor and CLI support

The CLI is the compatibility baseline. LSP and editor adapters add completion, definition, references, hover, diagnostics, rename, and code actions where the adapter is available.

Keep the command loop close to the file:

```bash
kujo check src/main.kujo
kujo format src/main.kujo
kujo lint src/main.kujo
```

When an editor integration behaves differently from the CLI, reproduce the issue with the CLI first and capture the exact version and command.

