# Kujo Docs demo

This is a launch-draft documentation site built from the Kujo SSG docs starter and the SiteKit distribution. It follows `../ssg/starters/docs-site/INFORMATION_ARCHITECTURE.md`: a short first-time path, task-oriented learning, intent-based tools, reviewable-work workflows, showcases, collections, and secondary reference surfaces.

## Build and preview

From this directory:

```bash
python3 scripts/build_demo.py --site-url http://127.0.0.1:4178
kujo serve output --port 4178
```

The build script uses the SSG once for the first-time path and once per IA collection, then composes the generated routes so the demo stays practical to rebuild while preserving the SSG templates, metadata, and generated artifacts.

The generated site is in `output/`. `output/` is disposable build output; edit Markdown, templates, or assets instead.

`assets/sitekit/` vendors the source-built SiteKit consumer bundle. Page-level overrides consume SiteKit tokens and keep the SSG docs layout readable without introducing a second visual language.

This is a local-first technical preview. Tool pages describe the smallest useful local workflow and state their boundaries; they do not imply hosted services or final public release artifacts.
