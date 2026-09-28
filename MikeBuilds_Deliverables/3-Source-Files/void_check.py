#!/usr/bin/env python3
"""Per-page void analysis + text integrity checks for the marketing kit PDF."""
import pypdfium2 as pdfium

PDF = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit.pdf"

doc = pdfium.PdfDocument(PDF)
n = len(doc)
print(f"pages: {n}")

def analyze_page(i, scale=0.25):
    page = doc[i]
    bmp = page.render(scale=scale)
    pil = bmp.to_pil().convert("L")
    w, h = pil.size
    px = pil.load()
    # page background = majority color of the page border ring
    from collections import Counter
    samples = [px[x, 1] for x in range(0, w, 4)] + [px[x, h-2] for x in range(0, w, 4)] \
              + [px[1, y] for y in range(0, h, 4)] + [px[w-2, y] for y in range(0, h, 4)]
    bg = Counter(samples).most_common(1)[0][0]
    tol = 14
    def row_has_content(y):
        for x in range(0, w, 3):
            if abs(px[x, y] - bg) > tol:
                return True
        return False
    top_void = 0
    for y in range(0, h):
        if row_has_content(y):
            break
        top_void += 1
    bottom_void = 0
    for y in range(h - 1, -1, -1):
        if row_has_content(y):
            break
        bottom_void += 1
    content_rows = sum(1 for y in range(0, h, 2) if row_has_content(y))
    fill = content_rows / (h / 2)
    page.close()
    return bg, top_void / h, bottom_void / h, fill

print("\npage | bg | top-void | bottom-void | fill")
issues = 0
for i in range(n):
    bg, tv, bv, fill = analyze_page(i)
    flag = ""
    if tv > 0.12 and i not in (0, n-1):
        flag += "  <-- TOP VOID"
    if bv > 0.30 and i != n-1:
        flag += "  <-- BOTTOM VOID"
    if flag:
        issues += 1
    print(f"{i+1:4d} | {bg:3d} | {tv*100:7.1f}% | {bv*100:10.1f}% | {fill*100:5.1f}%{flag}")
print(f"\npages with void issues: {issues} (excluding designed cover/ending)")

# ---- text extraction via pdfium ----
alltext = ""
for i in range(n):
    tp = doc[i].get_textpage()
    alltext += tp.get_text_bounded() + "\n"
bad = alltext.count("\ufffd")
print(f"\nU+FFFD count: {bad}")
for probe in ["$400 a job is $3,200", "$500", "410-575-4192", "mikebuilds.tech/automation",
              "no monthly. $400 once", "2,178", "2,118", "1,038", "That's it? That's all it does?"]:
    print(f"probe '{probe}': {'FOUND' if probe in alltext else 'MISSING'}")
import re
suspicious = re.findall(r'katex|mathml|frac\{', alltext, re.I)
print(f"katex artifacts: {len(suspicious)}")
