# -*- coding: utf-8 -*-
"""Rendu PDF (reportlab) — moteur de référence de la mise en page.

Le DOCX est produit à partir du même modèle de blocs, avec les mêmes
dimensions, couleurs, polices et corps de texte : les deux fichiers sont
visuellement identiques par construction.

Le sommaire est calculé en deux passes : la première passe mesure la page de
chaque titre (marqueurs de page), la seconde insère les numéros. La hauteur du
sommaire est identique entre les deux passes (seule la colonne de droite
change), la pagination est donc stable.
"""
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, HRFlowable,
                                Image, KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.pdfgen import canvas as pdfcanvas

import design as D

HERE = os.path.dirname(os.path.abspath(__file__))

for _name, _fn in {"Carlito": D.FONT_REG, "Carlito-Bold": D.FONT_BOLD,
                   "Carlito-It": D.FONT_IT, "Carlito-BoldIt": D.FONT_BI}.items():
    pdfmetrics.registerFont(TTFont(_name, os.path.join(HERE, _fn)))
registerFontFamily("Carlito", normal="Carlito", bold="Carlito-Bold",
                   italic="Carlito-It", boldItalic="Carlito-BoldIt")


def C(h):
    return colors.HexColor("#" + h.lstrip("#"))


# ----------------------------------------------------------------------
# Styles
# ----------------------------------------------------------------------
def _styles():
    s = {}
    s["p"] = ParagraphStyle("p", fontName="Carlito", fontSize=D.SZ_BODY,
                            leading=D.SZ_BODY * 1.50, textColor=C(D.GREY_TXT),
                            alignment=TA_JUSTIFY, spaceAfter=5.4)
    s["p_left"] = ParagraphStyle("p_left", parent=s["p"], alignment=TA_LEFT)
    s["lead"] = ParagraphStyle("lead", parent=s["p"], fontSize=10.7, leading=16.4,
                               textColor=C(D.NAVY_L), spaceAfter=9)
    s["bul"] = ParagraphStyle("bul", parent=s["p"], leftIndent=14, bulletIndent=2,
                              spaceAfter=2.6, bulletFontName="Carlito",
                              bulletFontSize=8.2, bulletColor=C(D.TEAL))
    s["h1"] = ParagraphStyle("h1", fontName="Carlito-Bold", fontSize=D.SZ_H1,
                             leading=D.SZ_H1 * 1.18, textColor=C(D.NAVY),
                             spaceAfter=0, spaceBefore=0)
    s["h2"] = ParagraphStyle("h2", fontName="Carlito-Bold", fontSize=D.SZ_H2,
                             leading=D.SZ_H2 * 1.24, textColor=C(D.NAVY),
                             spaceBefore=13, spaceAfter=5)
    s["h3"] = ParagraphStyle("h3", fontName="Carlito-Bold", fontSize=D.SZ_H3,
                             leading=D.SZ_H3 * 1.30, textColor=C(D.TEAL),
                             spaceBefore=10, spaceAfter=3.6)
    s["cell"] = ParagraphStyle("cell", fontName="Carlito", fontSize=7.7, leading=10.0,
                               textColor=C(D.GREY_TXT), alignment=TA_LEFT)
    s["cap"] = ParagraphStyle("cap", fontName="Carlito-Bold", fontSize=8.0, leading=10.8,
                              textColor=C(D.NAVY), spaceBefore=4, spaceAfter=3.4)
    s["note"] = ParagraphStyle("note", fontName="Carlito-It", fontSize=7.1, leading=9.6,
                               textColor=C(D.GREY_MID), spaceBefore=3, spaceAfter=9)
    s["toc1"] = ParagraphStyle("toc1", fontName="Carlito-Bold", fontSize=9.4, leading=17.5,
                               textColor=C(D.NAVY))
    s["toc1r"] = ParagraphStyle("toc1r", parent=s["toc1"], alignment=TA_RIGHT)
    s["toc2"] = ParagraphStyle("toc2", fontName="Carlito", fontSize=8.7, leading=13.4,
                               textColor=C(D.GREY_TXT), leftIndent=17)
    s["toc2r"] = ParagraphStyle("toc2r", parent=s["toc2"], alignment=TA_RIGHT)
    return s


ST = _styles()


