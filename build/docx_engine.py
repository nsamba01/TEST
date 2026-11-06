"""Moteur de rendu DOCX — à partir du modèle de blocs commun."""
import os
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_BREAK
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import charte as C

SYMBOLS = "✓▲●■▶★◆⚠→"
SYM_FONT_DOCX = "Segoe UI Symbol"


# ------------------------------------------------------------------ helpers XML
def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn("w:" + k), v)
    return e


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    tcPr.append(_el("w:shd", val="clear", color="auto", fill=hexcolor))


def cell_margins(table, top=0.03, left=0.14, bottom=0.03, right=0.14):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement("w:" + side)
        e.set(qn("w:w"), str(int(val * 567)))
        e.set(qn("w:type"), "dxa")
        mar.append(e)
    tblPr.append(mar)


def table_borders(table, color=C.BORDER, sz=6, inside=True):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")
    sides = ["top", "left", "bottom", "right"] + (["insideH", "insideV"] if inside else [])
    for s in sides:
        e = OxmlElement("w:" + s)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), str(sz))
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), color)
        borders.append(e)
    tblPr.append(borders)


def no_borders(table):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for s in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        e = OxmlElement("w:" + s)
        e.set(qn("w:val"), "none")
        e.set(qn("w:sz"), "0")
        borders.append(e)
    tblPr.append(borders)


def cell_border(cell, side, color, sz=18):
    tcPr = cell._tc.get_or_add_tcPr()
    b = tcPr.find(qn("w:tcBorders"))
    if b is None:
        b = OxmlElement("w:tcBorders")
        tcPr.append(b)
    e = OxmlElement("w:" + side)
    e.set(qn("w:val"), "single")
    e.set(qn("w:sz"), str(sz))
    e.set(qn("w:space"), "0")
    e.set(qn("w:color"), color)
    b.append(e)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(_el("w:tblHeader", val="true"))


def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(_el("w:cantSplit", val="true"))


def fixed_layout(table):
    tblPr = table._tbl.tblPr
    tblPr.append(_el("w:tblLayout", type="fixed"))


