# Research sources

Audit date: 2026-09-04

| Source | Retrieved | Supported conclusion | Classification |
| --- | --- | --- | --- |
| [Google: How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works) | 2026-09-04 | Discovery, crawling, indexing, and serving are separate; a successful crawl does not prove indexation. | Documented behavior |
| [Google: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | 2026-09-04 | Redirects, canonical markup, and sitemap inclusion should point at the same preferred URL. | Documented recommendation |
| [Google: sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | 2026-09-04 | Sitemaps should contain absolute canonical URLs, and `lastmod` should represent significant changes. | Documented recommendation |
| [Google: structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 2026-09-04 | Structured data must describe visible content; valid markup does not guarantee a rich result. | Documented requirement and limitation |
| [Google: AI features](https://developers.google.com/search/docs/appearance/ai-features) | 2026-09-04 | Existing Search guidance applies to Google's AI features; no special AI markup is required. | Documented behavior |
| [Bing: robots controls](https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240) | 2026-09-04 | Crawl and index controls must remain readable by Bingbot to take effect. | Documented behavior |
| [Bing: IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby) | 2026-09-04 | IndexNow can notify participating engines about changed URLs but does not guarantee indexation. | Documented behavior |
| [OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-09-04 | OAI-SearchBot discovery is distinct from GPTBot training access. | Documented behavior |
| [Anthropic crawler controls](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | 2026-09-04 | Claude search, user-triggered, and training crawlers are separate policy surfaces. | Documented behavior |
| [Schema.org documentation](https://schema.org/docs/documents.html) | 2026-09-04 | Schema.org defines vocabulary; search-feature eligibility remains provider-specific. | Documented vocabulary and limitation |
