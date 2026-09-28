#!/usr/bin/env bash
# market_scan.sh - validate current pricing and demand for the shortlisted services
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
    echo "    saved -> $OUT/search_$name.json"
  else
    echo "    FAILED: $name"
  fi
}

search "automation_pricing" "AI automation agency pricing how much to charge small business n8n workflow" 8 365
search "leadgen_pricing" "lead generation service pricing per lead monthly retainer small business" 8 365
search "seo_audit_pricing" "freelance SEO audit price monthly retainer small business" 6 365
search "fiverr_ai_gigs" "best selling in demand AI services on Fiverr Upwork" 8 365
search "cold_email_rules" "cold email B2B CAN-SPAM rules Gmail sending limits deliverability" 6 730
search "clip_service" "short form video clips editing service pricing for creators monthly" 6 365

echo ""
echo ">>> Done:"
ls -la "$OUT"/search_*.json 2>/dev/null || echo "(no search files)"
