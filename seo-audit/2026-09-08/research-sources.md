# Current primary guidance

Retrieved 2026-09-08 through live web reads/search and versioned repository source.

| Source | Conclusion | Classification |
| --- | --- | --- |
| [https://developers.google.com/search/docs/appearance/ai-features](https://developers.google.com/search/docs/appearance/ai-features) | Google AI Search eligibility follows indexability, snippet eligibility, and normal SEO; no special schema guarantees inclusion. | official requirement/recommendation |
| [https://developers.google.com/search/docs/fundamentals/ai-optimization-guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | Useful original information and normal SEO matter; no special llms.txt file is required. | official recommendation |
| [https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | Use canonical URLs and accurate last modification dates in sitemaps. | official recommendation |
| [https://www.bing.com/indexnow/getstarted](https://www.bing.com/indexnow/getstarted) | IndexNow notifies participating engines of changes; it does not guarantee indexing. No submission made. | official recommendation |
| [https://developers.openai.com/api/docs/bots](https://developers.openai.com/api/docs/bots) | Search indexing, user fetches, and model training use separate crawlers. Preserve the owner training policy. | official crawler documentation |
| [https://schema.org/SoftwareSourceCode](https://schema.org/SoftwareSourceCode) | SoftwareSourceCode describes software source; factual schema alignment is separate from rich-result eligibility. | documented vocabulary |
| [https://github.com/heygen-com/hyperframes#skills](https://github.com/heygen-com/hyperframes#skills) | Native skills update command installs the HyperFrames authoring context. | primary product source |
| [https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0](https://github.com/kujolang/kujo-skills/releases/tag/v0.7.0) | Released scope is 135 skills, including both migrated video skills and the shared VideoOps runtime references. | primary release evidence |

Query and content maps are editorial hypotheses. llms.txt is retained as an existing experimental convenience; it is not treated as an indexing requirement. No training policy or DNS/WAF setting was changed.
