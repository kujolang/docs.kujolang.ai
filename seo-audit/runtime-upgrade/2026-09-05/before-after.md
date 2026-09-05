# Before and after

| Generated metric | Baseline | Published artifact |
| --- | --- | --- |
| canonical_pages | 99 | 100 |
| sitemap_urls | 99 | 100 |
| broken_internal_links | 0 | 0 |
| duplicate_titles | 0 | 0 |
| duplicate_descriptions | 0 | 0 |
| h1_issues | 0 | 0 |
| canonical_mismatches | 0 | 0 |
| schema_parse_errors | 0 | 0 |
| orphan_pages | 0 | 0 |

Docs /upgrade/ changed from 404 to 200. Main /ecosystem/kujo/ gained a source-backed availability explanation; its shared installer and visible footer now link to the guide. Source changes add answers and discovery without changing crawler permissions, social images, or existing schema types.

Baseline came from the exact prior successful production artifacts, preserved before source edits. Default-runtime local attempts were stopped and are not counted as passed builds. The main-site validator has a helper that expects output/ even when a custom path is passed; validation passed after restoring the immutable artifact to the standard documented output path. Final validation also used that path. Docs full build passed; a core-page rebuild corrected shell-comment headings before publication, followed by full HTML validation/crawl.

The `production_200_pages: 0` field in local crawler summaries means production probing was disabled there, not that production failed. Separate live receipts establish HTTP results for changed routes. Robots and HTTP redirect checks preserved current policy; crawler labels are synthetic User-Agent checks, not real bot verification. Analytics and AI citation data remain unavailable.
