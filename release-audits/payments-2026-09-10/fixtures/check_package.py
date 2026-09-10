"""Validate review package structure and reproducible evidence references."""
import hashlib
import json
from pathlib import Path
import re
import sys

package = Path(__file__).resolve().parent.parent
workspace = Path(sys.argv[1]).resolve()
errors = []
json_count = 0
for file in package.rglob('*.json'):
    if file.name == 'package-check.json': continue
    json.loads(file.read_text())
    json_count += 1
links = 0
citations = 0
for file in package.glob('*.md'):
    text = file.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', '#')): continue
        if not (file.parent / target.split('#')[0]).exists():
            errors.append(f'{file.name}: missing link {target}')
        links += 1
    for relative, number in re.findall(r'([a-z][a-z-]*/(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+):(\d+)', text):
        path = (Path(sys.argv[2]) / relative) if relative.startswith("packages/") and len(sys.argv) > 2 else workspace / relative
        if not path.is_file() or not 1 <= int(number) <= len(path.read_text().splitlines()):
            errors.append(f'{file.name}: invalid citation {relative}:{number}')
        citations += 1
source_hashes = json.loads((package / 'evidence/source-hashes.json').read_text())
for item in source_hashes:
    path = workspace / item['path']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        errors.append('Source changed since review: ' + item['path'])
assert len(list(package.glob('0[1-9]-*.md'))) == 9
budget = json.loads((package / 'evidence/interface-budget.json').read_text())
assert budget['compact_tool_utf8_bytes'] <= 2048
assert budget['summary_utf8_bytes'] <= 512
result = {'ok': not errors, 'json_files': json_count, 'local_links_checked': links, 'source_citations_checked': citations, 'source_hashes_checked': len(source_hashes), 'errors': errors}
print(json.dumps(result, indent=2))
sys.exit(0 if not errors else 1)
