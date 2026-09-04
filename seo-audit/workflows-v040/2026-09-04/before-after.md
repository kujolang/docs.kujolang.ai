# Before and after

Audit date: 2026-09-04

Immediate technical evidence only; search outcomes require post-deployment data and elapsed time.

| Measure | Before | After | Result |
| --- | ---: | ---: | --- |
| Canonical pages | 98 | 98 | No coverage loss |
| Production 200 pages | 98 | 98 | Pass |
| Indexable pages | 98 | 98 | Pass |
| Sitemap URLs | 98 | 98 | Exact parity |
| Missing / duplicate titles | 0 / 2 | 0 / 0 | Fixed |
| Missing / duplicate descriptions | 0 / 8 | 0 / 0 | Fixed |
| H1 issues | 0 | 0 | Pass |
| Missing / mismatched canonicals | 0 / 0 | 0 / 0 | Pass |
| Broken internal links | 2 | 0 | Fixed |
| Orphans / pages deeper than 3 clicks | 0 / 0 | 0 / 0 | Pass |
| Images missing alt / dimensions | 0 / 196 | 0 / 0 | Fixed |
| Schema parse errors / coverage | 0 / 98 | 0 / 98 | Pass |
| Confirmed external 404 occurrences | 2 | 2 | Owner decision required |
| Redirect issues / crawler-access issues | 0 / 0 | 0 / 0 | Pass |
| Internal technical-readiness heuristic | 83/100 | 94/100 | Improved |
| Internal AI-search-readiness heuristic | 78/100 | 86/100 | Improved |

The internal scores weight crawlability, indexability, metadata, structure,
structured data, media hygiene, source clarity, crawler access, and unresolved
evidence. They exist only to compare this audit's before and after states; they
are not Google, Bing, or AI-platform scores.

Representative after Lens runs found no accessibility violations, horizontal
page overflow, failed internal links, console errors, or failed requests at
desktop or 390px mobile. All four observed load-event timings improved in this
lab run, from 1,716–1,819 ms before to 1,528–1,603 ms after. This is not field
Core Web Vitals or causal proof.
