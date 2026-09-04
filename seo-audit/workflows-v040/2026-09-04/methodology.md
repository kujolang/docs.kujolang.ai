# Methodology

Audit date: 2026-09-04

## Scope

Full repository and production audit of `https://docs.kujolang.ai`, with focused
content and browser review of the workflow collection, Editorial publishing,
and Publishing House Operator guides. The baseline covers all 98 canonical
pages and the complete deployed artifact.

## Evidence sequence

1. Preserve and fingerprint the deployed `gh-pages` artifact before editing.
2. Crawl all canonical pages against production and inspect metadata, schema, links, images, sitemap membership, and architecture.
3. Probe the canonical host, robots policy, ten crawler identities, and external destinations using the operator guide as the key route.
4. Run Lens on both publishing guides at desktop and 390px mobile sizes.
5. Apply source-level fixes for verified internal links, duplicate section metadata, duplicate titles, and intrinsic image dimensions.
6. Build, validate, deploy through the existing `gh-pages` contract, and repeat the same crawl and browser checks.

## Current primary guidance consulted

Only the dated first-party sources in `research-sources.md` support crawler,
canonical, sitemap, structured-data, and AI-search conclusions. `llms.txt`
remains an experimental discovery aid, not a ranking requirement.

## Build and crawl commands

```bash
PATH=/absolute/path/to/kujo:$PATH python3 scripts/build_site.py --site-url https://docs.kujolang.ai
bash ../ssg/scripts/validate-generated-output.sh output
bash scripts/verify-agent-platform-docs.sh output
python3 ../kujolang.ai-work/scripts/seo_audit.py --repo . --output output --audit-dir seo-audit/workflows-v040/2026-09-04 --phase after --origin https://docs.kujolang.ai --probe-production
python3 ../kujolang.ai-work/scripts/probe_site.py --audit-dir seo-audit/workflows-v040/2026-09-04 --origin https://docs.kujolang.ai --phase after --key-path /build/publishing-house-operator/ --skip-www --feed-path ''
```

## Interpretation limits

Technical readiness does not prove ranking, indexation, traffic, conversion, or
AI citation. Anonymous search results are dated observations. Lens timing is
lab evidence and not field Core Web Vitals. `www.docs.kujolang.ai` and a feed
are not part of this publication contract, so their absence is not treated as
a defect. Confirmed private or unavailable repository links remain unresolved
without an authoritative public replacement.
