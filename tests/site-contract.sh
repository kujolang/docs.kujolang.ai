#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SSG_ROOT="${SSG_ROOT:-$ROOT/../ssg}"
cd "$ROOT"

python3 scripts/build_site.py --site-url https://docs.kujolang.ai
bash "$SSG_ROOT/scripts/validate-generated-output.sh" output
bash scripts/verify-agent-platform-docs.sh output
