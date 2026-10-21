---
title: Source
description: Run Source 0.1.1 to connect Git proposals with tasks, agent sessions, evidence and authorized review decisions.
template: docs
section: Tools
nav_title: Source
order: 27
audience: developer
difficulty: advanced
status: experimental release
version: "0.1.1"
last_updated: "2026-10-21"
scope: local evaluation and deployment integration
source_repo: source
tags: [tool, git, collaboration, agents]
---

## Use it when

You need to trace an agent's proposed Git change through its task, session, evidence and review decision. Source provides a browser UI, CLI, HTTP API and scoped Git access around the same workflow.

## Install and run

Source is public and MIT-licensed. Use Node.js 22, npm and Git:

```bash
git clone --branch v0.1.1 https://github.com/kujolang/source.git
cd source
npm ci
npm run demo:contest -- --trace
```

This local demo needs no Cloudflare account, PostgreSQL server or AI API key. Three scripted contributors create real commits and proposals. The demo checks approval denials, stale updates, conflict recovery and accepted promotion.

To inspect the result, use the directory printed by the command:

```bash
npm run demo:serve -- .contest-demo/run-XXXXXX
```

Open http://127.0.0.1:8787. Read the login IDs and password from that run's local `operator.json`. Keep this file private. Stop the server with Ctrl-C; each demo run has its own directory.

Source uses Git and npm. It is not an npm registry publication or a Kennel-installable Kujo package.

## Review and promotion

Source records `Work → Session → Change → Evidence → Decision → Canonical Git`. Contributors receive scoped capabilities. They can propose changes and attach checks; an authorized reviewer decides what may become canonical. Source rejects stale promotions and retains the revision history.

## Cloudflare profile

`npm run demo:hybrid` runs real Source, Worker handlers and Git with an emulated Artifacts service. To use live Cloudflare, follow the [hybrid setup guide](https://github.com/kujolang/source/blob/v0.1.1/docs/contest/HYBRID.md) with your own Workers/Artifacts access and securely supplied credentials.

The [verified live demo](https://github.com/kujolang/source/blob/v0.1.1/docs/contest/CLOUDFLARE_LIVE.md) keeps Source and review data local. A deployed Worker creates repositories and issues short-lived credentials; accepted changes reach canonical Git on Artifacts. Expected-tip checks and retry reconciliation protect against stale updates and lost push acknowledgments.

## Verification and limits

Run `npm test`, `npm run test:cloudflare` and `npm run demo:hybrid` for local checks. PostgreSQL and container gates have separate prerequisites documented in the repository.

Version 0.1.1 is an experimental release, not a production-readiness certification. JSON is single-process. Exposed serving requires PostgreSQL, shared durable Git storage, TLS, writer fencing and deployment-specific validation. Synchronous PostgreSQL maintenance is not atomic across records. Worker timeout does not guarantee cancellation of arbitrary action handlers. Review historical requester credentials and evidence fidelity before upgrading an affected deployment.

## Reference

- [Public repository](https://github.com/kujolang/source)
- [Source 0.1.1 release](https://github.com/kujolang/source/releases/tag/v0.1.1)
- [Ecosystem page and hero](https://kujolang.ai/ecosystem/source/)
- [Hardening and verification record](https://github.com/kujolang/source/blob/v0.1.1/docs/audits/repository-hardening.md)
- [Deployment guide](https://github.com/kujolang/source/blob/v0.1.1/docs/source/23-tls-deployment.md)
