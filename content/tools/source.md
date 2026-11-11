---
title: Source
description: Run Source 0.2.0 to connect Git proposals with tasks, agent sessions, evidence and authorized review decisions.
template: docs
section: Tools
nav_title: Source
order: 27
audience: developer
difficulty: advanced
status: experimental release
version: "0.2.0"
last_updated: "2026-11-10"
scope: local evaluation and deployment integration
source_repo: source
tags: [tool, git, collaboration, agents]
---

## Use it when

You need to trace an agent's proposed Git change through its task, session, evidence and review decision. Source provides a browser UI, CLI, HTTP API and scoped Git access around the same workflow.

## Install and run

Source is public and MIT-licensed. Use Node.js 22.23.4+, 24.22.1+, or 26.12.1+ on supported branches, npm and Git:

```bash
git clone --branch v0.2.0 https://github.com/kujolang/source.git
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

## Use Source alongside GitHub

Create an empty Source repository whose default branch matches your local repository. Issue a project-scoped capability with `read_source`, `git_push` and `submit_change`, and set its returned credential in `SOURCE_CREDENTIAL`. Never embed credentials in a remote URL.

From the existing repository, run the CLI using the path to your Source checkout:

```bash
node /path/to/source/bin/source.js sync --url https://source.example.com/git/O1/P1/R1.git
node /path/to/source/bin/source.js sync --dry-run
node /path/to/source/bin/source.js sync
```

Replace the URL and IDs with your instance. GitHub stays `origin`; Source uses the `source` remote. Sync copies local branches and tags in one atomic push without force or deletion. It preserves upstream tracking. GitHub-only branches, LFS objects, issues and pull requests are not imported. Use `--cwd /path/to/repo` for additional repositories and `--remote NAME` for an explicit remote.

After the initial sync, create and commit a new feature. Submit it before syncing that commit onto Source's default branch:

```bash
node /path/to/source/bin/source.js submit --intent "Describe the change"
```

Sync does not produce review evidence and cannot bypass broker protection. See the [complete setup](https://github.com/kujolang/source/blob/v0.2.0/README.md#keep-github-as-origin).

## Candidates, verification and recovery

Source assembles compatible proposals using real Git merge semantics, schedules policy-selected checks through durable PostgreSQL workers, and requires valid evidence and authorized acceptance for the exact candidate before protected promotion. Reuse is bound to candidate, policy, tool, environment and input identity; a similar diff alone is insufficient.

For authenticated submissions to PostgreSQL-backed instances, retain a unique key:

```bash
node /path/to/source/bin/source.js submit --submission-key feature-123 --intent "Add feature"
# After a lost response, read the committed original result without fetching or pushing.
node /path/to/source/bin/source.js submit --submission-key feature-123 --recover
```

The key is scoped to the project and principal. Conflicting reuse returns 409. Recovery requires a current capability even on public projects. A missing receipt can race an in-flight request, so do not invent another key after a lost response. Git upload precedes the atomic database lifecycle; unkeyed submissions have no new recovery guarantee. See the [full contract](https://github.com/kujolang/source/blob/v0.2.0/docs/source/18-source-submit.md).

## Cloudflare profile

`npm run demo:hybrid` runs real Source, Worker handlers and Git with an emulated Artifacts service. To use live Cloudflare, follow the [hybrid setup guide](https://github.com/kujolang/source/blob/v0.2.0/docs/contest/HYBRID.md) with your own Workers/Artifacts access and securely supplied credentials.

The [verified live demo](https://github.com/kujolang/source/blob/v0.2.0/docs/contest/CLOUDFLARE_LIVE.md) keeps Source and review data local. A deployed Worker creates repositories and issues short-lived credentials; accepted changes reach canonical Git on Artifacts. Expected-tip checks and retry reconciliation protect against stale updates and lost push acknowledgments.

## Verification and limits

Run `npm test`, `npm run test:cloudflare` and `npm run demo:hybrid` for local checks. PostgreSQL and container gates have separate prerequisites documented in the repository.

Version 0.2.0 is an experimental release, not a production-readiness certification. JSON is single-process. Exposed serving requires PostgreSQL, shared durable Git storage, TLS, writer fencing and deployment-specific validation. Synchronous PostgreSQL maintenance is not atomic across records. Worker timeout does not guarantee cancellation of arbitrary action handlers. Review historical requester credentials and evidence fidelity before upgrading an affected deployment.

Local evidence covers real Source history, OCI component checks, Lens browser staging, worker crash recovery and coordinated Git/PostgreSQL restore. These are bounded local demonstrations, not host/power-loss, deployed failover, sustained production capacity or 1,000-agent end-to-end certification. See [hosting readiness](https://github.com/kujolang/source/blob/v0.2.0/docs/architecture/hosting-readiness.md).

Before upgrading, back up and restore-test Git and PostgreSQL together and drain writers/workers. Reassemble legacy candidates and redispatch verification under the current assembly contract rather than promoting stale receipts.

## Reference

- [Public repository](https://github.com/kujolang/source)
- [Source 0.2.0 release](https://github.com/kujolang/source/releases/tag/v0.2.0)
- [Ecosystem page and hero](https://kujolang.ai/ecosystem/source/)
- [Hardening and verification record](https://github.com/kujolang/source/blob/v0.2.0/docs/audits/repository-hardening.md)
- [Deployment guide](https://github.com/kujolang/source/blob/v0.2.0/docs/source/23-tls-deployment.md)
