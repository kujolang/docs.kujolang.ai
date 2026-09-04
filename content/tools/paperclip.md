---
title: Kujo for Paperclip
description: Add focused context, change review, and reproducible failure evidence to Paperclip tasks.
template: docs
section: Tools
nav_title: Paperclip
order: 255
audience: developer
difficulty: beginner
status: released
version: 0.1.7
last_updated: 2026-09-04
scope: local Paperclip integration
source_repo: paperclip
previous: /tools/howl/
next: /tools/site-kit/
tags: [tool, agents, context, review, evidence]
---

## Use it when…

Paperclip agents need a small, visible set of repository context, a clear review of change scope, or a safe record of failed command output.

Kujo works in Paperclip's current task view. You do not need the Classic Task Interface.

## Install

You need Paperclip `2026.824.1` or later and Node.js `24.11.0` or later.

```bash
npx paperclipai plugin install @kujolang/paperclip
```

Restart Paperclip if it is already running, then open an issue. The Kujo workspace appears in the task view. You can also open the **Kujo** tab on project, issue, and run pages.

The npm package includes the right Kujo runtime for supported macOS, Linux, and Windows systems. You do not need a separate Kujo install or Kujo API key.

## Interface overview

| Surface | What it does |
| --- | --- |
| Context Pack | Uses Scent to select a bounded, task-specific file set before broad reading |
| Review Pack | Uses ChangeBucket and PatchBrief to measure scope, show risk signals, and prepare a handoff |
| Failure Evidence | Uses CaseFile to save supplied command details and bounded logs with sensitive values redacted |
| Agent tools | Exposes four Paperclip tools for context selection, approved file reads, change review, and failure capture |

## First use

1. Open the Paperclip issue you want to work on.
2. Create a focused Context Pack.
3. Make and test the change with the repository's normal tools.
4. Create a Review Pack.
5. Save Failure Evidence when a command fails.

The plugin stores the latest result in Paperclip plugin state. It does not write reports into the repository.

## Agent tools

| Tool | Use |
| --- | --- |
| `kujolang.paperclip:get-context` | Select files at minimal, focused, or broad depth |
| `kujolang.paperclip:get-context-content` | Read safe content only from files selected by that Context Pack |
| `kujolang.paperclip:review-changes` | Measure a working tree or Git range and create a review handoff |
| `kujolang.paperclip:capture-failure` | Save supplied command output as redacted evidence without running it |

```text
Use kujolang.paperclip:get-context with task "trace the OAuth callback" and depth "focused".
Read only the selected files needed for the change.
Use kujolang.paperclip:review-changes after the edit.
If a check fails, use kujolang.paperclip:capture-failure with the command, exit code, and bounded log.
```

## Safety boundary

The worker starts child processes without a shell, uses a canonical Paperclip workspace, caps time and output, and passes a small environment. The content tool rejects files outside the matching Context Pack, traversal, symlink escapes, binary files, and oversized files. Failure Evidence never runs a command.

Suggested checks remain suggestions until another system records that they ran.

## Current install note

Use the unversioned package name in the install command for now. Current Paperclip releases mishandle an exact version suffix on scoped npm packages. The fix is under review in [paperclipai/paperclip#12745](https://github.com/paperclipai/paperclip/pull/12745). Normal installation and use are not blocked.

## Reference

Read the [Kujo for Paperclip repository](https://github.com/kujolang/paperclip), [complete usage guide](https://github.com/kujolang/paperclip/blob/v0.1.7/docs/USAGE.md), [compatibility contract](https://github.com/kujolang/paperclip/blob/v0.1.7/docs/COMPATIBILITY.md), and [v0.1.7 release](https://github.com/kujolang/paperclip/releases/tag/v0.1.7).
