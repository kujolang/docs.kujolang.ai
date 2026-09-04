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

reject_text() {
  local file="$1"
  local text="$2"
  if grep -Fq -- "$text" "$output_dir/$file"; then
    printf 'unexpected text in %s: %s\n' "$file" "$text" >&2
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

for route in \
  start-here/index.html \
  build/owned-agent-projects/index.html \
  tools/kujo/index.html; do
  reject_text "$route" 'class="docs-eyebrow"'
  reject_text "$route" 'docs-badge-section'
done

require_text "install/index.html" "https://kujolang.ai/install.sh"
require_text "install/index.html" "--group agent"
require_text "build/owned-agent-projects/index.html" "kujo agent new my-agent --profile basic --install"
require_text "build/owned-agent-projects/index.html" "kujo doctor agent --deep"
require_text "build/owned-agent-projects/index.html" '<p>An Agent Project keeps the agent in your repository. Its instructions, model preference, skills, tools, knowledge, policies, workflows, evaluation, exact dependency pins, and runtime boundaries remain reviewable files instead of hidden hosted state.</p>'
require_text "build/owned-agent-projects/index.html" '<p>The working sources are the <a href="https://github.com/kujolang/kujo/tree/main/examples/owned-agent-project">self-hosted example</a>, the <a href="https://github.com/kujolang/kujo-workflows/tree/main/owned-agent-project">lifecycle workflow</a>, and the <a href="https://github.com/kujolang/kujo/blob/main/docs/BUILD_AN_AGENT.md">implementation guide</a>.</p>'

for profile in basic tools knowledge workflow hardened observable full; do
  require_text "build/agent-profiles/index.html" "<code>${profile}</code>"
done

require_text "build/agent-credentials/index.html" "kujo agent auth set openai"
require_text "build/agent-credentials/index.html" "--from-stdin"
require_text "build/agent-credentials/index.html" "--from-env"
require_text "build/agent-credentials/index.html" "--project"
require_text "build/agent-credentials/index.html" "--name LINEAR_API_TOKEN"
require_text "build/agent-credentials/index.html" '<td>Current process environment</td>'
require_text "build/agent-credentials/index.html" '<td>Owner-only, Git-ignored project <code>.env.local</code></td>'
reject_text "build/agent-credentials/index.html" '<p>1. the current process environment;</p>'

require_text "build/agent-operations/index.html" "kujo agent inspect"
require_text "build/agent-operations/index.html" "kujo agent run"
require_text "build/agent-operations/index.html" "kujo agent eval"
require_text "build/agent-operations/index.html" "--workcell"
require_text "build/agent-operations/index.html" '<p>The fixture path remains deterministic. A live provider run uses the configured model and the credential resolution rules described in <a href="/build/agent-credentials/">Agent Credentials</a>.</p>'
require_text "build/ai-and-agents/index.html" '<a href="/build/owned-agent-projects/">Agent Projects</a>'
require_text "tools/kujo/index.html" '<a href="/build/owned-agent-projects/">Agent Projects guide</a>'

for route in \
  build/owned-agent-projects/index.html \
  build/agent-profiles/index.html \
  build/agent-credentials/index.html \
  build/agent-operations/index.html \
  build/ai-and-agents/index.html \
  tools/kujo/index.html; do
  if grep -Eq '\[[^]]+\]\([^)]*\)' "$output_dir/$route"; then
    printf 'unrendered Markdown link in %s\n' "$route" >&2
    exit 1
  fi
done

require_text "sitemap.xml" "/build/owned-agent-projects/"
require_text "sitemap.xml" "/build/agent-profiles/"
require_text "sitemap.xml" "/build/agent-credentials/"
require_text "sitemap.xml" "/build/agent-operations/"
require_text "llms.txt" "Repository-owned Agent Projects"
require_text ".well-known/kujo-site-index.json" "owned-agent-projects"
require_text ".well-known/kujo-site-index.json" "agent-credentials"
require_text "build/owned-agent-projects/index.html" "data-kujo-webmcp"
require_text "build/publishing-house-operator/index.html" "Configure live execution"
require_text "build/publishing-house-operator/index.html" "PUBLISHING_HOUSE_PHASE_ADAPTER"
require_text "build/publishing-house-operator/index.html" "--json resume ITEM_ID"
require_text "build/publishing-house-operator/index.html" "kujo-workflows 0.4.0"
require_text "build/editorial-publishing/index.html" "kujo-workflows 0.4.0"
require_text "collections/workflows/index.html" "38 workflow kits"
require_text "collections/workflows/index.html" "Owned Agent Project workflow"
reject_text "build/publishing-house-operator/index.html" "fixture-operational"
require_text "assets/js/docs.js" "updateScrollableCodeBlocks"

require_file "tools/paperclip/index.html"
require_text "tools/paperclip/index.html" "npx paperclipai plugin install @kujolang/paperclip"
require_text "tools/paperclip/index.html" "kujolang.paperclip:get-context-content"
require_text "tools/paperclip/index.html" "paperclipai/paperclip/pull/12745"
require_text "ecosystem/tooling/index.html" 'href="/tools/paperclip/"'
require_text "sitemap.xml" "/tools/paperclip/"
require_text "llms.txt" "Kujo for Paperclip"
require_text ".well-known/kujo-site-index.json" "paperclip"
require_text "build/agent-operations/index.html" 'href="/review/" rel="next"'
require_text "build/agent-profiles/index.html" 'href="/tools/rag/"'
reject_text "build/agent-profiles/index.html" '/tools/rag-starter-kit/'
require_text "ecosystem/showcases/index.html" '<title>Showcase Directory | Kujo Docs</title>'
require_text "tools/index.html" 'Use Kujo tools for agents, orchestration, evidence, quality, publishing, and operations.'
require_text "index.html" 'width="32" height="32"'

printf 'Agent platform documentation contract passed.\n'
