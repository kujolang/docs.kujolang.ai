# Recommendations and measurement plan

Audit date: 2026-09-04

## Immediate after deployment

- Submit the 99-route sitemap in Google Search Console and Bing Webmaster Tools and request inspection for `/tools/packwrite/`.
- Re-run production crawler and representative template checks after the audit commit deploys.

## 7-day checks

- Record discovered/indexed counts, canonical selections, query impressions, and exclusions.
- Review CDN logs for crawler access, 404s, and 5xx responses if access becomes available.
- Establish field performance through CrUX or privacy-conscious first-party RUM.

## 28-, 60-, and 90-day comparisons

Repeat identical queries, controlled AI-answer questions, coverage, clicks/impressions, referring domains, and template field CWV with consistent country/device settings. Do not infer causation from correlation.

## Editorial decisions

Keep tool guides task-focused and evidence-led. Strengthen PackWrite discovery only with accurate examples, release evidence, and contextual cross-links; do not keyword-stuff or manufacture adoption claims. Treat `llms.txt` as experimental discoverability support rather than a crawler requirement.
