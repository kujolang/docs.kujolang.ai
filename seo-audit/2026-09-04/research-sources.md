# Research sources

Audit date: 2026-09-04

| Source | Retrieved | Supported conclusion | Classification |
| --- | --- | --- | --- |
| [Google: How Search works](https://developers.google.com/search/docs/fundamentals/how-search-works) | 2026-09-04 | Discovery, crawling, indexing, and serving are separate; crawlability does not prove indexing. | Documented behavior |
| [Google: robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) | 2026-09-04 | Robots rules control crawling and are not a reliable noindex mechanism. | Documented behavior |
| [Google: sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) | 2026-09-04 | Sitemaps should contain preferred canonical URLs. | Documented recommendation |
| [Google: canonicals](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) | 2026-09-04 | Canonical signals should agree across HTML, sitemaps, and redirects. | Documented recommendation |
| [Google: structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | 2026-09-04 | Markup must describe visible content; validity does not guarantee a rich result. | Documented requirement/limitation |
| [Google: AI features](https://developers.google.com/search/docs/appearance/ai-features) | 2026-09-04 | Existing Search guidance applies to AI features; no special AI markup is required. | Documented behavior |
| [Bing: robots.txt tester](https://www.bing.com/webmasters/help/robots-txt-tester-623520f4) | 2026-09-04 | Bing interprets robots rules per user agent. | Documented behavior |
| [IndexNow](https://www.indexnow.org/documentation) | 2026-09-04 | IndexNow is optional change notification and does not guarantee indexing. | Documented behavior |
| [OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-09-04 | OAI-SearchBot search access is separate from GPTBot training access. | Documented behavior |
| [Anthropic crawler controls](https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | 2026-09-04 | ClaudeBot, Claude-User, and Claude-SearchBot have distinct roles. | Documented behavior |
| [Schema.org documentation](https://schema.org/docs/documents.html) | 2026-09-04 | Schema.org supplies vocabularies; search-feature eligibility is provider-specific. | Documented vocabulary/limit |
