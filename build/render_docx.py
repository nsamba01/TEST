# -*- coding: utf-8 -*-
"""Rendu DOCX — même modèle de blocs, même identité visuelle que le PDF.

Toutes les dimensions sont exprimées dans la même unité que le gabarit PDF
(points), de sorte que la mise en page soit identique dans les deux formats :
mêmes marges, mêmes largeurs de colonnes, mêmes tailles de police, même palette.
"""
import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Emu

import design as D
from ooxml_order import insert_ordered, set_child

EMU_PER_PT = 12700


def pt(v):
    """Points -> EMU (unité interne de python-docx)."""
    return Emu(int(round(v * EMU_PER_PT)))


def rgb(hexstr):
    h = hexstr.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


TAG_RE = re.compile(r"<[^>]+>")


def plain(s):
    return TAG_RE.sub("", str(s).replace("&nbsp;", " ")).replace("<br/>", " ")


def runs_of(text):
    """Convertit un mini-balisage (<b>, <i>, <font color>, <br/>) en segments."""
    text = str(text)
    out = []
    bold = italic = False
    color = None
    size = None
    buf = []

    def flush():
        if buf:
            out.append(("".join(buf), bold, italic, color, size))
            buf.clear()

    i = 0
    while i < len(text):
        if text.startswith("<br/>", i):
            flush()
            out.append(("\n", bold, italic, color, size))
            i += 5
        elif text.startswith("<b>", i):
            flush(); bold = True; i += 3
        elif text.startswith("</b>", i):
            flush(); bold = False; i += 4
        elif text.startswith("<i>", i):
            flush(); italic = True; i += 3
        elif text.startswith("</i>", i):
            flush(); italic = False; i += 4
        elif text.startswith("<font", i):
            flush()
            j = text.index(">", i)
            attrs = text[i:j]
            m = re.search(r'color="([^"]+)"', attrs)
            if m:
                color = m.group(1).lstrip("#")
            s = re.search(r'size="([\d.]+)"', attrs)
            if s:
                size = float(s.group(1))
            i = j + 1
        elif text.startswith("</font>", i):
            flush(); color = None; size = None; i += 7
        elif text.startswith("&nbsp;", i):
            buf.append(" "); i += 6
        else:
            buf.append(text[i]); i += 1
    flush()
    return out


def shade_cell(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor.lstrip("#"))
    set_child(tcPr, shd)


def _order(parent):
    """Réordonne les enfants d'un élément selon le schéma."""
    from ooxml_order import ORDERS, _tag
    order = ORDERS.get(_tag(parent))
    if not order:
        return
    kids = list(parent)
    kids.sort(key=lambda e: order.index(_tag(e)) if _tag(e) in order else len(order))
    for k in kids:
        parent.remove(k)
    for k in kids:
        parent.append(k)


