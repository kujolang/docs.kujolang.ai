# Kujo Docs

The official documentation site for the Kujo language and ecosystem, published at [docs.kujolang.ai](https://docs.kujolang.ai).

Version **1.0.0** launched on **August 8, 2026**. The site follows the Kujo documentation information architecture: a short first-run path, task-oriented learning, intent-based tool guidance, reviewable-work workflows, showcases, collections, and reference material.

## Build

Requirements:

- Python 3
- The `kujo` CLI on `PATH`
- The sibling Kujo SSG repository at `../ssg`

Build the production site:

```bash
python3 scripts/build_site.py --site-url https://docs.kujolang.ai
```

The generated static site is written to `output/`. It is disposable build output; edit files under `content/`, `templates/`, or `assets/` instead.

## Local preview

```bash
python3 scripts/build_site.py --site-url http://127.0.0.1:4178
kujo serve output --port 4178
```

Then open [http://127.0.0.1:4178](http://127.0.0.1:4178).

## Validate

```bash
bash ../ssg/scripts/validate-generated-output.sh output
```

Before release, also verify the generated sitemap routes, the themed 404 response, desktop and mobile layouts, same-origin links, keyboard interactions, and automated accessibility checks.

## Project structure

| Path | Purpose |
| --- | --- |
| `content/` | Markdown pages and repository guides |
| `templates/` | SSG layouts, listings, and error pages |
| `assets/` | Kujo Docs styles, scripts, Site Kit distribution, fonts, and images |
| `scripts/build_site.py` | Composes the IA sections into one generated site |
| `kujo-ssg.yml` | Production SSG defaults for `docs.kujolang.ai` |
| `output/` | Ignored generated site ready for static hosting |

The Site Kit consumer bundle and Departure Mono font are vendored under `assets/sitekit/` so production builds do not depend on remote assets.

## Release policy

The docs site has its own semantic version. Repository pages preserve the verified status and boundaries of the Kujo component they describe; releasing the documentation does not silently promote preview tools or hosted services to production-ready status.

Release changes are recorded in [CHANGELOG.md](CHANGELOG.md). The current version is stored in [VERSION](VERSION).

## Deploy

Production uses GitHub Pages behind Cloudflare:

| Layer | Configuration |
| --- | --- |
| GitHub Pages | Repository `kujolang/docs.kujolang.ai`, branch `gh-pages`, path `/` |
| Custom domain | `docs.kujolang.ai`, also emitted as `output/CNAME` |
| Cloudflare DNS | Proxied CNAME `docs` to `kujolang.github.io` |
| HTTPS | Cloudflare Universal SSL with **Always Use HTTPS** enabled |

Build from `main`, replace the contents of the `gh-pages` branch with the generated `output/` directory, and push that branch. The generated `.nojekyll` file disables Jekyll processing, while `404.html` provides the themed catchall response.

After deployment, verify the public edge rather than relying on a local DNS cache:

```bash
dig +short @1.1.1.1 docs.kujolang.ai A
curl -I http://docs.kujolang.ai/
curl -I https://docs.kujolang.ai/
```

The HTTP request should redirect to HTTPS, and the HTTPS request should return `200` from Cloudflare with GitHub Pages as the origin.