# ----------------------------------------------------------------------
# Marqueur de page (pour le sommaire)
# ----------------------------------------------------------------------
class _SoftBreak(PageBreak):
    """Saut de page qui ne crée pas de page blanche en fin de flux."""

    def isSatisfied(self):
        self._n = getattr(self, "_n", 0) + 1
        return 0 if self._n % 2 else 1


class PageMarker(Flowable):
    """Enregistre le numéro de page d'un titre sans dépendre du dessin différé."""

    def __init__(self, key, store):
        Flowable.__init__(self)
        self.key = key
        self.store = store

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        self.store[self.key] = self.canv.getPageNumber()

    def drawOn(self, canv, x, y, _sW=0):
        self.store[self.key] = canv.getPageNumber()


class Anchor(Flowable):
    """Signet PDF (navigation dans le document)."""

    def __init__(self, title, level=0, key=""):
        Flowable.__init__(self)
        self.title = title
        self.level = level
        self.key = key

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)


# ----------------------------------------------------------------------
# Canvas : en-tête, pied de page, foliotage
# ----------------------------------------------------------------------
class DocCanvas(pdfcanvas.Canvas):
    def __init__(self, *a, **kw):
        self._meta = kw.pop("meta", {})
        pdfcanvas.Canvas.__init__(self, *a, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for i, state in enumerate(self._saved):
            self.__dict__.update(state)
            self._decorate(i + 1, total)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def _decorate(self, page, total):
        if page == 1:
            return
        meta = self._meta
        W, H = self._pagesize
        land = W > H
        ml = D.LM_LEFT if land else D.M_LEFT
        mr = D.LM_RIGHT if land else D.M_RIGHT
        mt = D.LM_TOP if land else D.M_TOP
        mb = D.LM_BOT if land else D.M_BOT
        self.saveState()
        self.setStrokeColor(C(D.GREY_LN))
        self.setLineWidth(0.6)
        self.setFont("Carlito", 7.3)
        self.setFillColor(C(D.GREY_MID))
        self.drawString(ml, H - mt + 27, meta.get("header_left", ""))
        self.drawRightString(W - mr, H - mt + 27, meta.get("header_right", ""))
        self.line(ml, H - mt + 20, W - mr, H - mt + 20)

        self.line(ml, mb - 15, W - mr, mb - 15)
        self.setFont("Carlito", 7.0)
        self.setFillColor(C(D.GREY_MID))
        self.drawString(ml, mb - 26, meta.get("footer_left", ""))
        self.drawCentredString(W / 2, mb - 26, meta.get("footer_center", ""))
        self.setFont("Carlito-Bold", 7.8)
        self.setFillColor(C(D.NAVY))
        self.drawRightString(W - mr, mb - 26, "Page %d / %d" % (page, total))
        self.restoreState()


# ----------------------------------------------------------------------
# Couverture
# ----------------------------------------------------------------------
class CoverArt(Flowable):
    """Couverture : image pleine page commune au PDF et au DOCX."""

    def __init__(self, meta):
        Flowable.__init__(self)
        self.meta = meta
        self._img = None

    def wrap(self, aw, ah):
        return (D.PAGE_W, D.PAGE_H)

    def draw(self):
        m = self.meta
        c = self.canv
        p = m.get("cover_img")
        if not p:
            c.setFillColor(C(D.NAVY_D))
            c.rect(0, 0, D.PAGE_W, D.PAGE_H, stroke=0, fill=1)
            return
        c.drawImage(p, 0, 0, width=D.PAGE_W, height=D.PAGE_H,
                    preserveAspectRatio=False, mask=None)


class _SoftBreak(PageBreak):
    """Saut de page qui ne crée pas de page blanche en fin de flux."""

    def isSatisfied(self):
        self._n = getattr(self, "_n", 0) + 1
        return 0 if self._n % 2 else 1


class PageMarker(Flowable):
    """Enregistre le numéro de page d'un titre sans dépendre du dessin différé."""

    def __init__(self, key, store):
        Flowable.__init__(self)
        self.key = key
        self.store = store

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        self.store[self.key] = self.canv.getPageNumber()

    def drawOn(self, canv, x, y, _sW=0):
        self.store[self.key] = canv.getPageNumber()


class Anchor(Flowable):
    """Signet PDF (navigation dans le document)."""

    def __init__(self, title, level=0, key=""):
        Flowable.__init__(self)
        self.title = title
        self.level = level
        self.key = key

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)


