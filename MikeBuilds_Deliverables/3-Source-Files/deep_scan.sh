#!/usr/bin/env bash
# deep_scan.sh - verify core tool repos + fill remaining pricing gaps
set -u
OUT="/home/z/my-project/research"
mkdir -p "$OUT"

search() {
  local name="$1"; local query="$2"; local num="${3:-8}"; local rec="${4:-}"
  echo ">>> Search: $name"
  local args="{\"query\": \"$query\", \"num\": $num"
  [ -n "$rec" ] && args="$args, \"recency_days\": $rec"
  args="$args}"
  if z-ai function -n web_search -a "$args" -o "$OUT/search_$name.json"; then
    echo "    saved"
  else
    echo "    FAILED: $name"
  fi
}

fetch() {
  local name="$1"; local url="$2"
  echo ">>> Fetching tool: $name"
  if z-ai function -n page_reader -a "{\"url\": \"$url\"}" -o "$OUT/tool_$name.json"; then
    echo "    saved"
  else
    echo "    FAILED: $name"
  fi
}

search "gumroad_products" "best selling digital products Gumroad Notion templates prompt packs income" 8 365
search "fiverr_automation_gig" "Fiverr Upwork gig price AI automation chatbot workflow setup freelancer" 8 365

fetch "n8n"             "https://github.com/n8n-io/n8n"
fetch "scrapling"       "https://github.com/d4vinci/scrapling"
fetch "changedetection" "https://github.com/dgtlmoon/changedetection.io"
fetch "openseo"         "https://github.com/every-app/open-seo"
fetch "postiz"          "https://github.com/gitroomhq/postiz-app"
fetch "pipecat"         "https://github.com/pipecat-ai/pipecat"

echo ""
echo ">>> Done:"
ls -la "$OUT"/search_gumroad* "$OUT"/search_fiverr_automation* "$OUT"/tool_*.json 2>/dev/null
