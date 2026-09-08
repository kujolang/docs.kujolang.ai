# Methodology

Audit date: 2026-09-08. Full canonical inventory at https://docs.kujolang.ai; editorial scope: Kujo Skills v0.7.0, VideoOps, HyperFrames styles and invocation. English developer audience. Useful conversions: find a skill, reach versioned source, install it, and follow an example.

The baseline is the successful untouched HEAD CI artifact named in baseline-provenance.json, produced with the repository-pinned runtime (and pinned SSG for docs). Archive and per-file hashes seal raw/baseline-build before edits. A separate full live crawl follows sitemap and HTML links. Local default-runtime attempts were stopped after sustained no-progress output; they are not claimed as successful builds. Subsequent compatible-runtime local checks and final pinned CI checks are recorded separately.

Delivery chain: source Markdown/templates → Kujo static build → generated artifact → GitHub Pages → Cloudflare/public HTTPS. Main website deploys through pages.yml; docs publishes verified generated output on gh-pages. No DNS/WAF or training-crawler policy edits. Generated files stay ignored.

Frozen seo_audit.py creates baseline/after inventories and metadata, content, graph, image, schema and indexability tables. Content/topic labels are automated classification aids, supplemented by source review of changed pages and shared templates. They are not claims of human editorial review of every line. Prior full audit evidence remains intact. Raw baseline datasets are preserved separately before regenerating after tables. Local-status fields mean filesystem route resolution, not a local HTTP fetch. The generic production_200_pages=0 field means its optional live probe was not used; authoritative live counts are in separate full-crawl receipts and production summaries.

probe_site.py covers redirects, crawler agents and all unique external destinations; blocked/timeout responses remain indeterminate, not broken. User-agent spoofing does not prove real search-bot access. Expected missing routes and retired flat aliases should return 404; the edge email-protection helper is not canonical content. Cross-site links to new pages are verified after both deployments.

Repeat the same generated crawl and production inventory. Reopen frozen files and verify their hashes. JSON-LD parsing/visible facts do not establish rich-result eligibility. Lighthouse samples are mobile lab observations under host load, not field Core Web Vitals or ranking evidence. Report raw metrics without a fabricated composite SEO or AI-readiness score.

Final external-link probes use probe_site_parallel.py with four workers and the same request semantics, user agent, timeouts, and full destination set. The original baseline probe helper remains unchanged.