def cell_margins(table, top=2, bottom=2, left=4, right=4):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        el = OxmlElement("w:%s" % side)
        el.set(qn("w:w"), str(int(val / 0.05)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)
    _order(tblPr)


def table_borders(table, color="C9D3DA", size=4):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:%s" % edge)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(size))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)


def _fixed_layout(table, total_pt):
    tblPr = table._tbl.tblPr
    for el in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(el)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    insert_ordered(tblPr, lay)
    w = tblPr.find(qn("w:tblW"))
    if w is None:
        w = OxmlElement("w:tblW")
        tblPr.append(w)
    w.set(qn("w:type"), "dxa")
    w.set(qn("w:w"), str(int(total_pt / 0.05)))
    _order(tblPr)


def keep_with_next(p):
    pPr = p._p.get_or_add_pPr()
    el = OxmlElement("w:keepNext")
    insert_ordered(pPr, el)


def no_split_row(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    insert_ordered(trPr, el)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    insert_ordered(trPr, el)


def field_begin(paragraph, instr):
    r = paragraph.add_run()
    el = OxmlElement("w:fldChar")
    el.set(qn("w:fldCharType"), "begin")
    r._r.append(el)
    r = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = " %s " % instr
    r._r.append(it)
    r = paragraph.add_run()
    el = OxmlElement("w:fldChar")
    el.set(qn("w:fldCharType"), "separate")
    r._r.append(el)


def field_end(paragraph):
    r = paragraph.add_run()
    el = OxmlElement("w:fldChar")
    el.set(qn("w:fldCharType"), "end")
    r._r.append(el)


def field(paragraph, instr, placeholder="1"):
    """Insère un champ Word (TOC, PAGE, NUMPAGES) avec un résultat de secours."""
    def _fld(kind):
        r = paragraph.add_run()
        el = OxmlElement("w:fldChar")
        el.set(qn("w:fldCharType"), kind)
        r._r.append(el)
        return r

    _fld("begin")
    r = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = " %s " % instr
    r._r.append(it)
    _fld("separate")
    paragraph.add_run(placeholder)
    _fld("end")


def update_fields_on_open(d):
    """Demande à Word de recalculer le sommaire et la pagination à l'ouverture."""
    settings = d.settings.element
    for el in settings.findall(qn("w:updateFields")):
        settings.remove(el)
    el = OxmlElement("w:updateFields")
    el.set(qn("w:val"), "true")
    compat = settings.find(qn("w:compat"))
    upd = settings.findall(qn("w:updateFields"))
    for u in upd:
        settings.remove(u)
    if compat is not None:
        compat.addprevious(el)
    else:
        settings.append(el)


# --------------------------------------------------------------------------
def build_docx(doc, path, toc_pages=None):
    d = Document()

    # ---- styles de base
    st = d.styles["Normal"]
    st.font.name = D.FONT
    st.font.size = Pt(D.SZ_BODY)
    st.font.color.rgb = rgb(D.GREY_TXT)
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), D.FONT)
    st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.line_spacing = 1.32

    # ---- sections : portrait puis paysage
    sec = d.sections[0]
    sec.page_width = pt(D.PAGE_W)
    sec.page_height = pt(D.PAGE_H)
    sec.top_margin = pt(D.M_TOP)
    sec.bottom_margin = pt(D.M_BOT)
    sec.left_margin = pt(D.M_LEFT)
    sec.right_margin = pt(D.M_RIGHT)
    sec.header_distance = pt(28)
    sec.footer_distance = pt(24)

    _cover(d, doc.meta)

    # corps : nouvelle section portrait (page de sommaire)
    body = d.add_section(WD_SECTION.NEW_PAGE)
    body.orientation = 0
    body.page_width = pt(D.PAGE_W)
    body.page_height = pt(D.PAGE_H)
    body.top_margin = pt(D.M_TOP)
    body.bottom_margin = pt(D.M_BOT)
    body.left_margin = pt(D.M_LEFT)
    body.right_margin = pt(D.M_RIGHT)
    _header_footer(d, doc.meta)

    _toc(d, doc, toc_pages)

    cur = "portrait"
    for b in doc.blocks:
        k = b["kind"]
        if k == "h1":
            if b.get("page_break", True):
                d.add_page_break()
            _h1(d, b)
        elif k == "h2":
            _h2(d, b)
        elif k == "h3":
            p = d.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            keep_with_next(p)
            _runs(p, b["text"], size=D.SZ_H3, bold=True, color=D.TEAL)
        elif k == "p":
            _para(d, b)
        elif k == "lead":
            p = d.add_paragraph()
            p.paragraph_format.space_after = Pt(9)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            _runs(p, b["text"], size=10.7, color=D.NAVY_D)
            _rule(d, 0.5, D.GREY_LN, 4)
        elif k == "bullets":
            _bullets(d, b)
        elif k == "table":
            if b.get("landscape") and cur != "landscape":
                _new_sec(d, landscape=True, meta=doc.meta)
                cur = "landscape"
            elif not b.get("landscape") and cur != "portrait":
                _new_sec(d, landscape=False, meta=doc.meta)
                cur = "portrait"
            _table(d, b, landscape=b.get("landscape"))
        elif k == "figure":
            _figure(d, b)
        elif k == "kpis":
            _kpis(d, b)
        elif k == "callout":
            _callout(d, b)
        elif k == "toc":
            _toc(d, doc)
        elif k == "spacer":
            d.add_paragraph().paragraph_format.space_after = Pt(b.get("h", 6))
        elif k == "pagebreak":
            d.add_page_break()

    update_fields_on_open(d)
    d.save(path)
    return {"pages": None, "path": path}


# --------------------------------------------------------------------------
def _runs(p, text, size=None, bold=None, italic=None, color=None, font=None):
    for seg, b, it, col, sz in runs_of(text):
        if seg == "\n":
            p.add_run().add_break()
            continue
        r = p.add_run(seg)
        r.bold = b if bold is None else (bold or b)
        r.italic = it if italic is None else (italic or it)
        r.font.name = D.FONT
        r._element.rPr.rFonts.set(qn("w:eastAsia"), D.FONT)
        if sz:
            r.font.size = Pt(sz)
        elif size:
            r.font.size = Pt(size)
        c = col or color
        if c:
            r.font.color.rgb = rgb(c)


