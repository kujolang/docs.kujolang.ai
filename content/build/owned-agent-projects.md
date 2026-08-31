---
title: Repository-owned Agent Projects
description: Install Kujo's agent platform, create a repository-owned agent, and prove its local lifecycle.
custom_url: owned-agent-projects
template: docs
section: Build with Kujo
nav_title: Owned Agent Projects
order: 8
audience: developer
difficulty: beginner
status: stable
version: 1.1.0
last_updated: 2026-08-30
next: /build/agent-profiles/
tags: [ai, agents, projects, build]
---

An Agent Project keeps the agent in your repository. Its instructions, model preference, skills, tools, knowledge, policies, workflows, evaluation, exact dependency pins, and runtime boundaries remain reviewable files instead of hidden hosted state.

## Install the focused agent toolchain

```bash
curl -fsSL https://kujolang.ai/install.sh | bash -s -- --group agent
export PATH="$HOME/.local/bin:$PATH"
```

The public installer downloads published Kujo `v1.1.0` release assets, verifies their checksums, and installs the focused Agent Project dependencies.

## Create and run an agent

```bash
kujo agent new my-agent --profile basic --install
cd my-agent
kujo agent run "What can you help me with?"
```

The `basic` profile is deterministic and offline by default. It needs no API key, provider network, Watchdog, or RunLedger. The `--install` flag resolves the exact Kennel dependency pins after scaffolding so the project is ready to run.

## Prove the complete local lifecycle

```bash
kujo doctor agent --deep
kujo agent inspect
kujo agent eval
```

There is deliberately no `kujo agent doctor`. Agent diagnostics extend Kujo's canonical Doctor architecture through `kujo doctor agent`. Use `--json` with Doctor, Inspect, Run, or Eval when automation needs a versioned machine result.

`agent.project.json` is the root contract. Kujo discovers the project from a nested directory without crossing a Git boundary, validates every referenced path stays inside the project, and uses immutable Kennel pins instead of sibling checkout dependencies.

## Continue building

- [Choose an Agent Project profile](/build/agent-profiles/)
- [Store provider keys and connector credentials](/build/agent-credentials/)
- [Operate, evaluate, and harden an agent](/build/agent-operations/)
- [Explore agent examples and starter sets](https://agents.kujolang.ai/)

The working sources are the [self-hosted example](https://github.com/kujolang/kujo/tree/main/examples/owned-agent-project), the [lifecycle workflow](https://github.com/kujolang/kujo-workflows/tree/main/owned-agent-project), and the [implementation guide](https://github.com/kujolang/kujo/blob/main/docs/BUILD_AN_AGENT.md).

This page appears in `llms.txt` and the static WebMCP index. Those discovery surfaces expose documentation only; they never grant execution authority.
