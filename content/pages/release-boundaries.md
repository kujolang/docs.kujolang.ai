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
last_updated: 2026-09-05
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
