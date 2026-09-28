#!/usr/bin/env python3
"""merge_final.py - insert the Playwright cover as page 0 of the ReportLab body,
normalize page sizes to A4, write metadata, and output the final playbook PDF."""
import os
from pypdf import PdfReader, PdfWriter

BUILD = "/home/z/my-project/research/build"
DOWNLOAD = "/home/z/my-project/download"
os.makedirs(DOWNLOAD, exist_ok=True)

COVER_PDF = os.path.join(BUILD, "cover.pdf")
BODY_PDF = os.path.join(BUILD, "body.pdf")
FINAL_PDF = os.path.join(DOWNLOAD, "The_2K_Sprint_Playbook.pdf")

A4_W, A4_H = 595.28, 841.89


def normalize_page_to_a4(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.3 or abs(h - A4_H) > 0.3:
        page.scale_to(A4_W, A4_H)
    return page


writer = PdfWriter()
cover_page = PdfReader(COVER_PDF).pages[0]
writer.add_page(normalize_page_to_a4(cover_page))
for page in PdfReader(BODY_PDF).pages:
    writer.add_page(normalize_page_to_a4(page))

writer.add_metadata({
    "/Title": "The $2K Sprint Playbook",
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": "AI-driven business plans for an 8-week, zero-budget sprint to $2,000",
})

with open(FINAL_PDF, "wb") as f:
    writer.write(f)

n_pages = len(PdfReader(FINAL_PDF).pages)
size_kb = os.path.getsize(FINAL_PDF) / 1024
print(f"final -> {FINAL_PDF} ({n_pages} pages, {size_kb:.1f} KB)")
