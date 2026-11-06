# -*- coding: utf-8 -*-
"""Rendu des blocs de contenu vers DOCX et PDF."""
import os
import charte as C
from docx_engine import DocxBuilder
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import pdf_engine as PE
from reportlab.platypus import PageBreak

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")


def _last_is_break(story):
    for f in reversed(story):
        if isinstance(f, PageBreak):
            return True
        return False
    return True


# ------------------------------------------------------------------ DOCX
def render_docx(blocks, path, header_left, footer_left, title):
    d = DocxBuilder(title, header_left, footer_left)
    d._pending_break = False

    def brk(par):
        if d._pending_break:
            par.paragraph_format.page_break_before = True
            d._pending_break = False

    for b in blocks:
        t = b["t"]
        if t == "cover":
            _docx_cover(d, b["data"])
        elif t == "toc":
            d.toc()
        elif t == "section":
            d.section_page(b["num"], b["title"], b.get("sub", ""))
            d._pending_break = True
        elif t in ("h2", "h3"):
            par = d.heading(b["text"], 2 if t == "h2" else 3)
            brk(par)
        elif t == "p":
            par = d.p(b["text"], size=11.5 if b.get("lead") else C.SZ_BODY)
            brk(par)
        elif t == "bul":
            if d._pending_break:
                d.spacer(1)
                d._pending_break = False
            d.bullets(b["items"])
        elif t == "num":
            if d._pending_break:
                d.spacer(1)
                d._pending_break = False
            d.numbered(b["items"])
        elif t == "table":
            if d._pending_break:
                ppar = d.doc.add_paragraph()
                ppar.paragraph_format.page_break_before = True
                ppar.paragraph_format.space_after = Pt(0)
                d._pending_break = False
            d.table(b["header"], b["rows"], b["widths"], caption=b["caption"],
                    caption_num=b["num"], font=b["font"], first_col_bold=b["first_bold"],
                    align_center=b["center"], total_row=b["total"], band=b["band"],
                    colors=b.get("colors"))
       	elif t == "callout":
            if d._pending_break:
                d._pending_break = False
            d.callout(b["title"], b["text"], b.get("icon"),
                      fill=b.get("fill", C.LIGHT_BLUE), accent=b.get("accent", C.PRIMARY))
        elif t == "img":
            path_img = b["path"]
            w = b["w_cm"]
            d.image(path_img, min(w, C.CONTENT_W_CM), caption=b.get("caption"))
        elif t == "note":
            par = d.doc.add_paragraph()
            brk(par)
            from docx_engine import add_inline
            par.paragraph_format.space_before = Pt(3)
            par.paragraph_format.space_after = Pt(8)
            par.paragraph_format.line_spacing = 1.15
            add_inline(par, b["text"], size=C.SZ_CAPTION + 0.5, color=C.GREY, italic=True)
        elif t == "pagebreak":
            d.page_break()
        elif t == "land_start":
            d.new_section(landscape=True)
        elif t == "land_end":
            d.new_section(landscape=False)
    d.save(path)