def _rule(d, thickness=1.5, color=None, space_before=2, space_after=10):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    pPr = p._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(int(thickness * 8)))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), (color or D.NAVY).lstrip("#"))
    bd.append(bottom)
    insert_ordered(pPr, bd)


def _para(d, b):
    p = d.add_paragraph()
    p.paragraph_format.space_after = Pt(b.get("space", 5))
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if b.get("justify", True) else WD_ALIGN_PARAGRAPH.LEFT
    if b.get("keep"):
        keep_with_next(p)
    _runs(p, b["text"], size=b.get("size") or D.SZ_BODY, color=b.get("color"))


def _h1(d, b):
    num, title = b["num"], b["text"]
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    keep_with_next(p)
    kick = ("SECTION %s" % num) if num else "SECTION"
    r = p.add_run(kick)
    r.bold = True
    r.font.size = Pt(7.8)
    r.font.color.rgb = rgb(D.GOLD)
    r.font.name = D.FONT

    h = d.add_paragraph()
    h.paragraph_format.space_before = Pt(0)
    h.paragraph_format.space_after = Pt(4)
    keep_with_next(h)
    _runs(h, title, size=D.SZ_H1, bold=True, color=D.NAVY)
    _rule(d, 1.5, D.NAVY, 0, 10)


def _h2(d, b):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    keep_with_next(p)
    if b["num"]:
        r = p.add_run(b["num"] + "  ")
        r.bold = True
        r.font.size = Pt(D.SZ_H2)
        r.font.color.rgb = rgb(D.TEAL)
        r.font.name = D.FONT
    _runs(p, b["text"], size=D.SZ_H2, bold=True, color=D.NAVY)


def _bullets(d, b):
    for i, it in enumerate(b["items"], 1):
        p = d.add_paragraph()
        p.paragraph_format.left_indent = pt(14)
        p.paragraph_format.first_line_indent = pt(-8)
        p.paragraph_format.space_after = Pt(3)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if b.get("style", "dot") == "num":
            lead = "%d.  " % i
        else:
            lead = "\u25aa  "
        r = p.add_run(lead)
        r.font.size = Pt(8.2 if b.get("style", "dot") != "num" else D.SZ_BODY)
        r.font.color.rgb = rgb(D.TEAL)
        r.font.name = D.FONT
        _runs(p, it, size=b.get("size") or D.SZ_BODY)


def _table(d, b, landscape=False):
    total = D.LCONTENT_W if landscape else D.CONTENT_W
    if b.get("caption"):
        p = d.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        keep_with_next(p)
        _runs(p, b["caption"], size=8.0, bold=True, color=D.NAVY)

    widths = [total * w for w in b["widths"]]
    rows = b["rows"]
    ncol = len(b["cols"])
    fs = b.get("size") or 7.7
    align = b.get("align") or ["l"] * ncol

    t = d.add_table(rows=len(rows), cols=ncol)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    _fixed_layout(t, total)
    table_borders(t)
    cell_margins(t, top=2.2, bottom=2.2, left=4.2, right=4.2)
    for ci, w in enumerate(widths):
        for cell in t.columns[ci].cells:
            cell.width = pt(w)

    for ri, row in enumerate(rows):
        head = ri < b["head_rows"]
        no_split_row(t.rows[ri])
        if head and b.get("repeat_head", True):
            repeat_header(t.rows[ri])
        for ci, val in enumerate(row[:ncol]):
            cell = t.cell(ri, ci)
            cell.width = pt(widths[ci])
            para = cell.paragraphs[0]
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.line_spacing = 1.20
            a = align[ci] if ci < len(align) else "l"
            if head or a == "c":
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if head:
                shade_cell(cell, D.NAVY)
                _runs(para, "<b>%s</b>" % val, size=fs, color="FFFFFF")
            else:
                if b.get("zebra") and (ri - b["head_rows"]) % 2 == 1:
                    shade_cell(cell, D.GREY_BG)
                _runs(para, val, size=fs, color=D.GREY_TXT)

    if b.get("note"):
        p = d.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(10)
        _runs(p, b["note"], size=7.1, italic=True, color=D.GREY_MID)
    else:
        sp = d.add_paragraph()
        sp.paragraph_format.space_after = Pt(4)


def _figure(d, b):
    from PIL import Image as PILImage
    iw, ih = PILImage.open(b["path"]).size
    w = D.CONTENT_W * b.get("width_frac", 1.0)
    h = w * ih / iw
    p = d.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    keep_with_next(p)
    p.add_run().add_picture(b["path"], width=pt(w), height=pt(h))
    if b.get("caption"):
        c = d.add_paragraph()
        c.paragraph_format.space_after = Pt(3)
        keep_with_next(c)
        _runs(c, b["caption"], size=8.0, bold=True, color=D.NAVY)
    if b.get("note"):
        n = d.add_paragraph()
        n.paragraph_format.space_after = Pt(10)
        _runs(n, b["note"], size=7.1, italic=True, color=D.GREY_MID)


