#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
howl_bin="${HOWL_BIN:-${repo_root}/../howl/bin/howl}"
sharp_entry="${SHARP_ENTRY:-${repo_root}/../kujolang.ai-work/node_modules/sharp/lib/index.js}"
render_dir="$(mktemp -d /tmp/kujo-docs-howl.XXXXXX)"
export KUJO="${KUJO:-${repo_root}/../kujo/target/release/kujo}"

cleanup() {
	rm -rf -- "$render_dir"
}
trap cleanup EXIT

if [[ ! -x "$howl_bin" ]]; then
	printf 'Howl executable not found: %s\n' "$howl_bin" >&2
	exit 1
fi

"$howl_bin" validate --manifest "$repo_root/howl-social.json"
"$howl_bin" render --manifest "$repo_root/howl-social.json" --out "$render_dir" --format svg
mkdir -p "$repo_root/assets/img/social"

if command -v sips >/dev/null 2>&1; then
	sips -s format jpeg \
		"$render_dir/kujo-docs.svg" \
		--out "$repo_root/assets/img/social/kujo-docs.jpg" >/dev/null
elif [[ -f "$sharp_entry" ]]; then
	node "$repo_root/scripts/rasterize-social-card.mjs" \
		"$render_dir/kujo-docs.svg" \
		"$repo_root/assets/img/social/kujo-docs.jpg" \
		"$sharp_entry"
else
	printf 'No supported SVG rasterizer found. Install sips or set SHARP_ENTRY.\n' >&2
	exit 1
fi

printf 'Rendered Kujo Docs social card.\n'
