#!/usr/bin/env bash
set -euo pipefail

output_dir="${1:-output}"

require_file() {
  if [[ ! -f "$output_dir/$1" ]]; then
    printf 'missing generated file: %s\n' "$1" >&2
    exit 1
  fi
}

require_text() {
  local file="$1"
  local text="$2"
  if ! grep -Fq -- "$text" "$output_dir/$file"; then
    printf 'missing expected text in %s: %s\n' "$file" "$text" >&2
    exit 1
  fi
}

for route in \
  build/owned-agent-projects/index.html \
  build/agent-profiles/index.html \
  build/agent-credentials/index.html \
  build/agent-operations/index.html; do
  require_file "$route"
done

require_text "install/index.html" "https://kujolang.ai/install.sh"
require_text "install/index.html" "--group agent"
require_text "build/owned-agent-projects/index.html" "kujo agent new my-agent --profile basic --install"
require_text "build/owned-agent-projects/index.html" "kujo doctor agent --deep"

for profile in basic tools knowledge workflow hardened observable full; do
  require_text "build/agent-profiles/index.html" "<code>${profile}</code>"
done

require_text "build/agent-credentials/index.html" "kujo agent auth set openai"
require_text "build/agent-credentials/index.html" "--from-stdin"
require_text "build/agent-credentials/index.html" "--from-env"
require_text "build/agent-credentials/index.html" "--project"
require_text "build/agent-credentials/index.html" "--name LINEAR_API_TOKEN"

require_text "build/agent-operations/index.html" "kujo agent inspect"
require_text "build/agent-operations/index.html" "kujo agent run"
require_text "build/agent-operations/index.html" "kujo agent eval"
require_text "build/agent-operations/index.html" "--workcell"

require_text "sitemap.xml" "/build/owned-agent-projects/"
require_text "sitemap.xml" "/build/agent-profiles/"
require_text "sitemap.xml" "/build/agent-credentials/"
require_text "sitemap.xml" "/build/agent-operations/"
require_text "llms.txt" "Repository-owned Agent Projects"
require_text ".well-known/kujo-site-index.json" "owned-agent-projects"
require_text ".well-known/kujo-site-index.json" "agent-credentials"
require_text "build/owned-agent-projects/index.html" "data-kujo-webmcp"

printf 'Agent platform documentation contract passed.\n'
