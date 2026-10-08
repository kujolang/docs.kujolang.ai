---
title: Agent City
description: Run a local agent task, follow observed work through a pixel-art city, and review the result or replay its evidence.
template: docs
section: Showcases
nav_title: Agent City
order: 48
audience: developer
difficulty: intermediate
status: local scope verified
version: 0.2.0
last_updated: 2026-10-08
scope: local agent workspace
source_repo: agent-city
tags: [showcase, agents, tasks, review, replay]
---

Agent City is a local workspace for running and reviewing AI-agent tasks in a pixel-art city. Connect a model, give an author a task, and ask a separate reviewer to assess the output. The city shows observed Kujo activity and links it to evidence.

## Use it when…

You want to see which tools an agent used, inspect the work it produced, review failed and repaired attempts, or replay a recorded run without executing it again.

## Install and start

Supported platforms are macOS Intel and Apple Silicon, and Linux x64 and ARM64.

```sh
curl --proto '=https' --tlsv1.2 -fsSL https://github.com/kujolang/agent-city/releases/download/v0.2.0/install.sh | sh
```

The installer supplies pinned application and Kujo dependencies, and a private Node runtime when needed. It starts the app at `http://127.0.0.1:5178`, or the address printed in the terminal. Keep the terminal open; Ctrl+C stops the app. Installation does not submit a task.

To start an installed copy again:

```sh
"$HOME/.local/share/agent-city/start.command"
```

Agent City uses its own installer, not `kennel add`. See the [installation guide](https://github.com/kujolang/agent-city/blob/main/installer/README.md) for updates, removal, separate instances, and container setup.

## Connect a model

No model credentials are bundled. Choose one connection:

- **Ollama:** start Ollama with a model installed. Open **Mission Command → Model connection**, choose **Detect local Ollama**, select the model, then **Check model listing** and **Save connection**. A local endpoint that does not require authentication uses a blank API key.
- **Codex CLI:** install and authenticate Codex CLI separately with `codex login`. Leave Agent City running and start the connector in another terminal:

```sh
"$HOME/.local/share/agent-city/start.command" provider:codex --check
"$HOME/.local/share/agent-city/start.command" provider:codex
```

Keep the connector running and restart it after restarting City. If the app uses another address, set `CITY_APP_URL` to the launcher's printed URL. The connector uses your existing CLI login to provide model responses. It does not import Codex tools or projects; account access and usage limits still apply.

## Run a task and review it

1. Open **Mission Command** and choose **Writing + review**.
2. Enter a small request based on facts you supply, then choose **Start mission**.
3. Select the author in the roster and choose **Follow**. The camera tracks that execution across scenes.
4. Answer any actual question in **Mission Conversation → Reply / continue**.
5. Open the mission in history to inspect the draft, separate reviewer response, and saved result. Use **Continue / repair** to request a revision.

Built-in author and reviewer profiles need no import. Execution instances appear when work starts; the roster is not a team of continuously running decorative agents. A reviewer's grade is an opinion, separate from test or execution results.

For a Kujo task, choose **Kujo + senior review (real MCP)**. Enable the sources, tools, and checks you need under **Tools, files and checks**. Try a script that reads a supplied change list and writes Markdown release notes. The [reviewed-tool walkthrough](https://github.com/kujolang/agent-city/blob/main/docs/try-a-reviewed-tool.md) covers the inputs and explicit execution permissions.

## What the rooms mean

| Location | Observed activity |
| --- | --- |
| Dispatch HQ | Task intake and workflow state |
| Workshop / Workcell | Agent work, permitted execution, and artifacts |
| Library / RAG | Retrieval with source classification when metadata supports it |
| MCP Terminal Center | Tool invocation, server, attempt, and result metadata |
| Meeting / Handoff | Supported handoff and relationship evidence |
| Evaluation Dojo | Checks and their actual pass, fail, or skipped outcomes |
| Archive / Incidents | Recorded runs, evidence, replay, and source-health information |

Runtime truth updates immediately. Visual visits may finish later and show **RECENT**. Missing or stale observations remain explicit. A room does not imply that its capability is connected, and ambient motion does not claim a tool call or conversation.

## Replay and record

Open **Archive / Replay / Incidents**, choose a run, and select **Replay pinned run**. Replay preserves event order while shortening long gaps. Pause or restart playback, then choose **Return to live** to submit new work. Replay never calls models or tools.

**Record game video** captures the canvas only. **Stop / save video** downloads WebM, or MP4 where supported. Keep the tab visible. Recordings exclude audio and conversation panels and stop at five minutes or 64 MiB.

[Watch the real 53-second Kujo tool run](https://github.com/kujolang/agent-city/blob/main/evidence/reviewed-release-tool/repaired/release-notes-live.mp4) and [inspect its source evidence](https://github.com/kujolang/agent-city/tree/main/evidence/reviewed-release-tool).

## Permissions and limits

Agent City runs locally. Selected project context goes to the configured model. Provider credentials stay in private server configuration; task text, conversations, and artifacts remain in private runtime state. Normalized telemetry excludes raw prompts, retrieved content, and chat.

Workcell needs a compatible container engine with seccomp and AppArmor. Execution requires explicit permission. Exporting an output does not apply it to your host project. Optional VideoOps rendering and external media services have separate setup and authorization requirements.

Importing profiles does not install their tools or grant permissions. Hosted multi-user operation and an eight-hour reliability qualification are outside this release. Review work before applying or publishing it.

## Related tools and guides

- [Agent City showcase](https://kujolang.ai/ecosystem/agent-city/)
- [Agent City 0.2.0 release](https://github.com/kujolang/agent-city/releases/tag/v0.2.0)
- [Supported workflows](https://github.com/kujolang/agent-city/blob/main/docs/workflow-support.md)
- [First-task guide](https://github.com/kujolang/agent-city/blob/main/TRY-AGENT-CITY.md)
- [VideoOps setup](https://github.com/kujolang/agent-city/blob/main/docs/videoops.md)
