#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/build_site.py --site-url https://docs.kujolang.ai
bash ../ssg/scripts/validate-generated-output.sh output
bash scripts/verify-agent-platform-docs.sh output
