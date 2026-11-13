#!/usr/bin/env python3
"""Verify the complete vendored SiteKit release, including runnable assets."""
import hashlib
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
source = json.loads((root / 'assets/sitekit-source.json').read_text())
for directory in [root / 'assets/sitekit', root / 'output/assets/sitekit']:
    manifest = json.loads((directory / 'sitekit-manifest.json').read_text())
    assert manifest['version'] == source['version'] == '1.2.0'
    for name, expected in manifest['files'].items():
        assert hashlib.sha256((directory / name).read_bytes()).hexdigest() == expected, str(directory / name)
print('SiteKit 1.2.0 source/output distribution integrity passed')
