---
title: Presentations
description: Browser-native slide decks with static routes, reading and print editions, presenter tools, and optional motion.
template: docs
section: Showcases
nav_title: Presentations
order: 45
audience: developer
difficulty: intermediate
status: preview
version: 0.3.0
last_updated: 2026-10-03
scope: optional presentation package
source_repo: presentations
previous: /showcases/ssg/
next: /showcases/totalrecall/
tags: [showcase, presentations, slides, publishing, sitekit]
---

Kujo Presentations turns structured deck source into a browser-native static site. Each deck gets numbered slide URLs, an overview, a reading edition, print and PDF output, and an optional presenter console. The source stays in normal files instead of a proprietary presentation format.

## Use it when…

You need a deck that can be reviewed in Git, hosted as static files, read without the slide canvas, and extended with local themes, layouts, or motion.

## Interface overview

| Surface | What is available |
| --- | --- |
| Authoring | `deck.json`, `BRIEF.md`, local assets, deck themes, ten reusable layouts, and purpose-specific starters |
| Generated site | Overview, numbered slide routes, linked thumbnails, reading edition, print route, and a themed 404 page |
| Viewer | Keyboard and touch navigation, history, slide-only fullscreen, reduced-motion support, and optional local Motion bundles |
| Presenter tools | Current and next slide previews, audience-window control, timer, direct slide selection, and private notes loaded in the presenter tab |
| Review | Ready checks, Chromium inspection, slide screenshots, accessibility checks, geometry checks, and host verification |

## Main workflows

- Start from the `investor`, `live-talk`, or `sales` starter, then replace every placeholder with sourced facts and approved media.
- Run the ready check before building so unfinished placeholders fail early.
- Build the deck into static HTML, CSS, images, fonts, and SVG, then review the overview, slide routes, reading edition, and print output.
- Inspect the generated deck in Chromium and test the deployed host separately before presenting or sharing it.

## Five-minute example

Install Git, Node 20 or newer, and Kujo 1.5 or newer, then run:

```bash
git clone https://github.com/kujolang/presentations.git
cd presentations
npm run deck -- start investor my-pitch --title "My company"
```

The command creates `decks/my-pitch/`, installs the pinned SSG and SiteKit dependencies, builds the deck, and starts a local preview. The starter is a draft: replace its placeholders before you treat it as ready.

## What you get

The package keeps slides as real static pages. Overview and reading routes work without JavaScript. The viewer adds shortcuts, fullscreen, and optional motion while preserving normal links and history. A repeatable Chromium export can produce a visual PDF; the HTML reading edition remains the accessible, reflowing version.

Agents can use the repository's `CREATE_A_DECK.md`, starter catalog, JSON Schema, layout limits, and readiness checks. Those contracts help an agent build within the supported system, but they do not verify claims, approve media, or judge the story.

## How it fits

Presentations is an optional layer on [SSG](/showcases/ssg/) and SiteKit. SSG supplies static routes and asset copying. SiteKit supplies tokens, layout utilities, controls, and focus styles. Presentations owns slide layouts, validation, canvas geometry, controls, presenter tools, and motion. Neither upstream project depends on it.

Explore the [live presentation examples](https://presentations.kujolang.ai/) to see the generated output.

## Boundaries

Version 0.3.0 is a preview distributed as source through GitHub releases; it is not published to npm. Native authoring and build tools are verified on macOS and Linux, not Windows. Automated browser and accessibility checks do not replace human screen-reader, language, or presentation review.

Generated decks are static files. Presentations does not provide accounts, tenant isolation, hosted rendering, or server-side access control. Use a trusted build workspace, keep private files outside the published asset tree, and put confidential decks behind host-level authentication.

## Reference

- [Kujolang.ai Presentations showcase](https://kujolang.ai/ecosystem/presentations/)
- [Presentations repository](https://github.com/kujolang/presentations)
- [Presentations 0.3.0 release](https://github.com/kujolang/presentations/releases/tag/v0.3.0)
- [Getting started](https://github.com/kujolang/presentations/blob/v0.3.0/docs/getting-started.md)
- [Authoring guide](https://github.com/kujolang/presentations/blob/v0.3.0/docs/authoring.md)
- [Feature and presenter-tool guide](https://github.com/kujolang/presentations/blob/v0.3.0/docs/presentation-features.md)
- [Support matrix](https://github.com/kujolang/presentations/blob/v0.3.0/docs/support-matrix.md)
