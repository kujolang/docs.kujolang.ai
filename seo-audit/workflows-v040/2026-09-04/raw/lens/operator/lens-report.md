# Lens Report

Status: PASS
URL: https://docs.kujolang.ai/build/publishing-house-operator/
Started: 2026-09-04T14:45:05Z
Finished: 2026-09-04T14:45:32Z
Duration: 27309ms
Viewports: desktop, mobile
Output Directory: /Users/robertdevore/2026/Kujolang/kujo-repos/docs.kujolang.ai/seo-audit/workflows-v040/2026-09-04/raw/lens/operator

## Summary

Status: PASS
Total findings: 5
Critical: 0
Errors: 0
Warnings: 5
Info: 0
Fail threshold: error
Exit code: 0
Checks run: 10
Checks skipped: 0
Artifacts written: 11

Lens completed successfully. No findings met the configured fail threshold of `error`. Runtime artifacts were captured.

## Critical Issues

No critical issues found.

## Errors

No errors found.

## Warnings

- **LENS-FINDING-001** — Browser evidence capture reached a safety limit
  Lens omitted 0 console message(s), 0 network event(s), and 14 link(s) after reaching configured hard bounds.
  Evidence: metadata.json provider.evidence_limits

- **LENS-CONSOLE-001** — Console warning: Deprecated API for given entry type.
  Browser console warning during page load. Viewport: desktop
  Evidence: console.json entry 1

- **LENS-CONSOLE-002** — Console warning: Deprecated API for given entry type.
  Browser console warning during page load. Viewport: desktop
  Evidence: console.json entry 2

- **LENS-CONSOLE-003** — Console warning: Deprecated API for given entry type.
  Browser console warning during page load. Viewport: mobile
  Evidence: console.json entry 3

- **LENS-CONSOLE-004** — Console warning: Deprecated API for given entry type.
  Browser console warning during page load. Viewport: mobile
  Evidence: console.json entry 4


## Evidence

Runtime evidence collected:

- Screenshots: `screenshots/desktop.png`, `screenshots/mobile.png`
- Console log: `console.json`
- Network log: `network.json`
- DOM summaries: `dom-summary.json`
- Link check results: `links.json`

- Accessibility results: `accessibility.json`

## Accessibility

Accessibility checks were enabled for this run.

- Engine: axe-core 4.11.4
- Scans completed: 2
- Violations found: 0
- Results: `accessibility.json`

No accessibility violations were detected by automated scanning.
Automated checks cannot detect all accessibility issues. Manual review
and screen reader testing are still essential.

Accessibility checks use axe-core automated rules. They do not guarantee
WCAG compliance and are not a substitute for manual accessibility review.

## Suggested Repair Tasks

1. Reduce page noise or inspect the application with a purpose-built trace before relying on conclusions that require the omitted evidence.

2. Review the warning in console.json entry 1.

3. Review the warning in console.json entry 2.

4. Review the warning in console.json entry 3.

5. Review the warning in console.json entry 4.


## Agent Repair Brief

Lens failed because 0 finding(s) met the configured fail threshold of `error`.

The page loaded successfully. Secondary findings (console, network, overflow, links) can be trusted.

Viewports tested: desktop, mobile.

Link check enabled: all checked links passed.

First artifacts to inspect:

Suggested first pass:
1. Reduce page noise or inspect the application with a purpose-built trace before relying on conclusions that require the omitted evidence.
2. Review the warning in console.json entry 1.
3. Review the warning in console.json entry 2.
4. Review the warning in console.json entry 3.
5. Review the warning in console.json entry 4.

Do not assume the root cause is framework-specific unless the source code or console output proves it. Each finding includes evidence references — inspect those artifacts before drawing conclusions.

## Artifacts

- `lens-report.md`
- `lens-report.json`
- `metadata.json`
- `console.json`
- `network.json`
- `dom-summary.json`
- `metrics.json`
- `screenshots/desktop.png`
- `screenshots/mobile.png`
- `links.json`
- `accessibility.json`
