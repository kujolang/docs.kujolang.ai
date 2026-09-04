# Methodology

Audit date: 2026-09-04

## Scope

Release-publication audit of all 98 generated canonical pages, with focused content review of `/tools/searchbridge/` and global verification of metadata, canonicals, sitemap membership, robots policy, structured data, internal links, media attributes, redirects, external destinations, and search/AI crawler access.

## Evidence sequence

1. Reconstructed the baseline from immutable commit `555f36b6f88088b6309fedd6a352564e59e309d4` with the same deterministic builder.
2. Compared it with the validated output from commit `8fddff93815544b9c325984bc914e5f755a39cd4`.
3. Ran the same 98-page crawl for both outputs and probed the public deployment after publication.

The original untracked release-audit scratch workspace was removed during concurrent documentation publication. The same-day full audit in `seo-audit/2026-09-04/` preserves the actual pre-deployment production receipts. Baseline production statuses in this release-specific reconstruction therefore establish current routing parity, not archived pre-release HTTP bodies.

## Current primary guidance consulted

See `research-sources.md`. Requirements, recommendations, best practices, and measurement limitations are kept separate; no ranking or citation outcome is inferred from technical validity.

## Interpretation limits

The crawl is deterministic technical evidence, not proof of indexing, ranking, traffic, or AI citation. External 401/403/405/429 responses are treated as indeterminate. The audit adds no product claim beyond the tagged SearchBridge release record and its sanitized qualification evidence.
