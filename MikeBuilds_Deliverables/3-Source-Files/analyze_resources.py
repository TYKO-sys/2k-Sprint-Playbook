#!/usr/bin/env python3
"""analyze_resources.py - condense fetched JSON pages into readable text + link maps."""
import json, re, os, html as htmllib

RESEARCH = "/home/z/my-project/research"
OUT = os.path.join(RESEARCH, "condensed")
os.makedirs(OUT, exist_ok=True)

def strip_html(raw: str) -> str:
    raw = re.sub(r'<script[^>]*>.*?</script>', ' ', raw, flags=re.S | re.I)
    raw = re.sub(r'<style[^>]*>.*?</style>', ' ', raw, flags=re.S | re.I)
    # keep link targets visible
    raw = re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                 r'\2 <\1>', raw, flags=re.S | re.I)
    raw = re.sub(r'<br\s*/?>', '\n', raw, flags=re.I)
    raw = re.sub(r'</(p|div|li|h[1-6]|tr|section)>', '\n', raw, flags=re.I)
    raw = re.sub(r'<[^>]+>', '', raw)
    raw = htmllib.unescape(raw)
    raw = re.sub(r'[ \t]+', ' ', raw)
    raw = re.sub(r'\n\s*\n\s*\n+', '\n\n', raw)
    return raw.strip()

NAMES = ["fmhy_ai", "fmhy_linuxmacos", "fmhy_misc", "curated_catalog"]

for name in NAMES:
    path = os.path.join(RESEARCH, f"{name}.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    payload = data.get("data", data) if isinstance(data, dict) else data
    title = payload.get("title", "") or ""
    text = payload.get("text") or ""
    htmlc = payload.get("html") or ""
    if not text and htmlc:
        text = strip_html(htmlc)

    # section map: markdown-style headings and/or html h2/h3 captured pre-strip
    heads = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', htmlc, flags=re.S | re.I)
    heads = [re.sub(r'\s+', ' ', strip_html(h))[:90] for h in heads if h.strip()]
    md_heads = [ln.strip()[:90] for ln in text.splitlines()
                if re.match(r'^#{1,3}\s+\S', ln.strip())]

    urls = sorted(set(re.findall(r'https?://[^\s\]"<>)\]}]+', text)))

    out_path = os.path.join(OUT, f"{name}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"TITLE: {title}\nCHARS: {len(text)}\nURLS: {len(urls)}\n")
        f.write(f"HTML_HEADINGS: {len(heads)}\nMD_HEADINGS: {len(md_heads)}\n\n")
        if heads:
            f.write("== HTML SECTION MAP ==\n" + "\n".join(heads[:120]) + "\n\n")
        if md_heads:
            f.write("== MD SECTION MAP ==\n" + "\n".join(md_heads[:200]) + "\n\n")
        f.write("== FULL TEXT ==\n")
        f.write(text)
        f.write("\n\n== URL LIST ==\n")
        f.write("\n".join(urls))
    print(f"{name:18s} title={title[:60]!r} chars={len(text):7d} "
          f"urls={len(urls):4d} h-heads={len(heads):3d} md-heads={len(md_heads):3d}")

print("\ncondensed files in", OUT)
