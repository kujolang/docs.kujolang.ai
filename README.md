# Kujo Docs

The official documentation site for the Kujo language and ecosystem, published at [docs.kujolang.ai](https://docs.kujolang.ai).

Version **1.3.3** was released on **September 4, 2026** with a complete SEO and AI-search audit, unique section metadata, repaired internal navigation, and explicit image dimensions. It retains the Kujo for Paperclip and source-standardized PackWrite 1.1.0 guides. The site follows the Kujo documentation information architecture: a short first-run path, task-oriented learning, intent-based tool guidance, reviewable-work workflows, showcases, collections, and reference material.

## Build

Requirements:

- Python 3
- The `kujo` CLI on `PATH`
- The sibling Kujo SSG repository at `../ssg`, or `SSG_ROOT` set to another checkout

Build the production site:

```bash
python3 scripts/build_site.py --site-url https://docs.kujolang.ai
```

For a non-sibling checkout:

```bash
SSG_ROOT=/path/to/ssg python3 scripts/build_site.py --site-url https://docs.kujolang.ai
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
bash scripts/verify-agent-platform-docs.sh output
```

Before release, also verify the generated sitemap routes, the themed 404 response, desktop and mobile layouts, same-origin links, keyboard interactions, and automated accessibility checks.

## Project structure

| Path | Purpose |
| --- | --- |
| `content/` | Markdown pages and repository guides |
| `templates/` | SSG layouts, listings, and error pages |
| `assets/` | Kujo Docs styles, scripts, Site Kit distribution, fonts, and images |
| `howl-social.json` | Source contract for the shared Kujo Docs social card |
| `scripts/render-social-card.sh` | Validates, renders, and rasterizes the Howl social card |
| `scripts/build_site.py` | Composes the IA sections into one generated site |
| `kujo-ssg.yml` | Production SSG defaults for `docs.kujolang.ai` |
| `output/` | Ignored generated site ready for static hosting |

The Site Kit consumer bundle and Departure Mono font are vendored under `assets/sitekit/` so production builds do not depend on remote assets.

Every generated page uses the shared 1200-by-630 Howl card at
`assets/img/social/kujo-docs.jpg` for Open Graph and X previews. Regenerate it
with a local Howl checkout and a trusted Sharp installation:

```bash
bash scripts/render-social-card.sh
```

Set `HOWL_BIN` when Howl is not in its default sibling-repository location.
The raster step uses macOS `sips` when available or a trusted Sharp entrypoint
provided through `SHARP_ENTRY`; it fails closed when neither is available.

The official K logomark is also published as SVG, ICO, standard PNG favicons, an Apple touch icon, Android web-app icons, and a Windows tile. The generated files are committed under `assets/favicons/` and copied to the site root during every build. To regenerate them from `assets/img/kujo-logomark-black.svg`, install CairoSVG and Pillow, then run:

```bash
python3 scripts/generate_favicons.py
```

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
