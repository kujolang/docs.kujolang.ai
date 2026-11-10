---
title: Kujo Hermes
description: Install native Kujo engineering tools in Hermes and inspect approvals, verification results and receipts.
custom_url: kujo-hermes
template: docs
section: Tools
nav_title: Kujo Hermes
order: 238
audience: developer
difficulty: intermediate
status: released
version: 0.1.0
last_updated: 2026-11-10
scope: native Hermes integration
source_repo: kujo-hermes
tags: [tool, hermes, agents, ability, integration]
---

Kujo Hermes connects Hermes directly to canonical Kujo tools. It works with repositories in the languages supported by those tools; it is not limited to writing Kujo code.

## Install in your repository

With Hermes 0.22.7 or newer, Git, and the official Kujo runtime installed, run:

```sh
hermes plugins install kujolang/kujo-hermes
hermes kujo setup --trust-workspace .
```

Accept Hermes's dependency and enable prompts, then start a new conversation. Setup fetches 26 official source repositories at pinned commits and trusts only the workspace you name. It does not install the Kujo runtime, browser binaries, containers or credentials. macOS and Linux are supported; tested Hermes hosts are 0.22.7 and 0.23.0. No npm package or other agent plugin is needed.

## Give Hermes checks it can run

Ask: “Validate the specification, run Eval, and show the failed checks and receipts.”

- **Spec** checks the task contract so Hermes can work against explicit requirements.
- **Eval** runs deterministic checks so you can find regressions and rerun the same tests after a correction.
- **PackWrite** prepares an execution pack so the agent has the task context and constraints together.
- **ShipCheck** reports release-readiness findings so you can review what still needs attention.
- **Scout, PatchBrief and other installed Abilities** help inspect repositories, review changes and gather evidence.

Six native tools handle discovery, inspection, execution, status, receipts and diagnostics. Operation schemas load on demand. Profiles control which Abilities appear; they do not grant permission to execute them. Missing prerequisites remain visible with setup guidance.

## Inspect the evidence

The [checkout demonstration](https://github.com/kujolang/kujo-hermes/tree/main/demo/checkout-video) records a real Hermes conversation using a free local model. Eval catches a checkout regression; the model corrects the code and the unchanged tests pass. Both executions retain inspectable receipts. The edited film condenses model waits.

Receipts preserve structured results and local SHA-256 integrity checks. They are not signed attestations or proof that all possible behavior is correct. A successful process exit does not replace the tool's actual verification verdict.

## Keep execution under your control

Workspace trust and request-bound approvals restrict execution. Approved Eval, Loop and other operations can run repository-defined commands, so use trusted repositories. Ordinary CLI execution is not sandboxed; Workcell needs its own container prerequisites. Remote services and optional telemetry require explicit configuration. Long-running operations support status, cancellation and cleanup.

Run `hermes kujo doctor` for dependency and configuration guidance. The setup command uses Hermes's default in-process plugin mode; isolated host-mode profiles use the documented manual configuration instead. The runtime requirement is Kujo >=1.6,<2; release checks used official Kujo 1.8.0. Some service, browser and container operations remain outside the verified baseline.

## Sources and next steps

- [Kujo Hermes 0.1.0 release](https://github.com/kujolang/kujo-hermes/releases/tag/v0.1.0)
- [Source, configuration and manual installation](https://github.com/kujolang/kujo-hermes)
- [Tested Ability inventory and limitations](https://github.com/kujolang/kujo-hermes/blob/main/docs/abilities.md)
- [Readiness evidence](https://github.com/kujolang/kujo-hermes/blob/main/docs/readiness.md)

[View the ecosystem overview](https://kujolang.ai/ecosystem/kujo-hermes/).
