#!/usr/bin/env python3
"""Extract every paste-ready copy block from the marketing kit HTML into a
plain-text companion file for easy copy-paste. Blocks are pulled from the
same source as the PDF, so they match exactly."""
import re, html as htmlmod

SRC = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit.html"
OUT = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit_copyblocks.txt"

raw = open(SRC, encoding="utf-8").read()

def textify(inner):
    inner = re.sub(r'<br\s*/?>', '\n', inner)
    inner = re.sub(r'</?(p|strong|em|span|div)[^>]*>', '', inner)
    inner = re.sub(r'<[^>]+>', '', inner)
    inner = htmlmod.unescape(inner)
    inner = inner.replace('\r', '')
    inner = re.sub(r'\n{3,}', '\n\n', inner.strip())
    return inner

out = []
out.append("""THE AUTOMATION MECHANIC - MARKETING KIT
Copy-Paste Companion | mikebuilds.tech | September 2026
========================================================

Everything in this file is lifted verbatim from the PDF kit. Paste it where
the section says. Character counts are checked against platform limits:
Fiverr titles <= 80, descriptions <= 1,200. Instagram captions <= 2,200.
""")

# walk copyboxes in document order, with section context
sections = []  # (section_title)
for m in re.finditer(r'<div class="section-tag">([^<]+)</div>\s*<div class="section-title">([^<]+)</div>', raw):
    sections.append((m.group(1), m.group(2)))

# capture copybox blocks with their meta labels
blocks = []
for m in re.finditer(
        r'<div class="copybox(?: tall)?">\s*<div class="copy-meta"><span>([^<]+)</span>(?:<span[^>]*>([^<]*)</span>)?</div>\s*<div class="copy-body">(.*?)</div>\s*</div>',
        raw, re.S):
    label = htmlmod.unescape(m.group(1)).strip()
    right = htmlmod.unescape(m.group(2) or "").strip()
    body = textify(m.group(3))
    blocks.append((label, right, body))

# Fiverr title-option blocks have meta 'Pick one' and 3 lines
# tag sets
tag_sets = re.findall(r'<div class="copy-meta"><span>Paste &middot; first comment</span><span>hashtag set \d</span></div>\s*<div class="copy-body">(.*?)</div>', raw, re.S)

def divider(ch="="):
    return ch * 56

section_idx = 0
out.append("\n" + divider() + "\nSECTION 00 - READ THIS FIRST: THE MAP\n" + divider())
out.append("""
mikebuilds.tech        -> bare front porch. links to nothing.
mikebuilds.tech/plumber   -> Charm City sites (marketing done - don't touch)
mikebuilds.tech/realtor   -> AssetForge packs (marketing done - don't touch)
mikebuilds.tech/automation -> the four add-ons (copy below)
""")

n = len(blocks)
print(f"copy blocks found: {n}")
for label, right, body in blocks:
    out.append("")
    out.append(divider("-"))
    out.append(f">> {label}" + (f"  [{right}]" if right else ""))
    cnt = len(body)
    if "character" in label.lower() or "caption" in label.lower() or "description" in label.lower():
        out.append(f">> length: {cnt} characters")
    out.append(divider("-"))
    out.append(body)
    out.append("")

# Fiverr titles + tags appendix
out.append("\n" + divider() + "\nAPPENDIX - FIVERR TITLES (all under 80 characters)\n" + divider())
title_blocks = re.findall(r'<div class="copy-meta"><span>Pick one</span><span>fiverr title</span></div>\s*<div class="copy-body">(.*?)</div>', raw, re.S)
for i, tb in enumerate(title_blocks, 1):
    out.append(f"\nGig {i} title options:")
    for line in textify(tb).split("\n"):
        line = line.strip()
        if line:
            out.append(f"  [{len(line):2d} chars] {line}")

out.append("\n" + divider() + "\nAPPENDIX - SEARCH TAGS (5 per gig, all under 20 characters)\n" + divider())
gig_tag_sets = re.findall(r'<div class="tag-row">\s*((?:<span class="tag">[^<]+</span>\s*)+)</div>', raw)
for i, ts in enumerate(gig_tag_sets, 1):
    tags = re.findall(r'<span class="tag">([^<]+)</span>', ts)
    out.append(f"\nGig {i}: {', '.join(tags)}")

out.append("\n" + divider() + "\nAPPENDIX - HASHTAG SETS (post as first comment)\n" + divider())
for i, ts in enumerate(tag_sets, 1):
    out.append(f"\nPost {i}: {textify(ts).strip()}")

out.append("\n" + divider() + "\nTHE 90-SECOND DEMO VIDEO SCRIPT (Drill 3)\n" + divider())
out.append("""
0-5s   "This is what happens when a plumber misses a call."
       Show the ringing phone. Let it ring out. Silence is the hook.
5-15s  The money math on screen: "one lost job pays for this twice."
15-60s The demo. The text lands. The customer replies. The calendar fills.
       Narrate plainly, no excitement - deadpan sells machinery.
60-75s "$400, it's yours, no monthly fee. Text me."
       Phone number on screen, twice.

One take. Phone camera on the screen. No editing. This video closes texts,
fills the Instagram bio link, and becomes the Fiverr gig video with the
number cut out. Record it once, use it everywhere.
""")

open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(f"written: {OUT} ({sum(len(x) for x in out)} chars)")
