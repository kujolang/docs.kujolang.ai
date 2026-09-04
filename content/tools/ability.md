---
title: Ability
description: Define portable operation contracts, validate cross-language digests, verify signed packs offline, and test approvals with a local fixture kit.
template: docs
section: Tools
nav_title: Ability
order: 69
audience: developer
difficulty: advanced
status: stable runtime; SDK previews
version: 1.1.0
last_updated: 2026-09-04
scope: local-first
source_repo: ability
tags: [tool, contracts, agents, mcp]
---

Kujo Ability gives an operation a stable identity, input and output schemas, declared effects, and retry semantics. Applications bind that definition to handlers and retain control of identity, permissions, credentials, approvals, storage, and transport.

## Install

Ability 1.1.0 requires Kujo 1.2.0 or newer. Install the tagged release with [Kennel](/tools/kennel/) and commit the generated lockfile:

```bash
kujo run /path/to/kennel/kennel.kujo --interpreter -- add github:kujolang/ability@v1.1.0 --alias ability
kujo run /path/to/kennel/kennel.kujo --interpreter -- install
```

```kujo
from ability import validate_ability_definition, ability_definition_digest
```

Use the [complete definition example](https://github.com/kujolang/ability/blob/v1.1.0/examples/content_find.json) to start. It is a documentation fixture, not a built-in content service.

## What the release includes

| Surface | Use and boundary |
| --- | --- |
| Definition and execution contracts | Validate the stable `kujo.ability/v1` definition, bindings, exposures, invocations, policy decisions, approvals, and receipts. |
| Exact registry and runtime | Resolve exact identities and run policy, approval, idempotency, audit, handler, and output checks. Required services fail closed. |
| TypeScript and Python SDK previews | Validate definition envelopes and receipt identity, summarize effects, and share a cross-language definition digest. These local packages are not published SDKs or execution runtimes. |
| Offline pack verifier | Check Ed25519 signatures, artifact checksums, publisher allowlists, revocations, compatibility, effects, contained paths, and tenant visibility. Verification grants no execution permission. |
| Fixture development kit | Validate definitions, render reference docs, simulate request-bound approvals and keyed replay, and inspect receipts through a bounded local fixture server. |

## Digest compatibility

The explicit `sha256-canonical-json-v2` digest agrees across Kujo, TypeScript, and Python. It accepts JSON strings, booleans, null, arrays, objects, and integers within JavaScript's safe range. It rejects decimals and larger integers rather than changing their values.

The existing Kujo runtime and stored receipts keep their original digest. Use the explicit v2 digest for new offline pack trust tooling; do not silently replace live invocation or receipt identity. See the [SDK compatibility notes](https://github.com/kujolang/ability/blob/v1.1.0/docs/SDK.md).

## Try the development kit

Run these commands from an Ability checkout:

```bash
node devkit/cli.mjs validate examples/content_find.json
node devkit/cli.mjs docs examples/content_find.json /tmp/content-find.md
KUJO_ABILITY_DEV_TOKEN='replace-with-a-local-secret' node devkit/cli.mjs serve examples/dev-manifest.json --port 7777
```

The loopback server uses authenticated discovery, approval, and invocation endpoints. Its manifest supplies static fixture outputs. Non-read fixtures need a short-lived, one-time approval bound to the request; keyed fixtures replay matching requests and reject conflicting reuse. It cannot run shell commands, load provider credentials, or serve as a production gateway.

## Connect applications and agents

[CMS](/showcases/cms/) owns domain definitions and application authorization. [Agents SDK](/tools/agents-sdk/) projects definitions into agent tools. [MCP](/tools/mcp/) projects explicitly enabled definitions into MCP tools and maintains the portable host bridge. [SSG](/showcases/ssg/) supplies inspect, validate, and approval-gated build definitions.

An Ability definition describes an operation; it never grants permission. The application must authenticate and authorize requests, persist approvals and audit evidence, isolate tenants, and enforce timeouts at the handler boundary.

## Verify and learn more

```bash
bash tests/run_tests.sh
bash scripts/verify-release.sh
```

The release gate includes cross-language conformance, offline trust checks, fixture execution, available consumer conformance, and Fence architecture checks. See the [release](https://github.com/kujolang/ability/releases/tag/v1.1.0), [runtime guide](https://github.com/kujolang/ability/blob/v1.1.0/docs/RUNTIME.md), [pack trust model](https://github.com/kujolang/ability/blob/v1.1.0/docs/REGISTRY.md), and [development kit guide](https://github.com/kujolang/ability/blob/v1.1.0/docs/DEVKIT.md).
