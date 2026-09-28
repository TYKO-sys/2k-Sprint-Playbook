#!/usr/bin/env bash
# fetch_resources.sh - pull the user's resource pages for business-plan research
set -u
OUT="/home/z/my-project/research"
mkdir -p "$OUT"

fetch() {
  local name="$1"; local url="$2"
  echo ">>> Fetching $name ..."
  if z-ai function -n page_reader -a "{\"url\": \"$url\"}" -o "$OUT/$name.json"; then
    echo "    saved -> $OUT/$name.json"
  else
    echo "    FAILED: $name ($url)"
  fi
}

fetch "fmhy_ai"         "https://fmhy.net/ai"
fetch "fmhy_linuxmacos" "https://fmhy.net/linux-macos"
fetch "fmhy_misc"       "https://fmhy.net/misc"
fetch "curated_catalog" "https://github.com/user-attachments/files/32708278/curated_catalog.md"

echo ""
echo ">>> Fetch pass complete. Files in $OUT:"
ls -la "$OUT" 2>/dev/null || echo "(no files - all fetches failed)"