# ----------------------------------------------------------------------
# Canvas : en-tête, pied de page, foliotage
# ----------------------------------------------------------------------
class DocCanvas(pdfcanvas.Canvas):
    def __init__(self, *a, **kw):
        self._meta = kw.pop("meta", {})
        pdfcanvas.Canvas.__init__(self, *a, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for i, state in enumerate(self._saved):
            self.__dict__.update(state)
            self._decorate(i + 1, total)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def _decorate(self, page, total):
        if page == 1:
            return
        meta = self._meta
        W, H = self._pagesize
        land = W > H
        ml = D.LM_LEFT if land else D.M_LEFT
        mr = D.LM_RIGHT if land else D.M_RIGHT
        mt = D.LM_TOP if land else D.M_TOP
        mb = D.LM_BOT if land else D.M_BOT
        self.saveState()
        self.setStrokeColor(C(D.GREY_LN))
        self.setLineWidth(0.6)
        self.setFont("Carlito", 7.3)
        self.setFillColor(C(D.GREY_MID))
        self.drawString(ml, H - mt + 27, meta.get("header_left", ""))
        self.drawRightString(W - mr, H - mt + 27, meta.get("header_right", ""))
        self.line(ml, H - mt + 20, W - mr, H - mt + 20)

        self.line(ml, mb - 15, W - mr, mb - 15)
        self.setFont("Carlito", 7.0)
        self.setFillColor(C(D.GREY_MID))
        self.drawString(ml, mb - 26, meta.get("footer_left", ""))
        self.drawCentredString(W / 2, mb - 26, meta.get("footer_center", ""))
        self.setFont("Carlito-Bold", 7.8)
        self.setFillColor(C(D.NAVY))
        self.drawRightString(W - mr, mb - 26, "Page %d / %d" % (page, total))
        self.restoreState()


# ----------------------------------------------------------------------
# Couverture
# ----------------------------------------------------------------------
class CoverArt(Flowable):
    def __init__(self, meta):
        Flowable.__init__(self)
        self.meta = meta

    def wrap(self, aw, ah):
        return (D.PAGE_W, D.PAGE_H)

    def draw(self):
        m = self.meta
        c = self.canv
        W, H = D.PAGE_W, D.PAGE_H
        c.setFillColor(C(D.NAVY_D))
        c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setFillColor(C(D.TEAL))
        c.rect(0, H - 13, W, 13, stroke=0, fill=1)

        # motif discret (arcs concentriques)
        c.saveState()
        c.setFillColor(colors.HexColor("#0F4763"))
        c.circle(W + 40, H - 250, 190, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#11526F"))
        c.circle(W + 40, H - 250, 140, stroke=0, fill=1)
        c.restoreState()

        c.setFillColor(colors.HexColor("#7FC6CB"))
        c.setFont("Carlito-Bold", 8.8)
        c.drawString(D.M_LEFT, H - 92, m["cover_kicker"].upper())

        c.setStrokeColor(C(D.GOLD))
        c.setLineWidth(1.5)
        c.line(D.M_LEFT, H - 152, D.M_LEFT + 88, H - 152)

        c.setFillColor(colors.white)
        c.setFont("Carlito-Bold", 11.4)
        y = H - 176
        for line in m["cover_org"]:
            c.drawString(D.M_LEFT, y, line)
            y -= 15.5

        c.setFont("Carlito-Bold", 26.5)
        c.setFillColor(colors.white)
        c.drawString(D.M_LEFT, H - 268, "PLAN DE SUIVI-ÉVALUATION")
        c.setFillColor(C("#7FD1D6"))
        c.drawString(D.M_LEFT, H - 300, "2027 – 2028")

        c.setFillColor(colors.HexColor("#CBDDE6"))
        c.setFont("Carlito", 10.4)
        y = H - 336
        for line in m["cover_sub"]:
            c.drawString(D.M_LEFT, y, line)
            y -= 15

        # carte projet
        bx, by, bw, bh = D.M_LEFT, 236, D.CONTENT_W, 178
        c.setFillColor(colors.HexColor("#12455F"))
        c.roundRect(bx, by, bw, bh, 5, stroke=0, fill=1)
        c.setFillColor(C("#7FD1D6"))
        c.setFont("Carlito-Bold", 7.8)
        c.drawString(bx + 18, by + bh - 22, "PROJET DE RÉFÉRENCE")
        c.setFillColor(colors.white)
        c.setFont("Carlito-Bold", 10.0)
        yy = by + bh - 42
        for line in m["cover_projet"]:
            c.drawString(bx + 18, yy, line)
            yy -= 14.4
        c.setFillColor(colors.HexColor("#A6C1D2"))
        c.setFont("Carlito", 7.9)
        yy -= 6
        for line in m["cover_source"]:
            c.drawString(bx + 18, yy, line)
            yy -= 11.6

        c.setFillColor(colors.HexColor("#8FB3C7"))
        c.setFont("Carlito", 8.3)
        c.drawString(D.M_LEFT, 156, m["cover_periode"])
        c.drawString(D.M_LEFT, 141, m["cover_version"])
        c.setStrokeColor(colors.HexColor("#2C6079"))
        c.setLineWidth(0.8)
        c.line(D.M_LEFT, 124, D.M_LEFT + D.CONTENT_W, 124)
        c.setFillColor(colors.HexColor("#6E93A8"))
        c.setFont("Carlito-It", 7.2)
        yy = 106
        for line in m["cover_footer"]:
            c.drawString(D.M_LEFT, yy, line)
            yy -= 10.6


# ----------------------------------------------------------------------
# Sommaire
# ----------------------------------------------------------------------
def _toc_flowables(doc, pages):
    out = []
    for i, (lvl, num, title) in enumerate(doc.toc_entries):
        if lvl == 1:
            st, str_ = ST["toc1"], ST["toc1r"]
        elif lvl == 2:
            st, str_ = ST["toc2"], ST["toc2r"]
        else:
            continue
        pg = pages.get(i, "")
        if lvl == 1:
            label = title
            out.append([Paragraph(num or "", st), Paragraph(label, st),
                        Paragraph(str(pg), str_)])
        else:
            out.append([Paragraph("", ST["toc2"]),
                        Paragraph(("%s&nbsp;&nbsp;%s" % (num, title)) if num else title, st),
                        Paragraph(str(pg), str_)])
    if not out:
        out = [["", "", ""]]
    t = Table(out, colWidths=[36, D.CONTENT_W - 36 - 34, 34])
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.6),
    ]
    for i, (lvl, num, title) in enumerate([e for e in doc.toc_entries if e[0] in (1, 2)]):
        if lvl == 1:
            cmds.append(("LINEBELOW", (0, i), (-1, i), 0.4, C("#DCE5EB")))
    t.setStyle(TableStyle(cmds))
    return t


