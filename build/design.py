"""Design system + content model for the SE/CP deliverables 2027-2028.

Single source of truth: every visual rule (colour, type, spacing) is declared
here and consumed by BOTH renderers (DOCX via python-docx, PDF via reportlab)
so the two outputs are visually identical by construction.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# PALETTE  — bleu institutionnel + turquoise + gris
# --------------------------------------------------------------------------
NAVY      = "0B3C5D"   # couleur principale
NAVY_D    = "07293F"   # navy profond (couverture)
NAVY_L    = "1B5E88"   # navy clair (accents)
TEAL      = "17868C"   # couleur secondaire (turquoise)
TEAL_L    = "E4F1F2"   # turquoise très clair (fonds)
TEAL_M    = "B7DCDE"
GOLD      = "B7873C"   # accent sobre (filets, chiffres clés)
GREY_TXT  = "3A4A56"   # corps de texte
GREY_MID  = "6B7B87"   # texte secondaire
GREY_LN   = "C9D3DA"   # filets / bordures
GREY_BG   = "F2F5F7"   # lignes alternées
GREY_BG2  = "E6ECF0"
WHITE     = "FFFFFF"
RED       = "9B2226"   # « À préciser »
AMBER     = "8A6A1F"
GREEN     = "2A6F4F"

# statut / traçabilité
C_SRC = TEAL      # information issue de Tech-4
C_REC = GOLD      # recommandation à valider
C_NA  = RED       # information manquante

# --------------------------------------------------------------------------
# TYPOGRAPHIE  (Carlito == métrique Calibri ; mêmes fichiers dans les 2 rendus)
# --------------------------------------------------------------------------
FONT = "Carlito"
FONT_REG  = "Carlito-Regular.ttf"
FONT_BOLD = "Carlito-Bold.ttf"
FONT_IT   = "Carlito-Italic.ttf"
FONT_BI   = "Carlito-BoldItalic.ttf"

SZ_BODY   = 10.0
SZ_SMALL  = 8.5
SZ_TINY   = 7.6
SZ_H1     = 18.0
SZ_H2     = 13.0
SZ_H3     = 11.0
SZ_COVER  = 30.0
SZ_KPI    = 20.0

# --------------------------------------------------------------------------
# PAGE / GRILLE
# --------------------------------------------------------------------------
PAGE_W, PAGE_H = 595.276, 841.890          # A4 en points
M_TOP, M_BOT, M_LEFT, M_RIGHT = 78, 62, 62, 56
CONTENT_W = PAGE_W - M_LEFT - M_RIGHT

# --------------------------------------------------------------------------
# TITRES DU DOCUMENT
# --------------------------------------------------------------------------
PROJET_COURT = "PMNS-NAC Kwilu"
PROJET_LONG = ("Projet Multisectoriel de Nutrition et de Santé – Volet Nutrition à "
               "Assise Communautaire (PMNS-NAC), province du Kwilu, RDC")
CONSORTIUM = "Consortium SANRU – ICHESS – FONLIV – FDSS"
BAILLEUR_MAITRE = "UG-PDSS (Unité de Gestion du Programme de Développement du Système de Santé)"
TITRE_PLAN = "PLAN DE SUIVI-ÉVALUATION 2027–2028"
TITRE_CADRE = "CADRE DE PERFORMANCE 2027–2028"
PERIODE = "Période de mise en œuvre : 1er janvier 2027 – 31 décembre 2028"
SOURCE_DOC = "Document source : Tech-4 — « Description de l’approche, de la méthodologie et du programme de travail », DP N° ZR-DRC-MSP-235334-CS-QCBS"

# Mentions normalisées (traçabilité documentaire)
NA = "À préciser"
NA_LONG = "Non renseigné dans le document source"
SRC = "Tech-4"
REC = "Recommandation à valider"


# --------------------------------------------------------------------------
# METHODES UTILITAIRES DE MISE EN FORME
# --------------------------------------------------------------------------
def hx(c):
    return "#" + c if not c.startswith("#") else c


def tint(c, f):
    """Éclaircit une couleur hex vers le blanc (f=0 -> c, f=1 -> blanc)."""
    c = c.lstrip("#")
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    r = int(r + (255 - r) * f); g = int(g + (255 - g) * f); b = int(b + (255 - b) * f)
    return "%02X%02X%02X" % (r, g, b)


def shade(c, f):
    """Assombrit une couleur hex (f=0 -> c, f=1 -> noir)."""
    c = c.lstrip("#")
    r, g, b = int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)
    r = int(r * (1 - f)); g = int(g * (1 - f)); b = int(b * (1 - f))
    return "%02X%02X%02X" % (r, g, b)


# --------------------------------------------------------------------------
def _norm_rows(cols, rows):
    """Garantit que rows[0] est la ligne d'en-tête, identique à `cols`."""
    import re as _re

    def _n(x):
        return _re.sub(r"<[^>]+>", "", str(x)).replace("&nbsp;", " ").strip().lower()

    rows = [list(r) for r in rows]
    if rows and [_n(c) for c in rows[0]] == [_n(c) for c in cols]:
        rows = rows[1:]
    return [[str(c) for c in cols]] + rows


