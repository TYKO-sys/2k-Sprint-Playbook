#!/usr/bin/env python3
"""Count characters of paste-ready copy blocks in the marketing kit HTML.
Fiverr: title <= 80 chars, description <= 1200 chars.
Instagram: caption <= 2200 chars (target ~2050-2190 to 'use them all').
Counts are len() over the unescaped plain text (entity codes resolved)."""
import re, html as htmlmod, sys

PATH = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit.html"
raw = open(PATH, encoding="utf-8").read()

def text_of_div(src):
    """Extract text content of a <div class="copy-body">...</div> block (no nested divs)."""
    m = re.search(r'<div class="copy-body">(.*?)</div>', src, re.S)
    if not m:
        return None
    inner = m.group(1)
    inner = re.sub(r'<br\s*/?>', '\n', inner)
    inner = re.sub(r'<[^>]+>', '', inner)          # strip tags
    inner = htmlmod.unescape(inner)
    inner = inner.replace('\r', '')
    # normalize: collapse runs of blank lines to double newline, strip edges
    inner = re.sub(r'\n{3,}', '\n\n', inner.strip())
    return inner

def block_after(marker_id):
    idx = raw.find('id="%s"' % marker_id)
    if idx == -1:
        return None
    tail = raw[idx:]
    return text_of_div(tail)

targets = [
    ("count-gig1", "Fiverr Gig 1 description", 1200),
    ("count-gig2", "Fiverr Gig 2 description", 1200),
    ("count-gig3", "Fiverr Gig 3 description", 1200),
    ("count-ig1",  "Instagram Post 1 caption", 2200),
    ("count-ig2",  "Instagram Post 2 caption", 2200),
]
results = {}
for tid, label, limit in targets:
    t = block_after(tid)
    if t is None:
        print(f"[MISS] {label}: marker {tid} not found")
        continue
    n = len(t)
    status = "OK " if n <= limit else "OVER"
    results[tid] = n
    print(f"[{status}] {label}: {n} / {limit} chars")

# Fiverr title options: the copyboxes right after each 'count-gigX' marker are descriptions;
# title boxes are the ones with meta 'Pick one'. Extract them separately.
title_blocks = re.findall(r'<div class="copy-meta"><span>Pick one</span><span>fiverr title</span></div>\s*<div class="copy-body">(.*?)</div>', raw, re.S)
print(f"\nFiverr title option sets found: {len(title_blocks)}")
for i, tb in enumerate(title_blocks, 1):
    lines = [htmlmod.unescape(re.sub(r'<[^>]+>', '', l)).strip() for l in tb.strip().split('\n') if l.strip()]
    for l in lines:
        n = len(l)
        status = "OK " if n <= 80 else "OVER"
        print(f"  [{status}] Gig {i} title ({n} chars): {l}")

# Tag length check (Fiverr: 20 chars max per tag)
tag_blocks = re.findall(r'<span class="tag">([^<]+)</span>', raw)
print(f"\nTags found: {len(tag_blocks)}")
for t in dict.fromkeys(tag_blocks):
    n = len(t)
    status = "OK " if n <= 20 else "OVER"
    print(f"  [{status}] tag ({n} chars): {t}")

# Banned-word sweep on visible text of the document
visible = re.sub(r'<style.*?</style>', '', raw, flags=re.S)
visible = re.sub(r'<script.*?</script>', '', visible, flags=re.S)
visible = re.sub(r'<[^>]+>', ' ', visible)
visible = htmlmod.unescape(visible)
banned = ["meticulous", "meticulously", "navigating", "complexities", "realm",
          "understanding", " dive", "dive ", "shall", "tailored", "towards",
          "underpins", "everchanging", "ever-evolving", "the world of",
          "not only", "alright", "embark", "journey", "In today's digital age",
          "hey", "game changer", "designed to enhance", "it is advisable",
          "daunting", "when it comes to", "in the realm of", "amongst",
          "unlock the secrets", "unveil the secrets", "robust", "diving",
          "elevate", "unleash", "power", "cutting-edge", "rapidly",
          "expanding", "mastering", "excels", "harness"]
low = visible.lower()
hits = []
for w in banned:
    for m in re.finditer(r'\b' + re.escape(w.strip()) + r'\b', low):
        ctx = low[max(0, m.start()-40):m.end()+40].replace('\n', ' ')
        hits.append((w, ctx))
print(f"\nBanned-word sweep: {len(hits)} hit(s)")
for w, ctx in hits:
    print(f"  [{w}] ...{ctx}...")

# save counts for label update
import json
json.dump(results, open("/home/z/my-project/research/char_counts.json", "w"), indent=1)
print("\nCounts saved to research/char_counts.json")