def _docx_cover(d, data):
    from docx_engine import add_inline, set_run_font, para_bottom_rule, shade
    W = C.CONTENT_W_CM
    p0 = d.doc.add_paragraph()
    p0.paragraph_format.space_before = Pt(48)
    p0.paragraph_format.space_after = Pt(0)

    # bandeau supérieur
    band = d.doc.add_table(rows=1, cols=1)
    from docx_engine import no_borders, cell_margins, fixed_layout
    band.autofit = False
    fixed_layout(band)
    no_borders(band)
    cell_margins(band, 0.0, 0.0, 0.0, 0.0)
    c = band.rows[0].cells[0]
    c.width = Cm(W)
    shade(c, C.SECONDARY)
    pp = c.paragraphs[0]
    pp.paragraph_format.space_after = Pt(0)
    pp.paragraph_format.line_spacing = 1.0
    r = pp.add_run(" ")
    set_run_font(r, C.FONT_DOCX, 2, C.SECONDARY)

    d.spacer(18)
    par = d.doc.add_paragraph()
    par.paragraph_format.space_after = Pt(4)
    add_inline(par, data["kicker"], size=9, color=C.SECONDARY, bold=True)

    par = d.doc.add_paragraph()
    par.paragraph_format.space_after = Pt(6)
    par.paragraph_format.line_spacing = 1.0
    add_inline(par, data["title"], size=25, color=C.PRIMARY, base_font=C.FONT_DOCX_L)

    par = d.doc.add_paragraph()
    par.paragraph_format.space_before = Pt(2)
    par.paragraph_format.space_after = Pt(12)
    para_bottom_rule(par, C.ACCENT, 24)

    par = d.doc.add_paragraph()
    par.paragraph_format.space_after = Pt(10)
    par.paragraph_format.line_spacing = 1.0
    add_inline(par, data["subtitle"], size=19, color=C.SECONDARY, base_font=C.FONT_DOCX_L)

    par = d.doc.add_paragraph()
    par.paragraph_format.space_after = Pt(26)
    add_inline(par, data["consortium"], size=11.5, color=C.TEXT)

    rows = data["info"]
    t = d.doc.add_table(rows=0, cols=2)
    t.autofit = False
    fixed_layout(t)
    from docx_engine import table_borders
    table_borders(t, C.BORDER, 6)
    cell_margins(t, 0.05, 0.16, 0.05, 0.16)
    for k, v in rows:
        tr = t.add_row()
        c0, c1 = tr.cells[0], tr.cells[1]
        c0.width = Cm(4.6)
        c1.width = Cm(W - 4.6)
        shade(c0, C.LIGHT_BLUE)
        pc = c0.paragraphs[0]
        pc.paragraph_format.space_after = Pt(0)
        pc.paragraph_format.line_spacing = 1.0
        add_inline(pc, k, size=9, color=C.GREY, bold=True)
        pc = c1.paragraphs[0]
        pc.paragraph_format.space_after = Pt(0)
        pc.paragraph_format.line_spacing = 1.0
        add_inline(pc, v, size=9, color=C.TEXT)

    d.spacer(26)
    par = d.doc.add_paragraph()
    par.paragraph_format.space_before = Pt(6)
    add_inline(par, data["footer"], size=8, color=C.GREY, italic=True)
    d.page_break()


# ------------------------------------------------------------------ PDF
def render_pdf(blocks, path, header_left, footer_left, title):
    b = PE.PdfBuilder(title, header_left, footer_left, path)
    for bl in blocks:
        t = bl["t"]
        if t == "cover":
            b.cover(bl["data"])
        elif t == "toc":
            b.toc()
        elif t == "section":
            if not _last_is_break(b.story):
                b.add(PageBreak())
            b.section(bl["num"], bl["title"], bl.get("sub", ""))
            b.add(PageBreak())
        elif t == "h2":
            b.h2(bl["text"])
        elif t == "h3":
            b.h3(bl["text"])
        elif t == "p":
            b.p(bl["text"], "lead" if bl.get("lead") else "body")
        elif t == "bul":
            b.bullets(bl["items"])
        elif t == "num":
            b.numbered(bl["items"])
        elif t == "table":
            b.table(bl["header"], bl["rows"], bl["widths"], caption=bl["caption"],
                    num=bl["num"], font=bl["font"], first_bold=bl["first_bold"],
                    center=bl["center"], total=bl["total"], band=bl["band"],
                    colors=bl.get("colors"))
        elif t == "callout":
            b.callout(bl["title"], bl["text"], bl.get("icon"),
                      fill=bl.get("fill", C.LIGHT_BLUE), accent=bl.get("accent", C.PRIMARY))
        elif t == "img":
            b.image(bl["path"], min(bl["w_cm"], C.CONTENT_W_CM), caption=bl.get("caption"))
        elif t == "note":
            b.note(bl["text"])
        elif t == "pagebreak":
            b.page_break()
        elif t == "land_start":
            b.land_start()
        elif t == "land_end":
            b.land_end()
    b.save()