# CONTENU — modèle de blocs commun aux deux rendus
# --------------------------------------------------------------------------
class Doc:
    """Un document = une suite de blocs typés."""

    def __init__(self, meta):
        self.meta = meta          # dict : titre, sous_titre, page_de_garde...
        self.blocks = []
        self.toc_entries = []     # (niveau, numero, titre, ancre)

    # -- helpers -----------------------------------------------------------
    def add(self, kind, **kw):
        kw["kind"] = kind
        self.blocks.append(kw)
        return kw

    def h1(self, num, text, page_break=True):
        self.toc_entries.append((1, num, text))
        return self.add("h1", num=num, text=text, page_break=page_break)

    def h2(self, num, text, page_break=False):
        self.toc_entries.append((2, num, text))
        return self.add("h2", num=num, text=text, page_break=page_break)

    def h3(self, text, page_break=False):
        self.toc_entries.append((3, "", text))
        return self.add("h3", text=text, page_break=page_break)

    def p(self, text, size=None, space=5, justify=True, color=None, keep=False):
        return self.add("p", text=text, size=size, space=space, justify=justify,
                        color=color, keep=keep)

    def lead(self, text):
        return self.add("lead", text=text)

    def bullets(self, items, style="dot", size=None, space=5):
        return self.add("bullets", items=items, style=style, size=size, space=space)

    def numbered(self, items, size=None):
        return self.add("bullets", items=items, style="num", size=size, space=5)

    def table(self, cols, widths, rows, head_rows=1, size=None, caption=None,
              note=None, zebra=True, align=None, vcenter=False, group_rows=(),
              repeat_head=True, tag=None, landscape=False, split_after=None,
              rows_keep=False):
        rows = _norm_rows(cols, rows)
        return self.add("table", cols=cols, widths=widths, rows=rows,
                        head_rows=head_rows, size=size, caption=caption, note=note,
                        zebra=zebra, align=align, vcenter=vcenter,
                        group_rows=list(group_rows), repeat_head=repeat_head, tag=tag,
                        landscape=landscape, split_after=split_after,
                        rows_keep=rows_keep)

    def callout(self, title, text, tone="teal", icon=None):
        return self.add("callout", title=title, text=text, tone=tone, icon=icon)

    def figure(self, path, width_frac=1.0, caption=None, note=None):
        return self.add("figure", path=path, width_frac=width_frac,
                        caption=caption, note=note)

    def gantt(self, years, phases, caption=None, note=None):
        return self.add("gantt", years=years, phases=phases, caption=caption, note=note)

    def kpis(self, items):
        return self.add("kpis", items=items)

    def spacer(self, h=6):
        return self.add("spacer", h=h)

    def pagebreak(self):
        return self.add("pagebreak")

    def toc(self):
        return self.add("toc")

# --- Gabarit paysage (tableaux matriciels larges)
LPAGE_W, LPAGE_H = PAGE_H, PAGE_W
LM_TOP, LM_BOT, LM_LEFT, LM_RIGHT = 64, 56, 56, 56
LCONTENT_W = LPAGE_W - LM_LEFT - LM_RIGHT