def _callout(d, b):
    tone = b.get("tone", "teal")
    accent = {"teal": D.TEAL, "gold": D.GOLD, "red": D.RED, "grey": D.GREY_MID}.get(tone, D.TEAL)
    bg = {"teal": "E4F1F2", "gold": "FBF3E3", "red": "F8EDED", "grey": "F2F5F7"}.get(tone, "E4F1F2")
    t = d.add_table(rows=1, cols=1)
    t.autofit = False
    cell = t.cell(0, 0)
    cell.width = pt(D.CONTENT_W)
    t.columns[0].width = pt(D.CONTENT_W)
    shade_cell(cell, bg)
    tblPr = t._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:%s" % edge)
        el.set(qn("w:val"), "nil")
        borders.append(el)
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "24")
    left.set(qn("w:space"), "0")
    left.set(qn("w:color"), accent.lstrip("#"))
    borders.append(left)
    tblPr.append(borders)
    cell_margins(t, top=5, bottom=5, left=8, right=8)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    _runs(p, "<b>%s</b>" % b["title"], size=8.6, color=accent)
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _runs(p2, b["text"], size=8.5, color=D.GREY_TXT)
    sp = d.add_paragraph()
    sp.paragraph_format.space_after = Pt(8)


def _kpis(d, b):
    items = b["items"]
    n = len(items)
    gap = 7
    cw = (D.CONTENT_W - gap * (n - 1)) / n
    t = d.add_table(rows=1, cols=n)
    t.autofit = False
    tblPr = t._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:%s" % edge)
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tblPr.append(borders)
    _order(tblPr)
    for i, (val, lab) in enumerate(items):
        cell = t.cell(0, i)
        cell.width = pt(cw)
        shade_cell(cell, D.GREY_BG)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(val)
        r.bold = True
        r.font.size = Pt(16.5)
        r.font.color.rgb = rgb(D.NAVY)
        r.font.name = D.FONT
        p2 = cell.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_after = Pt(6)
        r2 = p2.add_run(lab)
        r2.font.size = Pt(7.0)
        r2.font.color.rgb = rgb(D.GREY_MID)
        r2.font.name = D.FONT
        tcPr = cell._tc.get_or_add_tcPr()
        bdr = OxmlElement("w:tcBorders")
        top = OxmlElement("w:top")
        top.set(qn("w:val"), "single")
        top.set(qn("w:sz"), "16")
        top.set(qn("w:color"), D.TEAL)
        bdr.append(top)
        insert_ordered(tcPr, bdr)
    sp = d.add_paragraph()
    sp.paragraph_format.space_after = Pt(8)


def _toc(d, doc, pages=None):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("Sommaire")
    r.bold = True
    r.font.size = Pt(D.SZ_H1)
    r.font.color.rgb = rgb(D.NAVY)
    r.font.name = D.FONT
    _rule(d, 1.5, D.NAVY, 1, 10)
    entries = [(lvl, num, title) for (lvl, num, title) in doc.toc_entries if lvl in (1, 2)]
    if pages:
        first = d.add_paragraph()
        first.paragraph_format.space_after = Pt(0)
        field_begin(first, r'TOC \o "1-2" \h \z \u')
        for i, (lvl, num, title) in enumerate(entries):
            q = d.add_paragraph() if i else first
            q.paragraph_format.space_after = Pt(1.5)
            q.paragraph_format.tab_stops.add_tab_stop(
                pt(D.CONTENT_W), WD_ALIGN_PARAGRAPH.RIGHT, leader=2)
            if lvl == 1:
                q.paragraph_format.space_before = Pt(7)
                txt = (num + "  " if num else "") + title
                _runs(q, txt, size=9.4, bold=True, color=D.NAVY)
            else:
                q.paragraph_format.left_indent = pt(20)
                txt = ((num + "  ") if num else "") + title
                _runs(q, txt, size=8.7, color=D.GREY_TXT)
            r = q.add_run("\t" + str(pages.get(i, "")))
            r.font.size = Pt(9.0 if lvl == 1 else 8.7)
            r.bold = lvl == 1
            r.font.name = D.FONT
            r.font.color.rgb = rgb(D.NAVY if lvl == 1 else D.GREY_MID)
        last = d.add_paragraph()
        last.paragraph_format.space_after = Pt(4)
        field_end(last)
    else:
        para = d.add_paragraph()
        para.paragraph_format.space_after = Pt(4)
        field(para, r'TOC \o "1-2" \h \z \u',
              "Sommaire automatique à actualiser sous Word.")
    d.add_page_break()


