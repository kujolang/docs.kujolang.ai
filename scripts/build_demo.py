#!/usr/bin/env python3
"""Build the Kujo docs demo as one navigable site from SSG section builds."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SSG_ROOT = ROOT.parent / "ssg"
SECTIONS = ("learn", "build", "tools", "showcases", "collections", "ecosystem")


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
        "kujo",
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


def write_font_css(output: Path) -> None:
    """Point the generated font stylesheet at the vendored Site Kit font."""
    (output / "assets" / "css" / "fonts.css").write_text(DEPARTURE_MONO_CSS, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-url", default="http://127.0.0.1:4178")
    args = parser.parse_args()

    output = ROOT / "output"
    if output.exists():
        shutil.rmtree(output)

    with tempfile.TemporaryDirectory(prefix="kujo-docs-build-") as temporary:
        temp_root = Path(temporary)
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
            for source in section_output.rglob("*"):
                relative = source.relative_to(section_output)
                destination = output / relative
                if source.is_dir():
                    destination.mkdir(parents=True, exist_ok=True)
                else:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)

    search_script = SSG_ROOT / "scripts" / "docs_search_index.py"
    subprocess.run(["python3", str(search_script), "--content", str(ROOT / "content"), "--output", str(ROOT / "assets/js/docs-search-index.json"), "--site-url", args.site_url], cwd=ROOT, check=True)
    shutil.copy2(ROOT / "assets/js/docs-search-index.json", output / "assets/js/docs-search-index.json")
    write_font_css(output)
    write_aux(output, args.site_url)
    print(json.dumps({"output": str(output), "routes": len(routes()), "sections": list(SECTIONS)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
