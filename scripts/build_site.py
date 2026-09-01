#!/usr/bin/env python3
"""Build the official Kujo documentation site from SSG section builds."""

from __future__ import annotations

import argparse
from html import unescape
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SSG_ROOT = Path(os.environ.get("SSG_ROOT", ROOT.parent / "ssg")).resolve()
SECTIONS = ("learn", "build", "review", "tools", "showcases", "collections", "ecosystem")
KUJO_BIN = os.environ.get("KUJO_BIN", "kujo")


DEPARTURE_MONO_CSS = """/* Kujo Docs typography: local Site Kit asset. */
@font-face {
  font-family: \"Departure Mono\";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(\"../sitekit/DepartureMono-Regular.woff2\") format(\"woff2\"),
       url(\"../sitekit/DepartureMono-Regular.woff\") format(\"woff\");
}

body,
h1, h2, h3, h4, h5, h6,
button, input, textarea, select,
code, pre, .title-font {
  font-family: \"Departure Mono\", \"SFMono-Regular\", \"Cascadia Code\", \"Roboto Mono\", \"Liberation Mono\", Menlo, Consolas, monospace;
}
"""


def run_build(content: Path, output: Path, site_url: str, *, no_index: bool, no_aux: bool) -> None:
    command = [
        KUJO_BIN,
        "run",
        str(SSG_ROOT / "build.kujo"),
        "--",
        "--content",
        str(content),
        "--output",
        str(output),
        "--site-url",
        site_url,
        "--no-aliases",
        "--webmcp",
    ]
    if no_index:
        command.append("--no-index")
    if no_aux:
        command.append("--no-aux")
    subprocess.run(command, cwd=ROOT, check=True)


