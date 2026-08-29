# Changelog

## Unreleased

### Added

- Document the repository-owned Agent Project lifecycle, profiles, live-provider
  boundary, Workcell path, self-hosted example, and executable workflow with
  automatic `llms.txt` and WebMCP discovery.
- Added a source-backed provider index covering all 25 current Kujo provider packages, immutable release tags, official provider references, authentication boundaries, native APIs, and AI SDK availability.

## [1.2.0] - 2026-08-27

### Changed

- Updated the Dispatch tool page for the Dispatch 1.2 release, including deterministic routing, evaluation, fallback, and persisted route evidence.
- Updated site-wide version markers and release date.

### Added

- Documented the installable `kujo-way-development` skill as the cross-cutting starting point for Kujo project implementation and substantial review.

## [1.1.0] - 2026-08-23

### Added

- Added source-backed guides for Workcell, Source, Redact, Tribunal, Relay, SiteKit, Commerce, SiteProbe, SearchBridge, ContentGraph, StoryDesk, Dossier, BluePencil, GalleyPack, AssetWorks, VersionSeal, PressWire, ReaderSignal, Intake, and Cinch.
- Added current WebOps and publishing-house routes to the ecosystem and path-selection pages.

### Changed

- Fact-checked the language, package, workflow, tooling, showcase, maturity, and deployment claims against current repository contracts.
- Updated installation for the stable Kujo `v1.0.1` release and its published platform binaries and checksums.
- Removed stale fixed repository counts and the unsupported Kujo JIT flag, corrected the DocGen and project-init examples, and replaced the nonexistent generic workflow command.
- Clarified that benchmark guidance is distributed with originating repositories rather than a nonexistent `kujo-benchmarks` repository.
- Marked Leash and Ward as private previews instead of presenting private repositories as public onboarding surfaces.
- Made the SSG checkout path configurable through `SSG_ROOT` for reproducible builds outside the original sibling layout.
- Ranked search results by exact and prefix title matches before broader body-text matches.
- Replaced the generic favicon with the official Kujo K logomark and added SVG, ICO, PNG, Apple touch, Android web-app, Windows tile, and web manifest assets.
- Reworked the mobile header with Tabler menu and theme icons, persistent header search, and a light/dark mode toggle.
- Updated the footer with the Kujo wordmark and current Docs version.
- Simplified the header brand to the K logomark and Docs label, reordered the mobile controls, and added IDE-style syntax highlighting to code blocks.
- Styled code-block scrollbars, pinned copy controls outside horizontal scrolling, and replaced copy text with Tabler icons.

All notable changes to Kujo Docs are documented here.

## [1.0.0] - 2026-08-08

### Added

- Official information architecture for learning Kujo, building applications, reviewing work, browsing tools, and exploring showcases.
- Thirty repository-backed ecosystem guides with CLI, API, workflow, artifact, and boundary overviews.
- Local search, generated sitemap, public `llms.txt`, robots policy, and themed catchall 404 page.
- Departure Mono typography, Kujo logomark, black-and-white visual system, and responsive layouts.

### Changed

- Replaced the compact mobile dropdown with an accessible full-screen navigation overlay.
- Promoted the site from launch draft to the official documentation at `docs.kujolang.ai`.

### Fixed

- Code-copy controls now work across the home hero and generated code blocks.
- Nested-page footer links, Markdown tables, route ordering, duplicate page titles, and missing-route behavior.
