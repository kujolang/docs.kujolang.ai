---
title: PackWrite
description: Compile a repository mega prompt and bounded context into deterministic execution packs for implementation agents and reviewers.
template: docs
section: Tools
nav_title: PackWrite
order: 210
audience: developer
difficulty: intermediate
status: released
version: 1.1.0
last_updated: 2026-09-04
scope: local-first
source_repo: packwrite
previous: /tools/shipcheck/
next: /tools/casefile/
tags: [tool, agents, packs, planning, review]
---


## Use it when…

You have a substantial project brief, feature plan, or repository migration that is too large to trust to one transient chat. PackWrite turns that intent into a versionable `agent/` operating manual with bounded phases, acceptance criteria, handoff state, decisions, and reviewer guidance.

PackWrite is local-first and AI-assisted. It compiles the pack; it does not implement the project.

## Interface overview

| Surface | What is available |
| --- | --- |
| Generate | `packwrite init [file]` builds an `agent/` pack from `MEGA_PROMPT.md` |
| Preview | `packwrite init MEGA_PROMPT.md --dry-run` calls the model and validates its manifest without writing |
| Validate | `packwrite validate` checks pack structure deterministically; `--json` supports CI |
| Summarize | `packwrite summary` reports phase count, missing files, warnings, and the next command |
| Diagnose | `packwrite doctor` explains prompt, provider, endpoint, credential, and output state; `--strict` fails on blockers |
| Prompts | `packwrite prompt deepseek` prints the implementation handoff; `prompt codex-review` prints the independent review handoff |
| Configuration | `packwrite config` shows the resolved defaults, global config, project config, and CLI overrides |
| Automation | `--quiet`, JSON status, and fake-response inputs support offline tests and CI |

## Main workflows

1. Write `MEGA_PROMPT.md` with purpose, users, use cases, non-goals, architecture guardrails, and a definition of done.
2. Run `doctor --strict` before spending a provider call.
3. Preview generation with `--dry-run`.
4. Generate and inspect the repository-local `agent/` pack.
5. Run deterministic validation and summary checks.
6. Hand the implementation prompt to an agent, then use the separate review prompt for independent verification.

## Five-minute example

```bash
packwrite doctor --strict
packwrite init MEGA_PROMPT.md --dry-run
packwrite init MEGA_PROMPT.md --provider deepseek --model deepseek-v4-pro
packwrite validate
packwrite summary
packwrite prompt deepseek
packwrite prompt codex-review
```

The launcher preserves your current working directory, so configuration discovery and pack output belong to the repository where you run it.

## Install and run

PackWrite is written in Kujo and requires the `kujo` interpreter. Clone the repository and run its launcher directly, or install the launcher symlink:

```bash
git clone https://github.com/kujolang/packwrite.git
cd packwrite
./bin/packwrite --help
make install
packwrite version
```

API keys are environment variables only. PackWrite checks `PACKWRITE_API_KEY` first and then provider-specific variables such as `DEEPSEEK_API_KEY` and `OPENAI_API_KEY`.

## What you get

The default pack is:

```text
agent/
  MASTER.md
  TODO.md
  HANDOFF.md
  DECISIONS.md
  REVIEW_CHECKLIST.md
  DEEPSEEK_START.md
  CODEX_REVIEW_PROMPT.md
  phases/
    00-project-brief.md
    01-*.md
```

`MASTER.md` holds stable intent. Phase files define scope and acceptance criteria. `HANDOFF.md` and `DECISIONS.md` preserve mutable run state. The checklist and two prompts separate implementation from review.

Optional prompt and review files are controlled by `[pack]` settings and remain part of validation when enabled.

## Configure PackWrite

Resolution order is:

```text
defaults < ~/.config/packwrite/config.toml < ./packwrite.toml < CLI flags
```

```toml
[prompt]
file = "MEGA_PROMPT.md"

[output]
dir = "agent"
overwrite = false

[model]
provider = "deepseek"
model = "deepseek-v4-pro"
temperature = 0.1

[repo_context]
include = ["README.md", "src", "tests", "docs"]
exclude = [".env", ".git", "node_modules", "dist", "build"]

[pack]
min_phases = 6
max_phases = 12
include_deepseek_prompt = true
include_codex_review_prompt = true
include_review_checklist = true
```

`[output].mode` and `--run-name` are reserved in 1.1 and do not yet drive execution behavior.

## Providers

The adapter speaks the OpenAI-compatible chat-completions protocol. Built-in endpoint presets cover DeepSeek, OpenAI, and a local compatible server. Other providers require an explicit `--endpoint` pointing to an OpenAI-compatible gateway.

Anthropic is not a native endpoint in 1.1 because its API uses a different protocol. Use an explicit compatible gateway when you need Claude or another non-compatible provider.

## Safe generation and overwrite

- Repository context is bounded and skips common dependency, build, and secret-looking paths by default.
- Output directories must be non-empty relative paths that cannot escape the project.
- Generated file paths reject traversal, backslash ambiguity, home expansion, control characters, symlink ancestors, and secret-looking names.
- Model output must be a JSON object with a non-empty `files` array of string paths and content.
- Response size and diagnostics are bounded before writes.
- `--overwrite` stages a clean replacement, validates it, promotes it atomically, prunes stale files, and rolls back a failed promotion.
- `--save-raw-response` is explicit, owner-only, and no-overwrite because model payloads can contain sensitive context.

## Offline and CI use

Use a reviewed fake response to exercise the complete write and validation path without credentials or network access:

```bash
export PACKWRITE_FAKE_RESPONSE_FILE=/path/to/manifest.json
packwrite init MEGA_PROMPT.md
packwrite validate --json
packwrite doctor --strict --json
```

`PACKWRITE_FAKE_RESPONSE` also accepts an inline manifest. `packwrite init --quiet` suppresses successful progress and summary output while keeping errors visible.

## How it fits

Use [Spec](/tools/spec/) to define a precise task contract, [Scent](/tools/scent/) to prepare focused context, PackWrite to compile the execution manual, [Muzzle](/tools/muzzle/) for quiet repeatable runs, and the [workflow catalog](/collections/workflows/) to evaluate and record bounded implementation work.

## Boundaries

PackWrite 1.1.0 is a released local/team workflow compiler, not a hosted agent platform. It does not supply SaaS authentication, organization policy, multi-user coordination, audit storage, signing, deployment controls, or a universal provider protocol. Generated packs still require review for scope, authority, model configuration, repository constraints, and real release gates.

## Reference

See the [PackWrite repository](https://github.com/kujolang/packwrite), [v1.1.0 release](https://github.com/kujolang/packwrite/releases/tag/v1.1.0), [configuration reference](https://github.com/kujolang/packwrite/blob/v1.1.0/docs/CONFIGURATION.md), and [end-to-end guide](https://github.com/kujolang/packwrite/blob/v1.1.0/docs/HOWTO.md).
