"""Moteur de rendu PDF — mêmes blocs, même charte, même pagination visuelle."""
import os
import re

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, Image,
                                NextPageTemplate, Flowable, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen import canvas as rl_canvas

import charte as C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "fonts")

SYMBOLS = "✓▲●■▶★◆⚠→"

_FONTS_DONE = False


def register_fonts():
    global _FONTS_DONE
    if _FONTS_DONE:
        return
    pdfmetrics.registerFont(TTFont("Carlito", os.path.join(FONTS, "Carlito-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Carlito-Bold", os.path.join(FONTS, "Carlito-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Carlito-Italic", os.path.join(FONTS, "Carlito-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("Carlito-BoldItalic", os.path.join(FONTS, "Carlito-BoldItalic.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSym", os.path.join(FONTS, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSym-Bold", os.path.join(FONTS, "DejaVuSans-Bold.ttf")))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("Carlito", normal="Carlito", bold="Carlito-Bold",
                       italic="Carlito-Italic", boldItalic="Carlito-BoldItalic")
    _FONTS_DONE = True


def hexc(h):
    return colors.HexColor("#" + h)


def esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def inline(text, size=None, color=None, bold=False, italic=False):
    """Convertit **gras** / __italique__ et isole les symboles dans une police dédiée."""
    def sym(ch):
        return '<font face="DejaVuSym">%s</font>' % ch

    def wrap_symbols(s):
        out = []
        for ch in s:
            if ch == "\n":
                out.append("<br/>")
            else:
                out.append(sym(ch) if ch in SYMBOLS else esc(ch))
        return "".join(out)

    tokens = re.split(r"(\*\*.+?\*\*|__.+?__)", str(text))
    parts = []
    for tok in tokens:
        if not tok:
            continue
        b, i = bold, italic
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            tok, b = tok[2:-2], True
        elif tok.startswith("__") and tok.endswith("__") and len(tok) > 4:
            tok, i = tok[2:-2], True
        s = wrap_symbols(tok)
        if b:
            s = "<b>%s</b>" % s
        if i:
            s = "<i>%s</i>" % s
        parts.append(s)
    body = "".join(parts)
    attrs = ""
    if size:
        attrs += ' size="%s"' % size
    if color:
        attrs += ' color="#%s"' % color
    return '<font%s>%s</font>' % (attrs, body) if attrs else body


# ------------------------------------------------------------------ styles
def styles():
    register_fonts()
    s = {}
    s["body"] = ParagraphStyle("body", fontName="Carlito", fontSize=C.SZ_BODY,
                               leading=C.SZ_BODY * 1.404, textColor=hexc(C.TEXT),
                               spaceAfter=C.SPACE_AFTER, alignment=TA_JUSTIFY,
                               splitLongWords=1)
    s["body_l"] = ParagraphStyle("body_l", parent=s["body"], alignment=TA_LEFT)
    s["lead"] = ParagraphStyle("lead", parent=s["body"], fontSize=11.5,
                               leading=11.5 * 1.404, textColor=hexc(C.PRIMARY_DARK),
                               spaceAfter=8)
    s["h1"] = ParagraphStyle("h1", fontName="Carlito", fontSize=C.SZ_H1,
                             leading=C.SZ_H1 * 1.16, textColor=hexc(C.PRIMARY),
                             spaceBefore=4, spaceAfter=10, alignment=TA_LEFT)
    s["h2"] = ParagraphStyle("h2", fontName="Carlito-Bold", fontSize=C.SZ_H2,
                             leading=C.SZ_H2 * 1.22, textColor=hexc(C.PRIMARY),
                             spaceBefore=13, spaceAfter=6)
    s["h3"] = ParagraphStyle("h3", fontName="Carlito-Bold", fontSize=C.SZ_H3,
                             leading=C.SZ_H3 * 1.25, textColor=hexc(C.SECONDARY),
                             spaceBefore=10, spaceAfter=4)
    s["caption"] = ParagraphStyle("caption", fontName="Carlito-Bold", fontSize=C.SZ_CAPTION + 0.5,
                                  leading=(C.SZ_CAPTION + 0.5) * 1.25, textColor=hexc(C.PRIMARY),
                                  spaceBefore=9, spaceAfter=3)
    s["note"] = ParagraphStyle("note", fontName="Carlito-Italic", fontSize=C.SZ_CAPTION + 0.5,
                               leading=(C.SZ_CAPTION + 0.5) * 1.3, textColor=hexc(C.GREY),
                               spaceBefore=3, spaceAfter=7)
    s["cell"] = ParagraphStyle("cell", fontName="Carlito", fontSize=C.SZ_TABLE,
                               leading=C.SZ_TABLE * 1.24, textColor=hexc(C.TEXT))
    s["cellc"] = ParagraphStyle("cellc", parent=s["cell"], alignment=TA_CENTER)
    s["head"] = ParagraphStyle("head", fontName="Carlito-Bold", fontSize=C.SZ_TABLE,
                               leading=C.SZ_TABLE * 1.24, textColor=hexc(C.WHITE))
    s["cellb"] = ParagraphStyle("cellb", parent=s["cell"], fontName="Carlito-Bold")
    return s


# ------------------------------------------------------------------ flowables
class HRule(Flowable):
    def __init__(self, width, thickness=1.0, color=C.PRIMARY, space_before=2, space_after=6):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.color = color
        self.sb = space_before
        self.sa = space_after

    def wrap(self, aw, ah):
        self.aw = aw
        return aw, self.thickness + self.sb + self.sa

    def draw(self):
        self.canv.setStrokeColor(hexc(self.color))
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.sa, self.aw, self.sa)


class SectionMark(Flowable):
    """Numéro de section en très grand format + titre."""
    def __init__(self, num, title, sub, width):
        Flowable.__init__(self)
        self.num, self.title, self.sub, self.width = num, title, sub, width

    def wrap(self, aw, ah):
        self.h = 300
        return aw, self.h

    def draw(self):
        c = self.canv
        c.setFillColor(hexc("D3E4F5"))
        c.setFont("Carlito", 76)
        c.drawString(0, self.h - 92, self.num)
        c.setFillColor(hexc(C.PRIMARY))
        c.setFont("Carlito", 26)
        c.drawString(0, self.h - 146, self.title)
        c.setStrokeColor(hexc(C.ACCENT))
        c.setLineWidth(2.2)
        c.line(0, self.h - 162, self.width, self.h - 162)
        if self.sub:
            c.setFillColor(hexc(C.SECONDARY))
            c.setFont("Carlito-Italic", 11)
            t = c.beginText(0, self.h - 186)
            c.drawString(0, self.h - 186, self.sub)


class TOCEntryMark(Flowable):
    def __init__(self, level, text):
        Flowable.__init__(self)
        self.level, self.text = level, text
        self.width = 0
        self.height = 0

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        pass


# ------------------------------------------------------------------ canvas
class NumberedCanvas(rl_canvas.Canvas):
    def __init__(self, *a, **kw):
        self._footer_left = kw.pop("footer_left", C.DOC_FOOTER)
        self._header_left = kw.pop("header_left", "")
        rl_canvas.Canvas.__init__(self, *a, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self._draw_furniture(total)
            rl_canvas.Canvas.showPage(self)
        rl_canvas.Canvas.save(self)

    def _draw_furniture(self, total):
        if self._footer_left == "__NONE__" or self._pageNumber == 1:
            return
        W, H = self._pagesize
        m = C.MARGIN_CM * cm
        # en-tête
        self.setStrokeColor(hexc(C.PRIMARY))
        self.setLineWidth(C.HEADER_RULE_PT)
        self.line(m, H - m + 8, W - m, H - m + 8)
        self.setFont("Carlito-Bold", 8)
        self.setFillColor(hexc(C.PRIMARY))
        self.drawString(m, H - m + 13, self._header_left)
        self.setFont("Carlito", 8)
        self.setFillColor(hexc(C.GREY))
        self.drawRightString(W - m, H - m + 13, C.PROJECT_SHORT)
        # pied de page
        self.setLineWidth(0.4)
        self.setStrokeColor(hexc(C.BORDER))
        self.line(m, m - 6, W - m, m - 6)
        self.setFont("Carlito", C.SZ_FOOTER)
        self.setFillColor(hexc(C.GREY))
        self.drawString(m, m - 15, self._footer_left)
        self.drawRightString(W - m, m - 15, "Page %d sur %d" % (self._pageNumber, total))


# ------------------------------------------------------------------ builder
class PdfBuilder:
    def __init__(self, title, header_left, footer_left, path):
        register_fonts()
        self.title = title
        self.header_left = header_left
        self.footer_left = footer_left
        self.path = path
        self.st = styles()
        self.story = []
        self.doc = BaseDocTemplate(
            path, pagesize=A4,
            leftMargin=C.MARGIN_CM * cm, rightMargin=C.MARGIN_CM * cm,
            topMargin=C.MARGIN_CM * cm + 6, bottomMargin=C.MARGIN_CM * cm + 4,
            title=title, author="Consortium SANRU-ICHESS-FONLIV-FDSS",
            subject="Plan de Suivi-Évaluation 2027-2028 — PMNS Kwilu")
        pw, ph = A4
        lw, lh = landscape(A4)
        frame_p = Frame(C.MARGIN_CM * cm, C.MARGIN_CM * cm + 4,
                        pw - 2 * C.MARGIN_CM * cm, ph - 2 * C.MARGIN_CM * cm - 10,
                        id="p", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_l = Frame(C.MARGIN_CM * cm, C.MARGIN_CM * cm + 4,
                        lw - 2 * C.MARGIN_CM * cm, lh - 2 * C.MARGIN_CM * cm - 10,
                        id="l", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.doc.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_p], pagesize=A4,
                         onPage=lambda c, d: None),
            PageTemplate(id="portrait", frames=[frame_p], pagesize=A4),
            PageTemplate(id="landscape", frames=[frame_l], pagesize=(lw, lh)),
        ])
        self.landscape = False

    # ---- internal
    def _p(self, text, style="body", **kw):
        return Paragraph(inline(text, **kw), self.st[style])

    def add(self, f):
        self.story.append(f)

    # ---- public block API
    def cover(self, d):
        self.story.append(NextPageTemplate("portrait"))
        W = C.CONTENT_W_CM * cm
        self.add(Spacer(1, 2.2 * cm))
        self.add(Table([[""]], colWidths=[W], rowHeights=[0.10 * cm],
                       style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), hexc(C.SECONDARY))])))
        self.add(Spacer(1, 0.55 * cm))
        self.add(Paragraph(inline(d["kicker"], size=9, color=C.SECONDARY),
                           ParagraphStyle("k", fontName="Carlito-Bold", fontSize=9,
                                          leading=13, textColor=hexc(C.SECONDARY))))
        self.add(Spacer(1, 0.35 * cm))
        self.add(Paragraph(inline(d["title"], size=25, color=C.PRIMARY),
                           ParagraphStyle("ct", fontName="Carlito", fontSize=25, leading=30,
                                          textColor=hexc(C.PRIMARY))))
        self.add(Spacer(1, 0.30 * cm))
        self.add(HRule(W, 2.4, C.ACCENT, 0, 10))
        self.add(Spacer(1, 0.20 * cm))
        self.add(Paragraph(inline(d["subtitle"], size=19, color=C.SECONDARY),
                           ParagraphStyle("cs", fontName="Carlito", fontSize=19, leading=24,
                                          textColor=hexc(C.SECONDARY))))
        self.add(Spacer(1, 0.35 * cm))
        self.add(Paragraph(inline(d["consortium"], size=11.5, color=C.TEXT),
                           ParagraphStyle("cc", fontName="Carlito", fontSize=11.5, leading=16,
                                          textColor=hexc(C.TEXT))))
        self.add(Spacer(1, 1.0 * cm))
        rows = [[Paragraph(inline(k, size=9, color=C.GREY, bold=True), self.st["cell"]),
                 Paragraph(inline(v, size=9), self.st["cell"])] for k, v in d["info"]]
        t = Table(rows, colWidths=[4.6 * cm, W - 4.6 * cm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), hexc(C.LIGHT_BLUE)),
            ("LINEBELOW", (0, 0), (-1, -1), 0.4, hexc(C.BORDER)),
            ("BOX", (0, 0), (-1, -1), 0.5, hexc(C.BORDER)),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        self.add(t)
        self.add(Spacer(1, 0.9 * cm))
        self.add(Paragraph(inline(d["footer"], size=8, color=C.GREY, italic=True),
                           ParagraphStyle("cf", fontName="Carlito-Italic", fontSize=8,
                                          leading=11, textColor=hexc(C.GREY))))
        self.add(PageBreak())

    def toc(self):
        par = Paragraph("Table des matières", ParagraphStyle(
            "toch", fontName="Carlito", fontSize=C.SZ_H1, leading=C.SZ_H1 * 1.16,
            textColor=hexc(C.PRIMARY), spaceAfter=10))
        self.add(par)
        self.add(HRule(C.CONTENT_W_CM * cm, 1.2, C.ACCENT, 0, 12))
        toc = TableOfContents()
        toc.levelStyles = [
            ParagraphStyle("toc0", fontName="Carlito-Bold", fontSize=11.5, leading=19,
                           textColor=hexc(C.PRIMARY), leftIndent=0, spaceBefore=7,
                           spaceAfter=1),
            ParagraphStyle("toc1", fontName="Carlito", fontSize=9.5, leading=14.5,
                           textColor=hexc(C.TEXT), leftIndent=16, spaceBefore=0),
        ]
        toc.dotsMinLevel = 0
        self.add(toc)
        self.add(PageBreak())

    def section(self, num, title, sub=""):
        self.add(Spacer(1, 0.8 * cm))
        self.add(SectionMark(num, title, sub, C.CONTENT_W_CM * cm))
        self._notify(title, 0)

    def h2(self, text):
        self.add(Paragraph(inline(text), self.st["h2"]))
        self._notify(text, 1)

    def h3(self, text):
        self.add(Paragraph(inline(text), self.st["h3"]))

    def p(self, text, style="body"):
        self.add(Paragraph(inline(text), self.st[style]))

    def bullets(self, items):
        for it in items:
            p = Paragraph(
                '<font face="DejaVuSym" color="#%s" size="6.5">●</font>&nbsp;&nbsp;%s'
                % (C.PRIMARY, inline(it, color=C.TEXT)),
                ParagraphStyle("bul", parent=self.st["body"], leftIndent=10,
                               bulletIndent=0, spaceAfter=3, firstLineIndent=0))
            self.add(p)

    def numbered(self, items):
        for i, it in enumerate(items, 1):
            p = Paragraph(
                '<font color="#%s"><b>%d.</b></font>&nbsp;&nbsp;%s'
                % (C.PRIMARY, i, inline(it, color=C.TEXT)),
                ParagraphStyle("num", parent=self.st["body"], leftIndent=14, spaceAfter=3))
            self.add(p)

    def table(self, header, rows, widths, caption=None, num=None, font=C.SZ_TABLE,
              first_bold=False, center=None, total=False, band=True,
              header_fill=C.PRIMARY, colors=None):
        keep = len(rows) <= 8
        cap_flow = None
        if caption:
            from reportlab.platypus import Paragraph as _P
            if num:
                cap_flow = _P('<font color="#%s">Tableau %s.</font> %s'
                              % (C.PRIMARY, num, esc(caption)), self.st["caption"])
            else:
                cap_flow = _P('<i>%s</i>' % esc(caption), self.st["note"])
        cell_style = ParagraphStyle("c%s" % font, fontName="Carlito", fontSize=font,
                                    leading=font * 1.24, textColor=hexc(C.TEXT))
        cell_c = ParagraphStyle("cc%s" % font, parent=cell_style, alignment=TA_CENTER)
        head_style = ParagraphStyle("h%s" % font, fontName="Carlito-Bold", fontSize=font,
                                    leading=font * 1.24, textColor=hexc(C.WHITE))
        data = [[Paragraph(inline(h), head_style) for h in header]]
        for r in rows:
            line = []
            for ci, v in enumerate(r):
                stl = cell_c if (center and ci in center) else cell_style
                if first_bold and ci == 0:
                    stl = ParagraphStyle("b%s" % ci, parent=stl, fontName="Carlito-Bold")
                line.append(Paragraph(inline(v), stl))
            data.append(line)
        colw = [w * cm for w in widths]
        t = Table(data, colWidths=colw, repeatRows=1, hAlign="CENTER")
        cmds = [
            ("BACKGROUND", (0, 0), (-1, 0), hexc(header_fill)),
            ("GRID", (0, 0), (-1, -1), 0.45, hexc(C.BORDER)),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3.6), ("RIGHTPADDING", (0, 0), (-1, -1), 3.6),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ]
        if band:
            for i in range(1, len(data)):
                if i % 2 == 0:
                    cmds.append(("BACKGROUND", (0, i), (-1, i), hexc(C.TABLE_BG)))
        if total:
            cmds.append(("BACKGROUND", (0, len(data) - 1), (-1, len(data) - 1), hexc("E4EEF8")))
        if colors:
            for (r, c), hx in colors.items():
                cmds.append(("BACKGROUND", (c, r + 1), (c, r + 1), hexc(hx)))
        t.setStyle(TableStyle(cmds))
        if keep:
            flows = ([cap_flow] if cap_flow is not None else []) + [t, Spacer(1, 7)]
            self.add(KeepTogether(flows))
        else:
            if cap_flow is not None:
                self.add(cap_flow)
            self.add(t)
            self.add(Spacer(1, 7))

    def caption(self, text, num=None):
        if num:
            self.add(Paragraph('<font color="#%s">Tableau %s.</font> %s'
                               % (C.PRIMARY, num, esc(text)), self.st["caption"]))
        else:
            self.add(Paragraph('<i>%s</i>' % esc(text), self.st["note"]))

    def callout(self, title, text, icon=None, fill=C.LIGHT_BLUE, accent=C.PRIMARY):
        W = (C.LAND_CONTENT_W_CM if self.landscape else C.CONTENT_W_CM) * cm
        inner = []
        if title:
            pre = ('<font face="DejaVuSym" color="#%s">%s</font>&nbsp;&nbsp;' % (accent, icon)) if icon else ""
            inner.append(Paragraph(pre + '<font color="#%s"><b>%s</b></font>' % (accent, esc(title)),
                                   ParagraphStyle("cot", fontName="Carlito", fontSize=9.5,
                                                  leading=12.6)))
        inner.append(Paragraph(inline(text, size=9.5, color=C.TEXT),
                               ParagraphStyle("cob", fontName="Carlito", fontSize=9.5,
                                              leading=12.9, textColor=hexc(C.TEXT))))
        t = Table([[inner]], colWidths=[W])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), hexc(fill)),
            ("LINEBEFORE", (0, 0), (0, -1), 2.4, hexc(accent)),
            ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        self.add(t)
        self.add(Spacer(1, 5))

    def image(self, path, width_cm, caption=None, h_cm=None):
        from PIL import Image as PILImage
        iw, ih = PILImage.open(path).size
        w = width_cm * cm
        h = w * ih / iw
        img = Image(path, width=w, height=h)
        img.hAlign = "CENTER"
        self.add(Spacer(1, 4))
        self.add(img)
        if caption:
            self.add(Paragraph('<i>%s</i>' % esc(caption),
                               ParagraphStyle("imgcap", fontName="Carlito-Italic",
                                              fontSize=C.SZ_CAPTION + 0.5,
                                              leading=(C.SZ_CAPTION + 0.5) * 1.3,
                                              textColor=hexc(C.GREY), spaceBefore=3, spaceAfter=8)))
        else:
            self.add(Spacer(1, 8))

    def note(self, text):
        self.add(Paragraph('<i>%s</i>' % inline(text, color=C.GREY), self.st["note"]))

    def _switch_template(self, name):
        if self.story and isinstance(self.story[-1], PageBreak):
            self.story.pop()
        self.story.append(NextPageTemplate(name))
        self.story.append(PageBreak())

    def land_start(self):
        self._switch_template("landscape")
        self.landscape = True

    def land_end(self):
        self._switch_template("portrait")
        self.landscape = False

    def page_break(self):
        self.add(PageBreak())

    def _notify(self, text, level):
        self.add(TOCEntryMark(level, text))

    def save(self):
        self.doc.multiBuild(self.story,
                            canvasmaker=lambda *a, **k: NumberedCanvas(
                                *a, footer_left=self.footer_left,
                                header_left=self.header_left, **k))


def _after_flowable(self, flowable):
    """Hook TOC : reportlab appelle doc.afterFlowable."""
    if isinstance(flowable, TOCEntryMark):
        self.notify("TOCEntry", (flowable.level, flowable.text, self.page))


BaseDocTemplate.afterFlowable = _after_flowable
