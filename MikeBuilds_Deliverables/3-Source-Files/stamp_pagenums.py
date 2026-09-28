#!/usr/bin/env python3
"""Stamp bare Arabic page numbers on the marketing kit PDF.
Scheme (pagination.md): cover = hidden page 1; body pages show 1,2,3... starting
at the first content page; numbering continues through the ending page.
Dark pages get a light number; light pages get a muted dark number."""
import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

SRC = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit.pdf"
OUT = "/home/z/my-project/download/Automation_Mechanic_Marketing_Kit_numbered.pdf"

reader = PdfReader(SRC)
writer = PdfWriter()
n = len(reader.pages)
W = float(reader.pages[0].mediabox.width)
H = float(reader.pages[0].mediabox.height)
print(f"pages: {n}, size: {W:.0f}x{H:.0f}pt")

DARK_PAGES = {1, n}  # cover and ending (1-indexed)

for i, page in enumerate(reader.pages, start=1):
    if i == 1:
        writer.add_page(page)  # cover: no number
        continue
    num = str(i - 1)  # body numbering starts at 1 on PDF page 2
    dark = i in DARK_PAGES
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    c.setFont("Helvetica", 8.5)
    c.setFillColor(HexColor("#b5aca2") if dark else HexColor("#8a8581"))
    c.drawCentredString(W / 2, 16, num)
    c.save()
    buf.seek(0)
    overlay = PdfReader(buf).pages[0]
    page.merge_page(overlay)
    writer.add_page(page)

# metadata: reflect the document's owner, not the toolchain
writer.add_metadata({
    "/Title": "The Automation Mechanic — Marketing Kit",
    "/Author": "Mike Builds",
    "/Subject": "Paste-ready marketing materials for the $2K Sprint Playbook: automation upsell menu, Fiverr gigs, Upwork proposals, Instagram posts",
    "/Creator": "Z.ai",
})

with open(OUT, "wb") as f:
    writer.write(f)
print(f"written: {OUT}")