# ----------------------------------------------------------------------
# Rendu des blocs
# ----------------------------------------------------------------------
def _h1(b, store, idx):
    num, title = b["num"], b["text"]
    kick = ("SECTION %s" % num) if num else "SECTION"
    els = [
        Anchor(title, level=0, key="h1_%d" % idx),
        Paragraph('<font color="#%s">%s</font>' % (D.GOLD, kick),
                  ParagraphStyle("kick", fontName="Carlito-Bold", fontSize=7.8, leading=10)),
        Spacer(1, 1.5),
        Paragraph(_inl(title), ST["h1"]),
        Spacer(1, 4),
        HRFlowable(width="100%", thickness=1.5, color=C(D.NAVY),
                   spaceBefore=1, spaceAfter=9),
    ]
    return [PageMarker(idx, store), KeepTogether(els)]


def _h2(b, store, idx):
    num, title = b["num"], b["text"]
    txt = ('<font color="#%s">%s</font>&nbsp;&nbsp;%s' % (D.TEAL, num, title)) if num else title
    return [PageMarker(idx, store), KeepTogether([Paragraph(_inl(txt), ST["h2"])])]


def _inl(t):
    return t


def _bullets(b):
    out = []
    style = b.get("style", "dot")
    for i, it in enumerate(b["items"], 1):
        bullet = ("%d." % i) if style == "num" else "\u25aa"
        st = ST["bul"]
        if b.get("size"):
            st = ParagraphStyle("bz", parent=st, fontSize=b["size"], leading=b["size"] * 1.50)
        out.append(Paragraph(_inl(it), st, bulletText=bullet))
    out.append(Spacer(1, 4))
    return out


