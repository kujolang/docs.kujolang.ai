# Executive summary

Audit date: 2026-09-04

## Overall status

PASS WITH RECOMMENDATIONS

## Where the site was

The preserved v1.3.2 deployment exposed 98 canonical, indexable pages. All 98
returned 200 and appeared in the sitemap, with valid H1s, canonicals,
structured data, crawl depth, and alt text. The internal technical-readiness
score was 83/100 and AI-search-readiness score was 78/100. These are audit
heuristics for before/after comparison, not search-engine scores.

## What was wrong

- Two rendered task links pointed to routes the documentation did not generate.
- Eight pages reused a generic section description, and two separate pages used
  the same `Showcases` title.
- Both shared brand images omitted intrinsic dimensions on every page, for 196
  affected occurrences.
- Two public links led to GitHub repositories that return 404 anonymously.
- Search-console, analytics, field-performance, backlink, and controlled
  AI-answer measurements were unavailable.

## What changed

- The two internal links now point to `/review/` and `/tools/rag/`.
- Seven section landing pages now have distinct descriptions, and the ecosystem
  listing is titled `Showcase Directory`.
- Both shared brand images now render with 32-by-32 intrinsic dimensions.
- The docs contract now asserts the repaired links, metadata, and image
  dimensions. Docs v1.3.3 was built cleanly and deployed through `gh-pages`.

## Where the site is now

The independent after crawl passes all tested technical gates across all 98
canonical pages: zero duplicate titles or descriptions, broken internal links,
missing image dimensions, canonical errors, H1 issues, orphan pages, or schema
parse errors. Both representative publishing guides pass desktop and 390px
mobile Lens checks with zero accessibility violations, failed internal links,
page overflow, console errors, or failed requests. The internal
technical-readiness score is 94/100 and AI-search-readiness score is 86/100;
remaining deductions reflect unavailable destinations and outcome data.

## Available measurements

- Full 98-page before/after crawl and live HTTP verification.
- Redirect, robots, sitemap, ten-crawler, and external-destination probes.
- Desktop and 390px-mobile Lens evidence for both Publishing House guides.
- Dated anonymous search observations and an explicitly unmeasured AI-answer
  benchmark.

## Unavailable measurements

Google Search Console, Bing Webmaster Tools, analytics, origin/CDN logs, field
Core Web Vitals, backlinks, and controlled AI-answer citations remain
`NOT AVAILABLE — DATA ACCESS REQUIRED`. No ranking, traffic, or citation gain
is claimed.

## Next actions

1. Decide whether `kujolang/cinch` and `kujolang/source` should become public or
   point to different authoritative destinations.
2. Submit and inspect the 98-URL sitemap in Google Search Console and Bing
   Webmaster Tools.
3. Repeat the dated search and AI-answer observations after 7, 28, 60, and 90
   days when measurement access is available.
