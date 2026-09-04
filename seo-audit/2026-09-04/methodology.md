# Methodology

Audit date: 2026-09-04

## Scope

Full repository and production audit of `https://docs.kujolang.ai`: every canonical page in the generated multi-section documentation build, rendered metadata and JSON-LD, navigation/link graphs, media, robots and sitemap behavior, production redirects, ten crawler identities, representative searches, and representative mobile-simulated Lighthouse runs.

## Evidence sequence

The documented `scripts/build_site.py` multi-section build produced the untouched baseline. That artifact was copied to `raw/baseline-output/` and fingerprinted. The site crawler then inspected every canonical page and its production equivalent. Production redirects and crawler profiles were checked independently. Search observations and Lighthouse runs were dated and kept separate from crawl evidence. The initially discovered incomplete local output is retained as `raw/baseline-output-incomplete/` and was excluded from conclusions.

## Build and crawl commands

The pinned Kujo binary and sibling SSG ran `python3 scripts/build_site.py --site-url https://docs.kujolang.ai`. Validation used `scripts/verify-agent-platform-docs.sh`, the SSG `scripts/validate-generated-output.sh`, the website repository's `scripts/seo_audit.py`, and targeted production probes. Raw and normalized evidence is stored beneath this audit directory.

## Interpretation limits

Production availability does not prove indexing. Anonymous searches are snapshots, not rank tracking. Lighthouse is lab evidence, not field Core Web Vitals. The generic production probe's `/ecosystem/kujo/`, `www.docs` and feed checks do not match this site's canonical route/host/artifact contract and are documented as non-applicable rather than defects. No traffic, ranking, backlink, or AI-citation outcome is inferred.