def _callout(b):
    tones = {"teal": (D.TEAL_L, D.TEAL), "gold": ("FBF4E7", D.GOLD),
             "grey": (D.GREY_BG, D.GREY_MID), "red": ("FCEEEE", D.RED),
             "navy": ("E9EFF4", D.NAVY)}
    bg, fg = tones[b["tone"]]
    inner = [
        Paragraph('<font color="#%s">%s</font>' % (fg, b["title"]),
                  ParagraphStyle("ct", fontName="Carlito-Bold", fontSize=8.5,
                                 leading=11, spaceAfter=2.8)),
        Paragraph(_inl(b["text"]), ParagraphStyle(
            "cb", fontName="Carlito", fontSize=8.35, leading=11.7,
            textColor=C(D.GREY_TXT), alignment=TA_JUSTIFY)),
    ]
    t = Table([[inner]], colWidths=[D.CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), C(bg)),
        ("LINEBEFORE", (0, 0), (0, -1), 2.4, C(fg)),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Spacer(1, 3), KeepTogether([t]), Spacer(1, 9)]


def _split(b):
    """Découpe un tableau paysage en blocs de n lignes (en-tête répété)."""
    n = b.get("split_after")
    if not n:
        return [b]
    rows = b["rows"]
    head = [r for r in rows[:b["head_rows"]]]
    body = rows[b["head_rows"]:]
    total = len(body)
    chunks = []
    i = 0
    idx = 0
    while i < total:
        part = body[i:i + n]
        cap = b.get("caption") if idx == 0 else b.get("caption", "").split(" — ")[0] + " (suite)"
        note = b.get("note") if idx == 0 else None
        nb = dict(b)
        nb["rows"] = head + part
        nb["caption"] = cap
        nb["note"] = note
        nb["head_rows"] = len(head)
        chunks.append(nb)
        i += n
        idx += 1
    return chunks


class _NoSplitRow(Table):
    """Table dont une ligne ne peut pas être coupée entre deux pages."""

    def __init__(self, data, **kw):
        Table.__init__(self, data, **kw)
        self._sty = TableStyle([])

    def _splitRows(self, availHeight, *a, **kw):
        if self._nrows <= 2:
            return []
        res = []
        cur = []
        h = 0
        for i in range(self._nrows):
            rh = self._rowHeights[i]
            if cur and h + rh > availHeight:
                res.append(cur)
                cur, h = [], 0
            cur.append(i)
            h += rh
        if cur:
            res.append(cur)
        if len(res) <= 1:
            return []
        out = []
        for idxs in res:
            part = _NoSplitRow([self._cellvalues[i] for i in idxs],
                               colWidths=self._colWidths,
                               rowHeights=[self._rowHeights[i] for i in idxs])
            part.setStyle(self._sty)
            out.append(part)
        return out


def _table(b, width=None):
    out = []
    if b.get("caption"):
        out.append(Paragraph(b["caption"], ST["cap"]))
    total_w = width or D.CONTENT_W
    widths = [total_w * w for w in b["widths"]]
    fs = b.get("size") or 7.7
    cs = ParagraphStyle("c", parent=ST["cell"], fontSize=fs, leading=fs * 1.32)
    csc = ParagraphStyle("cc", parent=cs, alignment=TA_CENTER)
    chs = ParagraphStyle("ch", parent=cs, fontName="Carlito-Bold", textColor=C("#FFFFFF"))
    chsc = ParagraphStyle("chc", parent=chs, alignment=TA_CENTER)
    align = b.get("align") or ["l"] * len(b["cols"])
    data = []
    for ri, row in enumerate(b["rows"]):
        head = ri < b["head_rows"]
        line = []
        for ci, cell in enumerate(row):
            a = align[ci] if ci < len(align) else "l"
            st = (chsc if a == "c" else chs) if head else (csc if a == "c" else cs)
            line.append(Paragraph("" if cell is None else str(cell), st))
        data.append(line)

    t = Table(data, colWidths=widths,
              repeatRows=(b["head_rows"] if b.get("repeat_head") else 0),
              splitByRow=1)
    pad = 2.7 if fs < 6.7 else (3.1 if fs < 7.4 else 3.4)
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE" if b.get("vcenter") else "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.0),
        ("TOPPADDING", (0, 0), (-1, -1), pad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad + 0.2),
        ("GRID", (0, 0), (-1, -1), 0.35, C(D.GREY_LN)),
    ]
    for ri in range(b["head_rows"]):
        cmds.append(("BACKGROUND", (0, ri), (-1, ri), C(D.NAVY)))
    if b.get("zebra"):
        for ri in range(b["head_rows"], len(data)):
            if (ri - b["head_rows"]) % 2 == 1:
                cmds.append(("BACKGROUND", (0, ri), (-1, ri), C(D.GREY_BG)))
    for gr in b.get("group_rows", []):
        cmds.append(("BACKGROUND", (0, gr), (-1, gr), C(D.GREY_BG2)))
    t.setStyle(TableStyle(cmds))
    out.append(t)
    if b.get("note"):
        out.append(Paragraph(b["note"], ST["note"]))
    else:
        out.append(Spacer(1, 9))
    if b.get("tag") == "keep":
        return [KeepTogether(out)]
    return out


