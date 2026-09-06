# Kujo v1.3.1 documentation verification

Prepared the installation page, Kujo tool reference, and native upgrade guide for
runtime v1.3.1. The guide preserves v1.3.0 as the first release supporting native
upgrades and explains bounded Linux `Text file busy` retries from v1.3.1 onward.
The product site's evergreen copy and the docs site's own version are unchanged.

Before source edits, the current live installation/upgrade pages, changed source
files and a full untouched generated build were retained under
`/tmp/kujo-v131-docs-before`. Prior dated repository audit baselines are unchanged.
`baseline-summary.json`, `after-summary.json` and `build-provenance.json` preserve
the scoped comparison and changed-page hashes.

Both generated inventories contain 100 canonical pages, with no metadata, H1,
canonical, internal-link, orphan or schema errors. The full SSG build,
`validate-generated-output.sh output` and `verify-agent-platform-docs.sh output`
passed. Builds used a checksum-verified temporary v1.2.2 runtime under the
existing SSG compatibility pin; the user's installed runtime was not modified.

Published source 657b0b4 and deployment 8492353 after runtime release
34043429054, npm clean-install matrix 34046196833 and five-platform cross-version
upgrade matrix 34046200374 passed. Pages run 34046539901 passed. All 100 live
canonical pages return 200 with one H1, matching canonical and valid JSON-LD;
installation, upgrade and tool content plus sitemap, llms.txt, search and WebMCP
discovery documents expose the current release. No search traffic,
ranking or AI-citation outcome is inferred from these technical checks.
