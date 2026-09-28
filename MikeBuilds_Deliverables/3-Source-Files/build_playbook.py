#!/usr/bin/env python3
"""build_playbook.py - body PDF for 'The $2K Sprint Playbook'.

Report route (ReportLab). Cover is generated separately via html2poster.js
(Template 07 Crystal Blue) and merged with pypdf afterwards.

Palette: Template 07 Crystal Blue fixed body palette (per typesetting/cover.md).
Fonts: allowed set only - FreeSerif family + DejaVuSans mono. install_font_fallback() called.
TOC: TocDocTemplate + multiBuild + clickable bookmark keys.
"""
import os
import sys
import hashlib

PDF_SKILL_DIR = "/home/z/my-project/skills/pdf"
sys.path.insert(0, os.path.join(PDF_SKILL_DIR, "scripts"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BUILD_DIR = "/home/z/my-project/research/build"
os.makedirs(BUILD_DIR, exist_ok=True)
BODY_PDF = os.path.join(BUILD_DIR, "body.pdf")
CHART_PNG = os.path.join(BUILD_DIR, "revenue_chart.png")

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image, KeepTogether, CondPageBreak, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents
from PIL import Image as PILImage

from playbook_text import CHAPTERS

# ----------------------------------------------------------------- fonts
FONT_DIR = "/usr/share/fonts"

pdfmetrics.registerFont(TTFont("NotoSerifSC", f"{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf"))
pdfmetrics.registerFont(TTFont("NotoSerifSC-Bold", f"{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf"))
pdfmetrics.registerFont(TTFont("SarasaMonoSC", f"{FONT_DIR}/truetype/chinese/SarasaMonoSC-Regular.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif", f"{FONT_DIR}/truetype/freefont/FreeSerif.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-Bold", f"{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-Italic", f"{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-BoldItalic", f"{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans", f"{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf"))

registerFontFamily("NotoSerifSC", normal="NotoSerifSC", bold="NotoSerifSC-Bold")
registerFontFamily("FreeSerif", normal="FreeSerif", bold="FreeSerif-Bold",
                   italic="FreeSerif-Italic", boldItalic="FreeSerif-BoldItalic")
registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans")

from pdf import install_font_fallback  # noqa: E402
install_font_fallback()

# ------------------------------------------- palette (Template 07 body set)
PAGE_BG      = colors.HexColor("#f5f8fc")   # XL
SECTION_BG   = colors.HexColor("#edf2f9")   # XL
CARD_BG      = colors.HexColor("#e4ecf5")   # L
TABLE_STRIPE = colors.HexColor("#eef3fa")   # L
HEADER_FILL  = colors.HexColor("#1a4a7a")   # M
BORDER       = colors.HexColor("#c0d0e2")   # S
ACCENT       = colors.HexColor("#2d7ab3")   # XS
TEXT_PRIMARY = colors.HexColor("#142840")
TEXT_MUTED   = colors.HexColor("#5a7a96")

TABLE_HEADER_COLOR = HEADER_FILL
TABLE_ROW_EVEN = colors.white
TABLE_ROW_ODD = TABLE_STRIPE

# ----------------------------------------------------------------- geometry
MARGIN = 0.9 * inch            # left == right (symmetry iron rule)
TOP_MARGIN = 0.95 * inch
BOTTOM_MARGIN = 0.85 * inch
PAGE_W, PAGE_H = A4
AVAIL_W = PAGE_W - 2 * MARGIN
AVAIL_H = PAGE_H - TOP_MARGIN - BOTTOM_MARGIN
MAX_KEEP_HEIGHT = PAGE_H * 0.4

# ----------------------------------------------------------------- styles
st_body = ParagraphStyle(
    "Body", fontName="FreeSerif", fontSize=10.5, leading=17,
    alignment=TA_JUSTIFY, textColor=TEXT_PRIMARY, spaceBefore=0, spaceAfter=10)

st_bullet = ParagraphStyle(
    "Bullet", fontName="FreeSerif", fontSize=10.5, leading=16,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY,
    leftIndent=16, bulletIndent=4, spaceBefore=0, spaceAfter=5,
    bulletFontName="FreeSerif", bulletFontSize=10.5)

st_h1 = ParagraphStyle(
    "H1", fontName="FreeSerif", fontSize=20, leading=25,
    alignment=TA_LEFT, textColor=HEADER_FILL, spaceBefore=18, spaceAfter=4)

st_h2 = ParagraphStyle(
    "H2", fontName="FreeSerif", fontSize=13.5, leading=18,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY, spaceBefore=14, spaceAfter=6)

st_caption = ParagraphStyle(
    "Caption", fontName="FreeSerif", fontSize=8.5, leading=12,
    alignment=TA_CENTER, textColor=TEXT_MUTED, spaceBefore=0, spaceAfter=0)

st_table_header = ParagraphStyle(
    "TblHead", fontName="FreeSerif", fontSize=9.5, leading=12.5,
    alignment=TA_LEFT, textColor=colors.white)

st_table_cell = ParagraphStyle(
    "TblCell", fontName="FreeSerif", fontSize=9, leading=12.5,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY)

st_stat_big = ParagraphStyle(
    "StatBig", fontName="FreeSerif", fontSize=19, leading=23,
    alignment=TA_CENTER, textColor=ACCENT)

st_stat_label = ParagraphStyle(
    "StatLabel", fontName="FreeSerif", fontSize=8.5, leading=11.5,
    alignment=TA_CENTER, textColor=TEXT_MUTED)

st_toc_title = ParagraphStyle(
    "TocTitle", fontName="FreeSerif", fontSize=20, leading=25,
    alignment=TA_LEFT, textColor=HEADER_FILL, spaceAfter=4)

st_toc_l0 = ParagraphStyle(
    "TOCL0", fontName="FreeSerif-Bold", fontSize=11, leading=21,
    leftIndent=0, textColor=TEXT_PRIMARY)

st_toc_l1 = ParagraphStyle(
    "TOCL1", fontName="FreeSerif", fontSize=9.5, leading=16,
    leftIndent=18, textColor=TEXT_MUTED)

# ----------------------------------------------------------------- helpers

def add_heading(text, style, level=0):
    """Heading Paragraph with TOC bookmark attributes (clickable)."""
    key = "h_%s" % hashlib.md5(text.encode()).hexdigest()[:8]
    p = Paragraph('<a name="%s"/><b>%s</b>' % (key, text), style)
    p.bookmark_name = key
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p


def safe_keep_together(elements):
    """KeepTogether only when the block is short enough (<= 40% page height)."""
    total_h = 0
    for el in elements:
        try:
            _w, h = el.wrap(AVAIL_W, PAGE_H)
        except Exception:
            h = 0
        total_h += h
    if total_h <= MAX_KEEP_HEIGHT:
        return [KeepTogether(elements)]
    elif len(elements) >= 2:
        return [KeepTogether(elements[:2])] + list(elements[2:])
    return list(elements)


def make_table(spec):
    ratios = spec["ratios"]
    col_widths = [r * AVAIL_W for r in ratios]
    scale = min(1.0, (AVAIL_W * 0.999) / sum(col_widths))
    col_widths = [w * scale for w in col_widths]
    data = [[Paragraph("<b>%s</b>" % h, st_table_header) for h in spec["headers"]]]
    for row in spec["rows"]:
        data.append([Paragraph(c, st_table_cell) for c in row])
    tbl = Table(data, colWidths=col_widths, hAlign="CENTER", repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
    ]
    for i in range(1, len(data)):
        bg = TABLE_ROW_EVEN if (i % 2 == 1) else TABLE_ROW_ODD
        style.append(("BACKGROUND", (0, i), (-1, i), bg))
    tbl.setStyle(TableStyle(style))
    return tbl


def make_callouts(items):
    nums = [Paragraph("<b>%s</b>" % n, st_stat_big) for n, _ in items]
    labels = [Paragraph(l, st_stat_label) for _, l in items]
    w = (AVAIL_W * 0.96) / len(items)
    tbl = Table([nums, labels], colWidths=[w] * len(items), hAlign="CENTER")
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 1, ACCENT),
        ("LINEBEFORE", (1, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
        ("TOPPADDING", (0, 1), (-1, 1), 2),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return tbl


def embed_chart(path=CHART_PNG, max_width=None, max_height=None):
    """Image with preserved aspect ratio, constrained to the content box."""
    if max_width is None:
        max_width = AVAIL_W
    if max_height is None:
        max_height = PAGE_H * 0.35
    pil = PILImage.open(path)
    ow, oh = pil.size
    ratio = min(max_width / ow if ow > max_width else 1.0,
                max_height / oh if oh > max_height else 1.0)
    return Image(path, width=ow * ratio, height=oh * ratio)


def make_chart():
    """Cumulative revenue chart. English labels, palette-family colors only."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    weeks = list(range(1, 9))
    cons = [0, 0, 150, 350, 600, 900, 1200, 1600]
    expc = [0, 50, 300, 650, 1050, 1450, 1800, 2250]
    aggr = [0, 150, 500, 1000, 1500, 2100, 2700, 3300]

    fig, ax = plt.subplots(figsize=(7.0, 3.1), dpi=200, constrained_layout=True)
    ax.plot(weeks, aggr, color="#1a4a7a", lw=2.4, label="Aggressive", solid_capstyle="round")
    ax.plot(weeks, expc, color="#2d7ab3", lw=2.6, label="Expected", solid_capstyle="round")
    ax.fill_between(weeks, expc, color="#2d7ab3", alpha=0.08, linewidth=0)
    ax.plot(weeks, cons, color="#5a7a96", lw=2.2, ls="--", label="Conservative")

    # first/last labeling rule: label the end values only
    for ys, c in [(aggr, "#1a4a7a"), (expc, "#2d7ab3"), (cons, "#5a7a96")]:
        ax.plot(weeks[-1], ys[-1], "o", color=c, ms=4.5)
        ax.annotate("$%s" % format(ys[-1], ","), (weeks[-1], ys[-1]),
                    textcoords="offset points", xytext=(7, 0),
                    fontsize=9, color=c, va="center", fontweight="bold")
    ax.annotate("$0", (1, 0), textcoords="offset points", xytext=(0, 9),
                fontsize=8.5, color="#5a7a96", ha="center")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#c0d0e2")
    ax.spines["bottom"].set_color("#c0d0e2")
    ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.25, color="#5a7a96")
    ax.set_axisbelow(True)
    ax.set_xlabel("Week", fontsize=10, color="#142840")
    ax.set_ylabel("Cumulative revenue (USD)", fontsize=10, color="#142840")
    ax.tick_params(colors="#5a7a96", labelsize=9)
    ax.set_xlim(0.8, 8.6)
    ax.set_ylim(0, 3600)
    ax.set_xticks(weeks)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.01), ncol=3,
              frameon=False, fontsize=9)
    fig.savefig(CHART_PNG)
    plt.close(fig)


# ----------------------------------------------------------- doc template
class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, "bookmark_name"):
            level = getattr(flowable, "bookmark_level", 0)
            text = getattr(flowable, "bookmark_text", "")
            key = getattr(flowable, "bookmark_key", "")
            self.notify("TOCEntry", (level, text, self.page, key))


def draw_page(canvas, doc):
    """Page background + header + footer. TOC page = roman i, body = arabic."""
    canvas.saveState()
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # header: title left + accent rule
    canvas.setFont("FreeSerif", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, PAGE_H - 40, "THE $2K SPRINT PLAYBOOK")
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.2)
    canvas.line(MARGIN, PAGE_H - 46, PAGE_W - MARGIN, PAGE_H - 46)
    # footer: author left, page number right, light rule above
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 40, PAGE_W - MARGIN, 40)
    canvas.setFont("FreeSerif", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, 29, "Z.ai")
    page_label = "i" if doc.page == 1 else str(doc.page - 1)
    canvas.drawRightString(PAGE_W - MARGIN, 29, page_label)
    canvas.restoreState()


# ----------------------------------------------------------------- assembly
def build():
    make_chart()

    doc = TocDocTemplate(
        BODY_PDF,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN,
        title="The $2K Sprint Playbook",
        author="Z.ai", creator="Z.ai",
        subject="AI-driven business plans for an 8-week, zero-budget sprint to $2,000",
    )

    story = []

    # ---- TOC page (front matter, roman numbering)
    story.append(Paragraph("<b>Contents</b>", st_toc_title))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT,
                            spaceBefore=2, spaceAfter=12))
    toc = TableOfContents()
    toc.levelStyles = [st_toc_l0, st_toc_l1]
    toc.dotsMinLevel = 0
    story.append(toc)
    story.append(PageBreak())

    # ---- chapters
    for idx, ch in enumerate(CHAPTERS, start=1):
        heading_text = "%02d  ·  %s" % (idx, ch["title"])
        story.append(CondPageBreak(AVAIL_H * 0.25))
        h1 = add_heading(heading_text, st_h1, level=0)
        rule = HRFlowable(width="100%", thickness=1.2, color=ACCENT,
                          spaceBefore=2, spaceAfter=12)

        flow = []
        blocks = ch["blocks"]
        i = 0
        while i < len(blocks):
            kind, payload = blocks[i][0], blocks[i][1]
            if kind == "p":
                flow.append(Paragraph(payload, st_body))
            elif kind == "h2":
                h2 = add_heading(payload, st_h2, level=1)
                if i + 1 < len(blocks) and blocks[i + 1][0] == "p":
                    flow.extend(safe_keep_together(
                        [h2, Paragraph(blocks[i + 1][1], st_body)]))
                    i += 1
                else:
                    flow.extend(safe_keep_together([h2]))
            elif kind == "bullets":
                bl = [Paragraph(t, st_bullet, bulletText="•") for t in payload]
                flow.extend(safe_keep_together(bl))
            elif kind == "table":
                flow.append(Spacer(1, 12))
                flow.append(make_table(payload))
                if i + 1 < len(blocks) and blocks[i + 1][0] == "caption":
                    flow.append(Spacer(1, 5))
                    flow.append(Paragraph(blocks[i + 1][1], st_caption))
                    flow.append(Spacer(1, 12))
                    i += 1
                else:
                    flow.append(Spacer(1, 12))
            elif kind == "callouts":
                flow.append(Spacer(1, 8))
                flow.append(make_callouts(payload))
                flow.append(Spacer(1, 12))
            elif kind == "chart":
                flow.append(Spacer(1, 12))
                img = embed_chart()
                if i + 1 < len(blocks) and blocks[i + 1][0] == "caption":
                    flow.extend(safe_keep_together(
                        [img, Spacer(1, 6),
                         Paragraph(blocks[i + 1][1], st_caption)]))
                    flow.append(Spacer(1, 12))
                    i += 1
                else:
                    flow.append(img)
                    flow.append(Spacer(1, 12))
            i += 1

        # heading + rule + first element stay together
        story.extend(safe_keep_together([h1, rule] + flow[:1]))
        story.extend(flow[1:])
        story.append(Spacer(1, 10))

    doc.multiBuild(story, onFirstPage=draw_page, onLaterPages=draw_page)
    print("body written ->", BODY_PDF)


if __name__ == "__main__":
    build()