def _figure(b):
    from PIL import Image as PILImage
    iw, ih = PILImage.open(b["path"]).size
    w = D.CONTENT_W * b.get("width_frac", 1.0)
    h = w * ih / iw
    max_h = D.PAGE_H - D.M_TOP - D.M_BOT - 78
    if h > max_h:
        h, w = max_h, max_h * iw / ih
    out = [Spacer(1, 5), Image(b["path"], width=w, height=h)]
    if b.get("caption"):
        out.append(Paragraph(b["caption"], ST["cap"]))
    out.append(Paragraph(b["note"], ST["note"]) if b.get("note") else Spacer(1, 9))
    return out


def _kpis(b):
    items = b["items"]
    n = len(items)
    gap = 7
    cw = (D.CONTENT_W - gap * (n - 1)) / n
    cells = []
    for val, lab in items:
        cells.append(Table(
            [[Paragraph(val, ParagraphStyle("kv", fontName="Carlito-Bold", fontSize=16.5,
                                            leading=19, textColor=C(D.NAVY), alignment=TA_CENTER))],
             [Paragraph(lab, ParagraphStyle("kl", fontName="Carlito", fontSize=7.0,
                                            leading=9.0, textColor=C(D.GREY_MID),
                                            alignment=TA_CENTER))]],
            colWidths=[cw], style=TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), C(D.GREY_BG)),
                ("LINEABOVE", (0, 0), (-1, 0), 2.0, C(D.TEAL)),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (0, 0), 7),
                ("BOTTOMPADDING", (0, 0), (0, 0), 0),
                ("TOPPADDING", (0, 1), (0, 1), 1),
                ("BOTTOMPADDING", (0, 1), (0, 1), 7),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ])))
    row = Table([[c for c in cells]], colWidths=[cw + gap] * (n - 1) + [cw])
    row.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0),
                            ("RIGHTPADDING", (0, 0), (-1, -1), gap),
                            ("TOPPADDING", (0, 0), (-1, -1), 0),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                            ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return [Spacer(1, 5), KeepTogether([row]), Spacer(1, 11)]