def vcenter(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(_el("w:vAlign", val="center"))


def add_field(paragraph, instr, placeholder="1"):
    r = paragraph.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    r._r.append(fld)
    r2 = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = instr
    r2._r.append(it)
    r3 = paragraph.add_run()
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    r3._r.append(sep)
    r4 = paragraph.add_run(placeholder)
    r5 = paragraph.add_run()
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    r5._r.append(end)
    for rr in (r, r2, r3, r4, r5):
        rr.font.name = C.FONT_DOCX
        rr.font.size = Pt(C.SZ_FOOTER)
        rr.font.color.rgb = RGBColor.from_string(C.GREY)
    return paragraph


def para_bottom_rule(paragraph, color=C.PRIMARY, sz=8):
    pPr = paragraph._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    e = OxmlElement("w:bottom")
    e.set(qn("w:val"), "single")
    e.set(qn("w:sz"), str(sz))
    e.set(qn("w:space"), "1")
    e.set(qn("w:color"), color)
    pbdr.append(e)
    pPr.append(pbdr)


def set_run_font(run, name, size=None, color=None, bold=None, italic=None):
    run.font.name = name
    rPr = run._element.get_or_add_rPr()
    rf = rPr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rPr.append(rf)
    for a in ("ascii", "hAnsi", "cs", "eastAsia"):
        rf.set(qn("w:" + a), name)
    if size is not None:
        run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic


# ------------------------------------------------------------------ inline
def add_inline(paragraph, text, size=C.SZ_BODY, color=C.TEXT, bold=False,
               italic=False, base_font=C.FONT_DOCX):
    """Gère **gras** et les puces symboliques (police dédiée)."""
    tokens = re.split(r"(\*\*.+?\*\*|__.+?__)", text)
    for tok in tokens:
        if not tok:
            continue
        b, i = bold, italic
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            tok, b = tok[2:-2], True
        elif tok.startswith("__") and tok.endswith("__") and len(tok) > 4:
            tok, i = tok[2:-2], True
        # découpe autour des symboles
        buf = ""
        for ch in tok:
            if ch in SYMBOLS:
                if buf:
                    r = paragraph.add_run(buf)
                    set_run_font(r, base_font, size, color, b, i)
                    buf = ""
                r = paragraph.add_run(ch)
                set_run_font(r, SYM_FONT_DOCX, size, color, b, False)
            else:
                buf += ch
        if buf:
            r = paragraph.add_run(buf)
            set_run_font(r, base_font, size, color, b, i)
    return paragraph


# ------------------------------------------------------------------ document
class DocxBuilder:
    def __init__(self, title, header_left, footer_left):
        self.doc = Document()
        self.header_left = header_left
        self.footer_left = footer_left
        self.title = title
        self._base_styles()
        self.section = self.doc.sections[0]
        self._setup_page(self.section, landscape=False)
        self._header_footer(self.section, landscape=False)

    # ---- styles
    def _base_styles(self):
        st = self.doc.styles["Normal"]
        st.font.name = C.FONT_DOCX
        st.font.size = Pt(C.SZ_BODY)
        st.font.color.rgb = RGBColor.from_string(C.TEXT)
        st.paragraph_format.line_spacing = C.LINE_SPACING
        st.paragraph_format.space_after = Pt(C.SPACE_AFTER)
        rpr = st.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts")
            rpr.append(rf)
        for a in ("ascii", "hAnsi", "cs", "eastAsia"):
            rf.set(qn("w:" + a), C.FONT_DOCX)

        for name, size, color, font, bold in (
                ("Heading 1", C.SZ_H1, C.PRIMARY, C.FONT_DOCX_L, False),
                ("Heading 2", C.SZ_H2, C.PRIMARY, C.FONT_DOCX, True),
                ("Heading 3", C.SZ_H3, C.SECONDARY, C.FONT_DOCX, True)):
            s = self.doc.styles[name]
            s.font.name = font
            s.font.size = Pt(size)
            s.font.color.rgb = RGBColor.from_string(color)
            s.font.bold = bold
            s.font.italic = False
            s.paragraph_format.space_before = Pt(14 if name == "Heading 1" else 10)
            s.paragraph_format.space_after = Pt(8 if name == "Heading 1" else 5)
            s.paragraph_format.keep_with_next = True
            s.paragraph_format.line_spacing = 1.0
            r = s.element.get_or_add_rPr()
            f = r.find(qn("w:rFonts"))
            if f is None:
                f = OxmlElement("w:rFonts")
                r.append(f)
            for a in ("ascii", "hAnsi", "cs", "eastAsia"):
                f.set(qn("w:" + a), font)
            f.set(qn("w:asciiTheme"), "minorHAnsi")
            try:
                del f.attrib[qn("w:asciiTheme")]
            except KeyError:
                pass

    def _setup_page(self, section, landscape):
        section.orientation = WD_ORIENT.LANDSCAPE if landscape else WD_ORIENT.PORTRAIT
        w, h = (C.PAGE_H_CM, C.PAGE_W_CM) if landscape else (C.PAGE_W_CM, C.PAGE_H_CM)
        section.page_width = Cm(w)
        section.page_height = Cm(h)
        for attr in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
            setattr(section, attr, Cm(C.MARGIN_CM))
        section.header_distance = Cm(0.85)
        section.footer_distance = Cm(0.80)

    def _header_footer(self, section, landscape):
        width_cm = (C.PAGE_H_CM if landscape else C.PAGE_W_CM) - 2 * C.MARGIN_CM
        for part, kind in ((section.header, "header"), (section.footer, "footer")):
            part.is_linked_to_previous = False
            for p in list(part.paragraphs):
                p._p.getparent().remove(p._p)
            if not part.paragraphs:
                part.add_paragraph()

        # ---- en-tête
        hp = section.header.paragraphs[0]
        hp.paragraph_format.space_after = Pt(2)
        hp.paragraph_format.tab_stops.add_tab_stop(Cm(width_cm), WD_TAB_ALIGNMENT.RIGHT)
        add_inline(hp, self.header_left, size=8, color=C.PRIMARY, bold=True)
        r = hp.add_run("\t")
        set_run_font(r, C.FONT_DOCX, 8, C.PRIMARY)
        add_inline(hp, C.PROJECT_SHORT, size=8, color=C.GREY)
        para_bottom_rule(hp, C.PRIMARY, 8)

        # ---- pied de page
        fp = section.footer.paragraphs[0]
        fp.paragraph_format.space_before = Pt(2)
        fp.paragraph_format.tab_stops.add_tab_stop(Cm(width_cm), WD_TAB_ALIGNMENT.RIGHT)
        add_inline(fp, self.footer_left, size=C.SZ_FOOTER, color=C.GREY)
        r = fp.add_run("\t")
        set_run_font(r, C.FONT_DOCX, C.SZ_FOOTER, C.GREY)
        r = fp.add_run("Page ")
        set_run_font(r, C.FONT_DOCX, C.SZ_FOOTER, C.GREY)
        add_field(fp, " PAGE ")
        r = fp.add_run(" sur ")
        set_run_font(r, C.FONT_DOCX, C.SZ_FOOTER, C.GREY)
        add_field(fp, " NUMPAGES ")

    def new_section(self, landscape):
        s = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._setup_page(s, landscape)
        self._header_footer(s, landscape)
        self.section = s
        return s

    # ---- primitives
    def p(self, text="", size=C.SZ_BODY, color=C.TEXT, bold=False, italic=False,
          align="left", before=0, after=C.SPACE_AFTER, spacing=C.LINE_SPACING,
          font=C.FONT_DOCX, indent=0, keep=False, style=None):
        par = self.doc.add_paragraph(style=style)
        pf = par.paragraph_format
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.line_spacing = spacing
        pf.keep_with_next = keep
        if indent:
            pf.left_indent = Cm(indent)
        pf.alignment = {"left": WD_ALIGN_PARAGRAPH.LEFT,
                        "center": WD_ALIGN_PARAGRAPH.CENTER,
                        "right": WD_ALIGN_PARAGRAPH.RIGHT,
                        "just": WD_ALIGN_PARAGRAPH.JUSTIFY}[align]
        if text:
            add_inline(par, text, size=size, color=color, bold=bold, italic=italic,
                       base_font=font)
        return par

    def heading(self, text, level=2):
        par = self.doc.add_paragraph(style=f"Heading {level}")
        if level == 2:
            # filet fin sous les titres de niveau 2
            pass
        add_inline(par, text, size={1: C.SZ_H1, 2: C.SZ_H2, 3: C.SZ_H3}[level],
                   color={1: C.PRIMARY, 2: C.PRIMARY, 3: C.SECONDARY}[level],
                   bold=(level != 1),
                   base_font=C.FONT_DOCX_L if level == 1 else C.FONT_DOCX)
        return par

    def bullets(self, items, size=C.SZ_BODY, color=C.TEXT):
        for it in items:
            par = self.doc.add_paragraph()
            pf = par.paragraph_format
            pf.left_indent = Cm(0.55)
            pf.first_line_indent = Cm(-0.35)
            pf.space_after = Pt(3)
            pf.line_spacing = C.LINE_SPACING
            r = par.add_run("●")
            set_run_font(r, SYM_FONT_DOCX, 7, C.PRIMARY)
            r = par.add_run("   ")
            set_run_font(r, C.FONT_DOCX, size, color)
            add_inline(par, it, size=size, color=color)

    def numbered(self, items, size=C.SZ_BODY):
        for i, it in enumerate(items, 1):
            par = self.doc.add_paragraph()
            pf = par.paragraph_format
            pf.left_indent = Cm(0.7)
            pf.first_line_indent = Cm(-0.55)
            pf.space_after = Pt(3)
            pf.line_spacing = C.LINE_SPACING
            r = par.add_run(f"{i}.")
            set_run_font(r, C.FONT_DOCX, size, C.PRIMARY, bold=True)
            r = par.add_run("   ")
            set_run_font(r, C.FONT_DOCX, size, C.TEXT)
            add_inline(par, it, size=size, color=C.TEXT)

    def table(self, header, rows, widths, caption=None, font=C.SZ_TABLE,
              header_fill=C.PRIMARY, first_col_bold=False, align_center=None,
              band=True, caption_num=None, total_row=False, zebra=C.TABLE_BG, colors=None):
        if caption:
            self.caption(caption, caption_num)
        ncol = len(widths)
        t = self.doc.add_table(rows=1, cols=ncol)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        fixed_layout(t)
        table_borders(t, C.BORDER, 6)
        cell_margins(t, 0.035, 0.13, 0.035, 0.13)

        hdr = t.rows[0]
        cant_split(hdr)
        repeat_header(hdr)
        for i, h in enumerate(header):
            cell = hdr.cells[i]
            cell.width = Cm(widths[i])
            shade(cell, header_fill)
            vcenter(cell)
            par = cell.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.space_before = Pt(0)
            par.paragraph_format.line_spacing = 1.0
            add_inline(par, h, size=font, color=C.WHITE, bold=True)

        keep = len(rows) <= 8
        for ri, row in enumerate(rows):
            tr = t.add_row()
            cant_split(tr)
            is_total = total_row and ri == len(rows) - 1
            for ci, val in enumerate(row):
                cell = tr.cells[ci]
                cell.width = Cm(widths[ci])
                vcenter(cell)
                if colors and (ri, ci) in colors:
                    shade(cell, colors[(ri, ci)])
                elif is_total:
                    shade(cell, "E4EEF8")
                elif band and ri % 2 == 1:
                    shade(cell, zebra)
                par = cell.paragraphs[0]
                par.paragraph_format.space_after = Pt(0)
                par.paragraph_format.space_before = Pt(0)
                par.paragraph_format.line_spacing = 1.0
                if align_center and ci in align_center:
                    par.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                bold = (first_col_bold and ci == 0) or is_total
                add_inline(par, str(val), size=font, color=C.TEXT, bold=bold)
                if keep and ri < len(rows) - 1:
                    par.paragraph_format.keep_with_next = True
        return t

    def caption(self, text, num=None):
        par = self.doc.add_paragraph()
        pf = par.paragraph_format
        pf.space_before = Pt(9 if num else 4)
        pf.space_after = Pt(3)
        pf.keep_with_next = True
        pf.line_spacing = 1.0
        if num:
            r = par.add_run(f"Tableau {num}. ")
            set_run_font(r, C.FONT_DOCX, C.SZ_CAPTION + 0.5, C.PRIMARY, bold=True)
        r = par.add_run(text)
        set_run_font(r, C.FONT_DOCX, C.SZ_CAPTION + 0.5, C.GREY, bold=bool(num), italic=not num)
        return par

    def callout(self, title, text, icon=None, fill=C.LIGHT_BLUE, accent=C.PRIMARY):
        t = self.doc.add_table(rows=1, cols=1)
        t.autofit = False
        fixed_layout(t)
        no_borders(t)
        cell_margins(t, 0.10, 0.22, 0.10, 0.22)
        cell = t.rows[0].cells[0]
        cell.width = Cm(C.CONTENT_W_CM if not self._is_landscape() else C.LAND_CONTENT_W_CM)
        shade(cell, fill)
        cell_border(cell, "left", accent, 24)
        par = cell.paragraphs[0]
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.line_spacing = C.LINE_SPACING
        if title:
            if icon:
                r = par.add_run(icon + "  ")
                set_run_font(r, SYM_FONT_DOCX, 9.5, accent, bold=True)
            r = par.add_run(title)
            set_run_font(r, C.FONT_DOCX, 9.5, accent, bold=True)
            par2 = cell.add_paragraph()
            par2.paragraph_format.space_after = Pt(0)
            par2.paragraph_format.line_spacing = C.LINE_SPACING
            add_inline(par2, text, size=9.5, color=C.TEXT)
        else:
            add_inline(par, text, size=9.5, color=C.TEXT)
        self.spacer(4)

    def spacer(self, pt=6):
        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.line_spacing = 1.0
        r = par.add_run("")
        r.font.size = Pt(pt)

    def image(self, path, width_cm, caption=None):
        par = self.doc.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        par.paragraph_format.space_before = Pt(6)
        par.paragraph_format.space_after = Pt(2)
        par.paragraph_format.keep_with_next = bool(caption)
        run = par.add_run()
        run.add_picture(path, width=Cm(width_cm))
        if caption:
            self.caption(caption)

    def page_break(self):
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def _is_landscape(self):
        return self.section.page_width > self.section.page_height

    def section_page(self, num, title, subtitle=""):
        self.page_break()
        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(150)
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.line_spacing = 1.0
        r = par.add_run(num)
        set_run_font(r, C.FONT_DOCX_L, 76, "D3E4F5", bold=False)

        par = self.doc.add_paragraph(style="Heading 1")
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.space_after = Pt(6)
        par.paragraph_format.line_spacing = 1.0
        par.paragraph_format.keep_with_next = True
        r = par.add_run(title)
        set_run_font(r, C.FONT_DOCX_L, 26, C.PRIMARY, bold=False)

        par = self.doc.add_paragraph()
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.space_after = Pt(10)
        par.paragraph_format.line_spacing = 1.0
        para_bottom_rule(par, C.ACCENT, 18)

        if subtitle:
            par = self.doc.add_paragraph()
            par.paragraph_format.space_before = Pt(6)
            par.paragraph_format.line_spacing = C.LINE_SPACING
            add_inline(par, subtitle, size=11, color=C.SECONDARY, italic=True)
        self.page_break()

    def toc(self):
        par = self.doc.add_paragraph()
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), r'TOC \o "1-2" \h \z \u')
        run = OxmlElement("w:r")
        t = OxmlElement("w:t")
        t.text = "Table des matières — champ à mettre à jour (F9) pour afficher la pagination."
        run.append(t)
        fld.append(run)
        par._p.append(fld)

    def save(self, path):
        # mise à jour automatique des champs à l'ouverture
        settings = self.doc.settings.element
        upd = OxmlElement("w:updateFields")
        upd.set(qn("w:val"), "true")
        settings.append(upd)
        self.doc.core_properties.title = self.title
        self.doc.core_properties.author = "Consortium SANRU-ICHESS-FONLIV-FDSS"
        self.doc.core_properties.subject = "Plan de Suivi-Évaluation 2027-2028 — PMNS Kwilu"
        self.doc.core_properties.language = "fr-FR"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.doc.save(path)
