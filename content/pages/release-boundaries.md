---
title: Release boundaries
description: Read the difference between release-ready within scope, preview, dogfood, and technical showcase.
custom_url: release-boundaries
template: docs
section: Reference
nav_title: Release boundaries
order: 100
audience: all
difficulty: beginner
status: stable
version: current
last_updated: 2026-09-09
tags: [release, maturity, scope]
---


The docs use maturity labels beside recommendations so a reader can make an informed choice.

| Label | Means |
| --- | --- |
| **Launch scope** | The smallest local workflow has a current source-backed proof. |
| **Preview / dogfood** | Useful for evaluation and local teams; broader proof or wording is still in progress. |
| **Showcase** | Demonstrates a pattern or application surface without promising a hosted service. |
| **Release-candidate onboarding** | The source path is verified while public artifacts, checksums, or clean-machine proof are pending. |
| **Stable within scope** | The documented local contract is released and verified; deployment-specific controls still belong to the adopter. |

Always check the page's **Status** and **Scope** fields plus the linked repository's release notes. A version number or passing local build is not a blanket enterprise-readiness claim.

## Runtime upgrade compatibility

[`kujo upgrade`](/upgrade/) is available in v1.3.0 and later. Users of earlier runtimes must install a current version through the existing installer or original package manager before using the command. Native upgrades cover only the standalone runtime executable; ecosystem sources and package pins retain their own update workflows. Docs-site version numbers are independent of runtime releases.

## Current ecosystem versions

Use the [dated ecosystem release overview](/ecosystem/releases/) to distinguish published GitHub Releases, tagged provider packages, and newer default-branch development. A repository badge or version file alone does not prove a release was published.

## Kujo 1.6 runtime versus experimental contracts

The Kujo **1.6.0 runtime is released** for Linux x64/arm64, macOS x64/arm64 and Windows x64 through native archives and npm. That runtime release does not stabilize companion protocols.

- **Wave C:** experimental beta, explicit opt-in, required/deny in a bounded single-effect domain; alpha compatibility is retained.
- **Wave D:** experimental alpha generic handoffs and participant SDK APIs, using trusted local hosts. Participant SDK packages remain private/unpublished.
- **Authority:** participants carry evidence and completion knowledge. Dispatch owns review and replay admission; correlation is not authorization.

No exactly-once, universal rollback, general machine-loss recovery, remote participant trust, multi-effect assurance or stable participant SDK is claimed. Source-blind agent adopter rehearsal passed; human adopter usability remains post-release validation.