def _make_story(doc, store, pages):
    story = [NextPageTemplate("body"), CoverArt(doc.meta), PageBreak()]

    # ---- page de sommaire
    story.append(Anchor("Sommaire", level=0, key="toc"))
    story.append(Paragraph("Sommaire", ST["h1"]))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C(D.NAVY),
                            spaceBefore=1, spaceAfter=12))
    story.append(_toc_flowables(doc, pages))
    story.append(PageBreak())

    TEXTY = {"p", "h2", "h3", "bullets", "callout", "kpis"}
    land_start = set()
    for i, b in enumerate(doc.blocks):
        if b["kind"] != "h1":
            continue
        nxt = doc.blocks[i + 1] if i + 1 < len(doc.blocks) else None
        if nxt is not None and nxt["kind"] == "table" and nxt.get("landscape"):
            land_start.add(i)

    cur_tpl = ["body"]
    toc_key = {}
    j = 0
    for idx, b in enumerate(doc.blocks):
        if b["kind"] in ("h1", "h2"):
            toc_key[idx] = j
            j += 1

    for idx, b in enumerate(doc.blocks):
        k = b["kind"]
        if k == "h1":
            target = "land" if idx in land_start else "body"
            if target != cur_tpl[0]:
                story.append(NextPageTemplate(target))
                story.append(_SoftBreak())
                cur_tpl[0] = target
            elif b.get("page_break", True) and idx > 0:
                story.append(_SoftBreak())
            story.extend(_h1(b, store, toc_key[idx]))
        elif k == "h2":
            story.extend(_h2(b, store, toc_key[idx]))
        elif k == "h3":
            story.append(Paragraph(_inl(b["text"]), ST["h3"]))
        elif k == "p":
            st = ST["p"] if b.get("justify", True) else ST["p_left"]
            if b.get("size"):
                st = ParagraphStyle("pz", parent=st, fontSize=b["size"],
                                    leading=b["size"] * 1.50)
            if b.get("color"):
                st = ParagraphStyle("pc", parent=st, textColor=C(b["color"]))
            story.append(Paragraph(_inl(b["text"]), st))
        elif k == "lead":
            story.append(Paragraph(_inl(b["text"]), ST["lead"]))
        elif k == "bullets":
            story.extend(_bullets(b))
        elif k == "spacer":
            story.append(Spacer(1, b["h"]))
        elif k == "pagebreak":
            story.append(PageBreak())
        elif k == "callout":
            story.extend(_callout(b))
        elif k == "table":
            if b.get("landscape"):
                nxt = doc.blocks[idx + 1] if idx + 1 < len(doc.blocks) else None
                more = nxt is not None and (
                    (nxt["kind"] == "table" and nxt.get("landscape")) or
                    (nxt["kind"] == "h1" and nxt.get("page_break", True)))
                chunks = _split(b)
                for n, ch in enumerate(chunks):
                    if cur_tpl[0] != "land":
                        story.append(NextPageTemplate("land"))
                        story.append(_SoftBreak())
                        cur_tpl[0] = "land"
                    story.extend(_table(ch, width=D.LCONTENT_W))
                if not more:
                    story.append(NextPageTemplate("body"))
                    story.append(_SoftBreak())
                    cur_tpl[0] = "body"
            else:
                story.extend(_table(b))
        elif k == "figure":
            story.extend(_figure(b))
        elif k == "kpis":
            story.extend(_kpis(b))
        elif k == "figure_page":
            story.append(PageBreak())
            story.extend(_figure(b))
    return story


def build_pdf(doc, path, meta_extra=None):
    meta = dict(doc.meta)
    if meta_extra:
        meta.update(meta_extra)

    def _doc_obj():
        d = BaseDocTemplate(
            path, pagesize=(D.PAGE_W, D.PAGE_H),
            leftMargin=D.M_LEFT, rightMargin=D.M_RIGHT,
            topMargin=D.M_TOP, bottomMargin=D.M_BOT,
            title=meta.get("title", ""), author=meta.get("author", ""),
            subject=meta.get("subject", ""), creator="Arena Agent",
        )
        frame = Frame(D.M_LEFT, D.M_BOT, D.CONTENT_W,
                      D.PAGE_H - D.M_TOP - D.M_BOT, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        cover = Frame(0, 0, D.PAGE_W, D.PAGE_H, id="cover",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        lframe = Frame(D.LM_LEFT, D.LM_BOT, D.LCONTENT_W, D.LPAGE_H - D.LM_TOP - D.LM_BOT,
                       id="lbody", leftPadding=0, rightPadding=0, topPadding=0,
                       bottomPadding=0)

        def _land(c, doc_):
            c.setPageSize((D.LPAGE_W, D.LPAGE_H))

        def _port(c, doc_):
            c.setPageSize((D.PAGE_W, D.PAGE_H))

        d.addPageTemplates([
            PageTemplate(id="cover", frames=[cover]),
            PageTemplate(id="body", frames=[frame], onPage=_port),
            PageTemplate(id="land", frames=[lframe], onPage=_land),
        ])
        return d

    # ---- passe 1 : mesure
    store = {}
    story = _make_story(doc, store, {})
    _doc_obj().build(story, canvasmaker=lambda *a, **k: DocCanvas(*a, meta=meta, **k))

    # ---- passe 2 : sommaire renseigné
    store2 = {}
    story2 = _make_story(doc, store2, store)
    _doc_obj().build(story2, canvasmaker=lambda *a, **k: DocCanvas(*a, meta=meta, **k))

    pages = {}
    for i, (lvl, num, title) in enumerate(doc.toc_entries):
        if i in store2:
            pages[i] = store2[i]
    return pages