def _header_footer(d, meta, sec=None):
    sec = sec or d.sections[-1]
    cw = sec.page_width.pt - sec.left_margin.pt - sec.right_margin.pt
    sec.different_first_page_header_footer = False
    hdr = sec.header
    hp = hdr.paragraphs[0]
    hp.text = ""
    hp.paragraph_format.tab_stops.add_tab_stop(pt(cw), WD_ALIGN_PARAGRAPH.RIGHT)
    r = hp.add_run(meta.get("header_left", ""))
    r.font.size = Pt(7.3)
    r.font.color.rgb = rgb(D.GREY_MID)
    r.font.name = D.FONT
    r2 = hp.add_run("\t" + meta.get("header_right", ""))
    r2.font.size = Pt(7.3)
    r2.font.color.rgb = rgb(D.GREY_MID)
    r2.font.name = D.FONT
    pPr = hp._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), D.GREY_LN)
    bd.append(bottom)
    insert_ordered(pPr, bd)

    ftr = sec.footer
    fp = ftr.paragraphs[0]
    fp.text = ""
    fp.paragraph_format.tab_stops.add_tab_stop(pt(cw / 2), WD_ALIGN_PARAGRAPH.CENTER)
    fp.paragraph_format.tab_stops.add_tab_stop(pt(cw), WD_ALIGN_PARAGRAPH.RIGHT)
    a = fp.add_run(meta.get("footer_left", ""))
    a.font.size = Pt(7.0)
    a.font.color.rgb = rgb(D.GREY_MID)
    a.font.name = D.FONT
    b = fp.add_run("\t" + meta.get("footer_center", ""))
    b.font.size = Pt(7.0)
    b.font.color.rgb = rgb(D.GREY_MID)
    b.font.name = D.FONT
    c = fp.add_run("\tPage ")
    c.font.size = Pt(7.8)
    c.font.color.rgb = rgb(D.NAVY)
    c.font.name = D.FONT
    c.bold = True
    field(fp, "PAGE", "1")
    for r in fp.runs[-3:]:
        r.font.size = Pt(7.8)
        r.font.color.rgb = rgb(D.NAVY)
        r.font.name = D.FONT
        r.bold = True
    d2 = fp.add_run(" / ")
    d2.font.size = Pt(7.8)
    d2.font.color.rgb = rgb(D.NAVY)
    d2.bold = True
    field(fp, "NUMPAGES", "1")
    for r in fp.runs[-3:]:
        r.font.size = Pt(7.8)
        r.font.color.rgb = rgb(D.NAVY)
        r.font.name = D.FONT
        r.bold = True
    pPr = fp._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr")
    top = OxmlElement("w:top")
    top.set(qn("w:val"), "single")
    top.set(qn("w:sz"), "6")
    top.set(qn("w:space"), "4")
    top.set(qn("w:color"), D.GREY_LN)
    bd.append(top)
    insert_ordered(pPr, bd)


def _new_sec(d, landscape, meta):  # noqa: C901
    sec = d.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        sec.page_width = pt(D.LPAGE_W)
        sec.page_height = pt(D.LPAGE_H)
        sec.left_margin = pt(D.LM_LEFT)
        sec.right_margin = pt(D.LM_RIGHT)
        sec.top_margin = pt(D.LM_TOP)
        sec.bottom_margin = pt(D.LM_BOT)
    else:
        sec.page_width = pt(D.PAGE_W)
        sec.page_height = pt(D.PAGE_H)
        sec.left_margin = pt(D.M_LEFT)
        sec.right_margin = pt(D.M_RIGHT)
        sec.top_margin = pt(D.M_TOP)
        sec.bottom_margin = pt(D.M_BOT)
    sec.header_distance = pt(28)
    sec.footer_distance = pt(24)
    _header_footer(d, meta, sec)


def _cover(d, meta):
    """Couverture : image pleine page commune au PDF et au DOCX."""
    sec = d.sections[0]
    sec.different_first_page_header_footer = False
    sec.top_margin = pt(0)
    sec.bottom_margin = pt(0)
    sec.left_margin = pt(0)
    sec.right_margin = pt(0)
    sec.header_distance = pt(0)
    sec.footer_distance = pt(0)
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    p.add_run().add_picture(meta["cover_img"], width=pt(D.PAGE_W), height=pt(D.PAGE_H))
