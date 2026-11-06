"""Charte graphique commune aux rendus DOCX et PDF."""

# ---------------------------------------------------------------- palette
PRIMARY      = "0072CE"   # Bleu santé
PRIMARY_DARK = "005AA3"
SECONDARY    = "2E8B57"   # Vert
ACCENT       = "F4A460"   # Orange doux (alertes)
TABLE_BG     = "F5F5F5"   # Fond des tableaux (banding)
LIGHT_BLUE   = "EAF3FB"   # Encadrés / notes (bleu très pâle)
TEXT         = "333333"   # Gris foncé — jamais de noir pur
GREY         = "6B7280"
BORDER       = "D6E3F0"
WHITE        = "FFFFFF"

GRID_LIGHT   = "E3EAF2"

# ---------------------------------------------------------------- typographie
FONT_DOCX    = "Calibri"
FONT_DOCX_L  = "Calibri Light"
FONT_PDF     = "Carlito"       # métriquement compatible avec Calibri
FONT_PDF_B   = "Carlito-Bold"

SZ_COVER_TITLE = 26
SZ_H1          = 22
SZ_H2          = 15
SZ_H3          = 12
SZ_BODY        = 11
SZ_SMALL       = 9.5
SZ_TABLE       = 9
SZ_TABLE_WIDE  = 8
SZ_CAPTION     = 8.5
SZ_FOOTER      = 8

LINE_SPACING   = 1.15
SPACE_AFTER    = 6

# ---------------------------------------------------------------- page
PAGE_W_CM = 21.0
PAGE_H_CM = 29.7
MARGIN_CM = 2.0
CONTENT_W_CM = PAGE_W_CM - 2 * MARGIN_CM          # 17.0
LAND_CONTENT_W_CM = PAGE_H_CM - 2 * MARGIN_CM     # 25.7

CM2PT = 28.3464567

def cm2pt(x):
    return x * CM2PT

HEADER_RULE_PT = 0.75

# ---------------------------------------------------------------- textes fixes
DOC_FOOTER = "Plan S&E – Tech-4 | 2027-2028"
PROJECT_SHORT = "PMNS – Kwilu | Services NAC"
