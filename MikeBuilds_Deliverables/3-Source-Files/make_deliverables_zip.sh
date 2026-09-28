#!/bin/bash
set -euo pipefail

BASE=/home/z/my-project
STAGE_ROOT=$BASE/scripts/zip_stage
PKG=$STAGE_ROOT/MikeBuilds_Deliverables

rm -rf "$STAGE_ROOT"
mkdir -p "$PKG/1-The-2K-Sprint-Playbook" \
         "$PKG/2-Automation-Mechanic-Marketing-Kit" \
         "$PKG/3-Source-Files/research"

# README at zip root
cp "$BASE/scripts/readme_first.txt" "$PKG/README-FIRST.txt"

# Folder 1: the playbook
cp "$BASE/download/The_2K_Sprint_Playbook.pdf"        "$PKG/1-The-2K-Sprint-Playbook/"
cp "$BASE/download/The_2K_Sprint_Playbook_cover.html" "$PKG/1-The-2K-Sprint-Playbook/"

# Folder 2: the marketing kit
cp "$BASE/download/Automation_Mechanic_Marketing_Kit.pdf"             "$PKG/2-Automation-Mechanic-Marketing-Kit/"
cp "$BASE/download/Automation_Mechanic_Marketing_Kit_copyblocks.txt"  "$PKG/2-Automation-Mechanic-Marketing-Kit/"
cp "$BASE/download/Automation_Mechanic_Marketing_Kit.html"            "$PKG/2-Automation-Mechanic-Marketing-Kit/"
cp "$BASE/download/Automation_Mechanic_Marketing_Kit_cover.png"       "$PKG/2-Automation-Mechanic-Marketing-Kit/"

# Folder 3: source files (scripts + research, minus intermediate build artifacts)
cp "$BASE/scripts/"*.py "$BASE/scripts/"*.sh "$PKG/3-Source-Files/" 2>/dev/null || true
cp -r "$BASE/research/." "$PKG/3-Source-Files/research/"
rm -rf "$PKG/3-Source-Files/research/build"

# Build the zip
OUT=$BASE/download/MikeBuilds_Deliverables.zip
rm -f "$OUT"
( cd "$STAGE_ROOT" && zip -r -9 -q "$OUT" MikeBuilds_Deliverables )

echo "--- zip created ---"
du -h "$OUT"
echo "--- contents ---"
unzip -l "$OUT"
