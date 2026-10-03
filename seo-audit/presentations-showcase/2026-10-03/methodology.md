# Methodology

Audit date: 2026-10-03

## Scope

Full local crawl and production baseline for docs.kujolang.ai, with focused editorial and linking review for the new Presentations showcase route. Repository source, generated output, production responses, first-party product documentation, and current primary search/crawler guidance were kept as separate evidence layers.

## Evidence sequence

1. Checked out clean `origin/main` at `83812218029de98af35d4244159b8e9db0f8c70b`.
2. Built and validated the untouched 103-route site with Kujo 1.7.0.
3. Crawled every canonical page and probed each production equivalent.
4. Preserved the baseline output under the ignored `raw/baseline-build/` workspace before editing.
5. Added the source-backed page and contextual links.
6. Rebuilt, reran repository contracts, and crawled the same inventory fields.
7. Probed the live new route, live examples, release URL, robots policy, and OAI-SearchBot access separately.

## Current primary guidance consulted

See `research-sources.md`. The implementation follows documented requirements and recommendations for crawlable links, descriptive metadata, canonicals, sitemaps, and crawler policy. No experimental protocol was treated as a ranking requirement.

## Build and crawl commands

`KUJO_BIN=../kujo/target/release/kujo python3 scripts/build_site.py --site-url https://docs.kujolang.ai`

`bash ../ssg/scripts/validate-generated-output.sh output`

`bash scripts/verify-agent-platform-docs.sh output`

`python3 ../kujolang.ai-work/scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/presentations-showcase/2026-10-03 --phase baseline|after --origin https://docs.kujolang.ai`

## Interpretation limits

The after crawl is local generated-output evidence, not deployment evidence. Production, ranking, referral, field-performance, and AI-citation outcomes require deployment, elapsed time, and authenticated platform data. Schema.org validity does not imply a Google rich result.