def frontmatter(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    meta: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta


def routes() -> list[tuple[str, str, str]]:
    found: list[tuple[str, str, str]] = [("/", "Kujo Docs", "The shortest path from language basics to reviewable, local-first software.")]
    for path in sorted((ROOT / "content").rglob("*.md")):
        relative = path.relative_to(ROOT / "content")
        meta = frontmatter(path)
        if meta.get("draft") in {"true", "yes"} or meta.get("search_exclude") in {"true", "yes"}:
            continue
        slug = str(meta.get("custom_url") or path.stem).strip("/")
        if relative.parts[0] not in {"pages", "posts"}:
            slug = f"{relative.parts[0]}/{slug}"
        if relative.parts[0] == "posts":
            slug = f"updates/{slug}"
        found.append((f"/{slug}/", str(meta.get("title") or path.stem), str(meta.get("description") or "")))
    for section in SECTIONS:
        found.append((f"/{section}/", section.title(), f"Kujo {section} documentation."))
    return sorted(set(found), key=lambda item: item[0])


def write_aux(output: Path, site_url: str) -> None:
    items = routes()
    sitemap = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for route, _, _ in items:
        sitemap.append(f"  <url><loc>{site_url.rstrip('/')}{quote(route)}</loc></url>")
    sitemap.append("</urlset>")
    (output / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")

    llms = ["# Kujo Docs", "", "A local-first path through the Kujo language and ecosystem.", ""]
    for route, title, description in items:
        llms.append(f"- [{title}]({site_url.rstrip('/')}{route}) — {description}")
    (output / "llms.txt").write_text("\n".join(llms) + "\n", encoding="utf-8")
    (output / "CNAME").write_text("docs.kujolang.ai\n", encoding="utf-8")
    (output / ".nojekyll").write_text("", encoding="utf-8")


def write_font_css(output: Path) -> None:
    """Point the generated font stylesheet at the vendored Site Kit font."""
    (output / "assets" / "css" / "fonts.css").write_text(DEPARTURE_MONO_CSS, encoding="utf-8")


def publish_favicons(output: Path) -> None:
    """Publish the committed cross-platform favicon set at the site root."""
    source = ROOT / "assets" / "favicons"
    required = {
        "favicon.svg",
        "favicon.ico",
        "favicon-16x16.png",
        "favicon-32x32.png",
        "favicon-48x48.png",
        "apple-touch-icon.png",
        "android-chrome-192x192.png",
        "android-chrome-512x512.png",
        "mstile-150x150.png",
        "site.webmanifest",
        "browserconfig.xml",
    }
    missing = sorted(name for name in required if not (source / name).is_file())
    if missing:
        raise FileNotFoundError(f"missing favicon assets: {', '.join(missing)}")
    for name in sorted(required):
        shutil.copy2(source / name, output / name)


def merge_webmcp_indexes(output: Path, section_indexes: list[Path]) -> None:
    """Combine the core and section SSG indexes into one public docs catalog."""
    index_path = output / ".well-known" / "kujo-site-index.json"
    document = json.loads(index_path.read_text(encoding="utf-8"))
    items_by_id = {item["id"]: item for item in document.get("items", [])}
    types_by_name = {entry["name"]: entry for entry in document.get("content_types", [])}
    for section_index in section_indexes:
        section = json.loads(section_index.read_text(encoding="utf-8"))
        for item in section.get("items", []):
            items_by_id[item["id"]] = item
        for entry in section.get("content_types", []):
            types_by_name[entry["name"]] = entry
    document["items"] = sorted(items_by_id.values(), key=lambda item: item["url"])
    document["content_types"] = [types_by_name[name] for name in sorted(types_by_name)]
    for entry in document["content_types"]:
        entry["count"] = sum(1 for item in document["items"] if item["type"] == entry["name"])
    index_path.write_text(json.dumps(document, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def finalize_html(output: Path) -> None:
    """Apply docs-specific cleanup that is not part of the generic SSG templates."""
    empty_prerequisites = re.compile(
        r'\s*<section class="docs-prerequisites"[^>]*>'
        r'\s*<h2[^>]*>Prerequisites</h2>\s*</section>'
    )
    section_badge = re.compile(
        r'<span class="docs-badge docs-badge-section"><span>Section</span>.*?</span>'
    )
    listing_link = re.compile(
        r'(<li class="listing-card">.*?<h2 class="listing-card-title">'
        r'<a href="(?P<href>[^"]+)"[^>]*>(?P<title>[^<]+)</a></h2>.*?'
        r'<a href="(?P=href)" class="listing-card-button">)View Product(</a>.*?</li>)',
        re.DOTALL,
    )

    def add_heading_ids(document: str) -> str:
        """Give rendered headings stable fragment targets for docs links and TOCs."""
        used: set[str] = set()
        heading = re.compile(r"<h([1-6])(?P<attrs>[^>]*)>(?P<body>.*?)</h\1>", re.DOTALL)

        def replace(match: re.Match[str]) -> str:
            attrs = match.group("attrs")
            if re.search(r"\bid=", attrs):
                return match.group(0)
            plain = re.sub(r"<[^>]+>", " ", unescape(match.group("body")))
            slug = re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-") or "section"
            candidate = slug
            suffix = 2
            while candidate in used:
                candidate = f"{slug}-{suffix}"
                suffix += 1
            used.add(candidate)
            return f'<h{match.group(1)} id="{candidate}"{attrs}>{match.group("body")}</h{match.group(1)}>'

        return heading.sub(replace, document)

    for path in output.rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        html = empty_prerequisites.sub("", html)
        html = section_badge.sub("", html)
        html = listing_link.sub(
            lambda match: f'{match.group(1)}View {match.group("title")}{match.group(4)}',
            html,
        )
        html = add_heading_ids(html)
        if path == output / "404.html":
            for relative, absolute in (
                ('href="assets/', 'href="/assets/'),
                ('src="assets/', 'src="/assets/'),
                ('href="favicon.svg"', 'href="/favicon.svg"'),
                ('href="index.html"', 'href="/"'),
                ('href="sitemap.xml"', 'href="/sitemap.xml"'),
                ('href="llms.txt"', 'href="/llms.txt"'),
            ):
                html = html.replace(relative, absolute)
        html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
        path.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-url", default="https://docs.kujolang.ai")
    args = parser.parse_args()

    output = ROOT / "output"
    if output.exists():
        shutil.rmtree(output)

    with tempfile.TemporaryDirectory(prefix="kujo-docs-build-") as temporary:
        temp_root = Path(temporary)
        section_indexes: list[Path] = []
        core_content = temp_root / "core-content"
        for directory in ("pages", "posts"):
            destination = core_content / directory
            destination.mkdir(parents=True)
            for source in (ROOT / "content" / directory).glob("*.md"):
                shutil.copy2(source, destination / source.name)
        run_build(core_content, output, args.site_url, no_index=False, no_aux=False)

        for section in SECTIONS:
            section_content = temp_root / section
            (section_content / section).mkdir(parents=True)
            for source in (ROOT / "content" / section).glob("*.md"):
                shutil.copy2(source, section_content / section / source.name)
            section_output = temp_root / f"{section}-output"
            run_build(section_content, section_output, args.site_url, no_index=True, no_aux=True)
            section_index = section_output / ".well-known" / "kujo-site-index.json"
            if section_index.is_file():
                section_indexes.append(section_index)
            for source in section_output.rglob("*"):
                relative = source.relative_to(section_output)
                if relative == Path(".well-known/kujo-site-index.json"):
                    continue
                destination = output / relative
                if source.is_dir():
                    destination.mkdir(parents=True, exist_ok=True)
                else:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)

        merge_webmcp_indexes(output, section_indexes)

    for blog_artifact in (output / "blog", output / "updates", output / "feed"):
        if blog_artifact.exists():
            shutil.rmtree(blog_artifact)

    search_script = SSG_ROOT / "scripts" / "docs_search_index.py"
    subprocess.run(["python3", str(search_script), "--content", str(ROOT / "content"), "--output", str(ROOT / "assets/js/docs-search-index.json"), "--site-url", args.site_url], cwd=ROOT, check=True)
    shutil.copy2(ROOT / "assets/js/docs-search-index.json", output / "assets/js/docs-search-index.json")
    write_font_css(output)
    finalize_html(output)
    write_aux(output, args.site_url)
    publish_favicons(output)
    print(json.dumps({"output": str(output), "routes": len(routes()), "sections": list(SECTIONS)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
