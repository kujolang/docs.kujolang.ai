# Methodology

Immutable successful pinned-CI build artifacts were downloaded before edits; archive and file hashes were sealed. Source-only audit commits after those builds do not change website output. The same filesystem crawl checks every canonical route in baseline and after output for metadata, headings, canonical URLs, sitemap coverage, internal links, image attributes and JSON-LD. Independent production crawls follow sitemap and HTML links. Redirect and crawler probes test HTTP delivery, not authenticated bot identity. Native repository validators and browser inspection supplement HTML inspection. Existing hosting, runtime build pins, robots and crawler training policies remain unchanged. Source/runtime/deployment identifiers are in provenance files.

Research sources distinguish official recommendations from editorial judgment. Rankings, AI citations and field CWV are unavailable rather than estimated. Lighthouse is a variable-load mobile lab observation.

Indeterminate production TLS/read timeouts were retried after the build-artifact download, at lower concurrency where needed. Original attempts are retained in raw/live; no certificate checks, crawler policies or assertions were weakened.
