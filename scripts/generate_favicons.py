#!/usr/bin/env python3
"""Generate the Kujo Docs browser, desktop, and mobile icon set."""

from __future__ import annotations

import copy
import io
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "img" / "kujo-logomark-black.svg"
DESTINATION = ROOT / "assets" / "favicons"
SVG_NAMESPACE = "http://www.w3.org/2000/svg"


def square_svg() -> bytes:
    """Center the official mark on a square, opaque canvas."""
    source_root = ET.parse(SOURCE).getroot()
    root = ET.Element(
        f"{{{SVG_NAMESPACE}}}svg",
        {
            "viewBox": "0 0 1536 1536",
            "role": "img",
            "aria-label": "Kujo logomark",
        },
    )
    ET.SubElement(
        root,
        f"{{{SVG_NAMESPACE}}}rect",
        {"width": "1536", "height": "1536", "fill": "#ffffff"},
    )
    group = ET.SubElement(
        root,
        f"{{{SVG_NAMESPACE}}}g",
        {"transform": "translate(4.5 0)"},
    )
    for child in source_root:
        group.append(copy.deepcopy(child))
    ET.register_namespace("", SVG_NAMESPACE)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def render(svg: bytes, size: int) -> Image.Image:
    png = cairosvg.svg2png(
        bytestring=svg,
        output_width=size,
        output_height=size,
    )
    return Image.open(io.BytesIO(png)).convert("RGBA")


def main() -> int:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    svg = square_svg()
    (DESTINATION / "favicon.svg").write_bytes(svg)

    images = {size: render(svg, size) for size in (16, 32, 48, 150, 180, 192, 512)}
    for size in (16, 32, 48):
        images[size].save(DESTINATION / f"favicon-{size}x{size}.png", optimize=True)
    images[150].save(DESTINATION / "mstile-150x150.png", optimize=True)
    images[180].save(DESTINATION / "apple-touch-icon.png", optimize=True)
    images[192].save(DESTINATION / "android-chrome-192x192.png", optimize=True)
    images[512].save(DESTINATION / "android-chrome-512x512.png", optimize=True)
    images[48].save(
        DESTINATION / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[images[32], images[16]],
    )

    manifest = {
        "name": "Kujo Docs",
        "short_name": "Kujo Docs",
        "description": "Official documentation for the Kujo language and ecosystem.",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#ffffff",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any",
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any",
            },
        ],
    }
    (DESTINATION / "site.webmanifest").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    (DESTINATION / "browserconfig.xml").write_text(
        """<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
  <msapplication>
    <tile>
      <square150x150logo src="/mstile-150x150.png"/>
      <TileColor>#ffffff</TileColor>
    </tile>
  </msapplication>
</browserconfig>
""",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
