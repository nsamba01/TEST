"""Génération des diagrammes (PNG) — images strictement identiques dans le DOCX et le PDF."""
import os
import math
from PIL import Image, ImageDraw, ImageFont

from charte import (PRIMARY, SECONDARY, ACCENT, LIGHT_BLUE, TEXT, GREY,
                    TABLE_BG, BORDER, WHITE)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets")
FONTS = os.path.join(ROOT, "fonts")
os.makedirs(OUT, exist_ok=True)

REG = os.path.join(FONTS, "Carlito-Regular.ttf")
BOLD = os.path.join(FONTS, "Carlito-Bold.ttf")
ITAL = os.path.join(FONTS, "Carlito-Italic.ttf")
BI = os.path.join(FONTS, "Carlito-BoldItalic.ttf")
SYM = os.path.join(FONTS, "DejaVuSans.ttf")

PPCM = 118.0
_fc = {}


def H(c):
    return "#" + c


def font(size_pt, bold=False, italic=False, sym=False):
    # PPCM px par cm = 300 dpi : 1 pt = 300/72 px sur le papier
    px = int(round(size_pt * PPCM * 2.54 / 72.0))
    key = (px, bold, italic, sym)
    if key not in _fc:
        if sym:
            path = os.path.join(FONTS, "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
        elif bold and italic:
            path = BI
        elif bold:
            path = BOLD
        elif italic:
            path = ITAL
        else:
            path = REG
        _fc[key] = ImageFont.truetype(path, px)
    return _fc[key]


def canvas(w_cm, h_cm):
    W, Hh = int(w_cm * PPCM), int(h_cm * PPCM)
    img = Image.new("RGB", (W, Hh), H(WHITE))
    return img, ImageDraw.Draw(img), W, Hh


def rrect(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=H(fill) if fill else None,
                        outline=H(outline) if outline else None, width=width)


def wrap(d, text, f, max_w):
    """Césure aux espaces et après les traits d'union ; les espaces insécables collent les nombres."""
    text = text.replace("\u00a0", "\x01")

    def L(t):
        return d.textlength(t, font=f)

    breaks = [i + 1 for i, ch in enumerate(text) if ch in (" ", "-") and i + 1 < len(text)]
    lines, start = [], 0
    while L(text[start:]) > max_w:
        fit = None
        for b in breaks:
            if b <= start:
                continue
            if L(text[start:b]) <= max_w:
                fit = b
            else:
                break
        if fit is None:
            fit = start + 1
        lines.append(text[start:fit].rstrip(" "))
        start = fit
        while start < len(text) and text[start] == " ":
            start += 1
    lines.append(text[start:])
    return [l.rstrip(" ").replace("\x01", "\u00a0") for l in lines]


def autosave(img, name, pad_cm=0.06):
    """Recadre au contenu puis enregistre. Retourne (chemin, largeur_cm, hauteur_cm)."""
    bg = Image.new("RGB", img.size, H(WHITE))
    from PIL import ImageChops
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        pad = int(pad_cm * PPCM)
        box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
               min(img.size[0], bbox[2] + pad), min(img.size[1], bbox[3] + pad))
        img = img.crop(box)
    path = os.path.join(OUT, name)
    img.save(path, dpi=(300, 300))
    return path, img.size[0] / PPCM, img.size[1] / PPCM


# =============================================================== GANTT
GANTT_ROWS = [
    ("A", "PLANIFICATION ET MESURE INITIALE", None),
    (None, "Cadrage participatif et validation du plan S&E", [(0, 1)]),
    (None, "Enquête de référence (SMART, CAP, fonctionnalité CAC/CODESA)", [(0, 2)]),
    (None, "Atelier de validation des cibles et du cadre de performance", [(2, 3)]),
    ("B", "COLLECTE EN CONTINU", None),
    (None, "Collecte routinière communautaire (registres RECO, tablettes)", [(0, 24)]),
    (None, "Collecte routinière FOSA (registres, DHIS2)", [(0, 24)]),
    (None, "Rapports mensuels AS → ZS → DPS / PRONANUT", [(0, 24)]),
    (None, "Transmission DHIS2 et SNSAP (20 sites sentinelles)", [(0, 24)]),
    ("C", "ASSURANCE QUALITÉ DES DONNÉES", None),
    (None, "Monitorage amélioré pour action (MAA) trimestriel", [(q, q + 1) for q in range(0, 24, 3)]),
    (None, "Audits de qualité des données (complétude, promptitude, cohérence)",
     [(1, 2), (4, 5), (7, 8), (10, 11), (13, 14), (16, 17), (19, 20), (22, 23)]),
    (None, "Third Party Monitoring (TPM) indépendant", [(3, 4), (9, 10), (15, 16), (21, 22)]),
    (None, "Supervisions conjointes DPS / PRONANUT / ECZS / Consortium", [(0, 24)]),
    ("D", "ANALYSE, REDEVABILITÉ ET REVUES", None),
    (None, "Revues trimestrielles de performance (consortium + ZS)",
     [(q + 2, q + 3) for q in range(0, 24, 3)]),
    (None, "Revues semestrielles de la nutrition (Gouverneur / Ministre)",
     [(5, 6), (11, 12), (17, 18), (23, 24)]),
    (None, "Bulletins trimestriels de données clés nutrition",
     [(q + 2, q + 3) for q in range(0, 24, 3)]),
    (None, "Contrôle communautaire et Bulletins de Performance (BCP)", [(1, 24)]),
    ("E", "ÉVALUATION ET RECHERCHE", None),
    (None, "Évaluation à mi-parcours (T3 2027)", [(6, 9)]),
    (None, "Évaluations thématiques (qualité des soins, VBG, FARN)", [(10, 12), (19, 21)]),
    (None, "Recherche opérationnelle (2 études protocolisées)", [(4, 10), (13, 19)]),
    (None, "Évaluation finale externe (T4 2028)", [(21, 24)]),
    ("F", "RAPPORTAGE ET APPRENTISSAGE", None),
    (None, "Rapports trimestriels à l'UG-PDSS", [(q + 2, q + 3) for q in range(0, 24, 3)]),
    (None, "Rapport annuel (Y1 : déc. 2027 — Y2 : déc. 2028)", [(11, 12), (23, 24)]),
    (None, "Capitalisation, documentation des bonnes pratiques", [(6, 12), (18, 24)]),
    (None, "Ateliers de gestion adaptative et planification glissante",
     [(5, 6), (11, 12), (17, 18), (23, 24)]),
]

SOFT = ["5E9FD8", "8FBEE6", "3F86C9"]


def gantt(name="gantt_24m.png"):
    W_CM = 17.0
    LABEL_W = 6.90
    HEAD = 1.72
    ROW_H = 0.560
    h_cm = HEAD + ROW_H * len(GANTT_ROWS) + 0.85

    img, d, W, Hh = canvas(W_CM, h_cm)
    P = PPCM
    gx = LABEL_W * P
    mw = (W_CM - LABEL_W - 0.02) * P / 24.0
    top = HEAD * P

    # --- en-tête
    d.rectangle([0, 0, W, 0.66 * P], fill=H(PRIMARY))
    d.text((0.16 * P, 0.20 * P), "ACTIVITÉS DE S&E", font=font(8.2, True), fill=H(WHITE))
    d.rectangle([gx, 0, W, 0.66 * P], fill=H(PRIMARY))
    for i, lab in enumerate(["ANNÉE 1 — 2027", "ANNÉE 2 — 2028"]):
        xa = gx + i * 12 * mw
        d.text((xa + (12 * mw - d.textlength(lab, font=font(8.6, True))) / 2, 0.17 * P),
               lab, font=font(8.6, True), fill=H(WHITE))
    d.rectangle([0, 0.66 * P, gx, 1.24 * P], fill=H("0B5FA5"))
    d.text((0.16 * P, 0.80 * P), "et périodes de mise en œuvre", font=font(6.8),
           fill=H("CDE4F7"))
    d.rectangle([gx, 0.66 * P, W, 1.24 * P], fill=H("0B5FA5"))
    for t in range(8):
        lab = f"T{t % 4 + 1}"
        xa = gx + t * 3 * mw
        d.text((xa + (3 * mw - d.textlength(lab, font=font(7.4, True))) / 2, 0.80 * P),
               lab, font=font(7.4, True), fill=H(WHITE))
    for m in range(24):
        xa = gx + m * mw
        d.rectangle([xa, 1.24 * P, xa + mw, 1.72 * P],
                    fill=H(LIGHT_BLUE if m < 12 else "D8E8F8"))
        lab = "JFMAMJJASOND"[m % 12]
        d.text((xa + (mw - d.textlength(lab, font=font(6.0))) / 2, 1.34 * P),
               lab, font=font(6.0), fill=H(GREY))

    # --- fonds de lignes
    y = top
    band = False
    for letter, label, bars in GANTT_ROWS:
        hh = ROW_H * P
        if bars is not None:
            if band:
                d.rectangle([0, y, W, y + hh], fill=H(TABLE_BG))
            band = not band
        y += hh

    # --- grille (sous les barres)
    y = top
    for _ in range(len(GANTT_ROWS)):
        d.line([0, y, W, y], fill=H("E9EEF3"), width=1)
        y += ROW_H * P
    for m in range(25):
        xa = gx + m * mw
        d.line([xa, top, xa, y], fill=H("E3EAF2" if m % 3 else "C9D8E9"), width=1)
    for t in range(1, 8):
        d.line([gx + t * 3 * mw, top, gx + t * 3 * mw, y], fill=H("A9C2DA"), width=1)
    d.line([gx + 12 * mw, 0, gx + 12 * mw, y], fill=H(PRIMARY), width=4)

    # --- lignes
    y = top
    f_lab = font(6.4)
    for letter, label, bars in GANTT_ROWS:
        hh = ROW_H * P
        if bars is None:
            d.rectangle([0, y, W, y + hh], fill=H(SECONDARY))
            fl = font(7.6, True)
            d.text((0.16 * P, y + (hh - fl.size) / 2 - 0.04 * P), letter,
                   font=fl, fill=H(WHITE))
            fp = font(7.4, True)
            d.text((0.56 * P, y + (hh - fp.size) / 2 - 0.04 * P), label,
                   font=fp, fill=H(WHITE))
        else:
            lines = wrap(d, label, f_lab, LABEL_W * P - 0.30 * P)
            ty = y + (hh - len(lines) * f_lab.size * 1.18) / 2
            for ln in lines[:2]:
                d.text((0.16 * P, ty), ln, font=f_lab, fill=H(TEXT))
                ty += f_lab.size * 1.18
            for i, (a, b) in enumerate(bars):
                bx0 = gx + a * mw + 1.2
                bx1 = gx + b * mw - 1.2
                col = PRIMARY if (b - a) <= 2 else SOFT[i % 3]
                rrect(d, [bx0, y + hh * 0.27, bx1, y + hh * 0.73],
                      int(hh * 0.21), fill=col)
        y += hh

    d.rectangle([0, top, W - 1, y], outline=H(BORDER), width=2)

    # --- légende
    ly = y + 0.22 * P
    lx = 0.16 * P
    f7 = font(6.9)
    for col, lab in ((PRIMARY, "activité ponctuelle"), ("8FBEE6", "activité récurrente / continue")):
        d.rounded_rectangle([lx, ly + 0.03 * P, lx + 0.52 * P, ly + 0.21 * P],
                            radius=int(0.07 * P), fill=H(col))
        d.text((lx + 0.64 * P, ly + 0.02 * P), lab, font=f7, fill=H(GREY))
        lx += 0.64 * P + d.textlength(lab, font=f7) + 0.45 * P
    d.line([lx, ly - 0.02 * P, lx, ly + 0.26 * P], fill=H(PRIMARY), width=3)
    d.text((lx + 0.14 * P, ly + 0.02 * P), "passage à l'année 2", font=f7, fill=H(GREY))

    return autosave(img, name)


# =============================================================== THÉORIE DU CHANGEMENT
LEVELS = [
    ("INTRANTS", SECONDARY, [
        "Financement PMNS / UG-PDSS",
        "Consortium SANRU-ICHESS-FONLIV-FDSS",
        "63 superviseurs nutritionnistes · 33 staffs d'appui",
        "Intrants : Vit A, Mébendazole, Fer/FAF, SRO-Zinc, MNPs",
        "Équipements : MUAC, balances, toises, tablettes",
        "Outils de gestion et de rapportage",
    ]),
    ("ACTIVITÉS", PRIMARY, [
        "Formation de 8 314 RECO et 846 prestataires de FOSA",
        "Dotation et approvisionnement des 3 188 CAC et 423 FOSA",
        "VAD, CPSr, PCIMA, ANJE/PFE, démonstrations culinaires",
        "MAA trimestriel, supervisions formatives, revues",
        "Sensibilisation VBG/EAS/HS et référencement des SVS",
    ]),
    ("EXTRANTS", "3F86C9", [
        "3 188 CAC et 250 CODESA fonctionnelles",
        "423 FOSA offrant le paquet nutritionnel",
        "30 FARN opérationnels (Yasa Bonga, Kingandu)",
        "10 comités locaux VBG actifs",
        "Données DHIS2 complètes, promptes et cohérentes",
    ]),
    ("RÉSULTATS", "1F6FB2", [
        "Accès, utilisation et qualité des services NAC améliorés (OS1)",
        "Système de prise en charge des SVS renforcé (OS2)",
        "Structures de participation communautaire performantes (OS3)",
        "Système de santé offrant des services de nutrition de qualité (OS4)",
    ]),
    ("IMPACT", "14507F", [
        "Réduction du retard de croissance chez l'enfant de moins de 2 ans",
        "Réduction de la morbidité et de la mortalité liées à la malnutrition",
        "Capital humain préservé dans la province du Kwilu",
    ]),
]


def toc_edo(name="theorie_changement.png"):
    W_CM = 17.0
    GAP = 0.30
    bw = (W_CM - 4 * GAP) / 5.0
    img, d, W, Hh = canvas(W_CM, 16.0)
    P = PPCM

    # bandeau
    d.rectangle([0, 0, W, 0.95 * P], fill=H(SECONDARY))
    t = "MODÈLE EDO — ENVIRONNEMENT  ·  DEMANDE  ·  OFFRE"
    d.text(((W - d.textlength(t, font=font(9.6, True))) / 2, 0.27 * P), t,
           font=font(9.6, True), fill=H(WHITE))

    # mesure de la hauteur nécessaire
    ytop = 1.20 * P
    f = font(7.4)
    max_h = 0
    for _, _, items in LEVELS:
        hh = 0.20 * P
        for it in items:
            hh += len(wrap(d, "•  " + it, f, bw * P - 0.36 * P)) * f.size * 1.20 + 0.20 * P
        max_h = max(max_h, hh)
    body_h = max_h + 0.24 * P

    for i, (title, color, items) in enumerate(LEVELS):
        x = i * (bw + GAP) * P
        wpx = bw * P
        rrect(d, [x, ytop, x + wpx, ytop + 0.80 * P], int(0.09 * P), fill=color)
        d.text((x + (wpx - d.textlength(title, font=font(8.4, True))) / 2, ytop + 0.21 * P),
               title, font=font(8.4, True), fill=H(WHITE))
        rrect(d, [x, ytop + 0.80 * P, x + wpx, ytop + 0.80 * P + body_h], int(0.10 * P),
              fill=LIGHT_BLUE, outline=BORDER, width=2)
        yy = ytop + 1.06 * P
        for it in items:
            for ln in wrap(d, "•  " + it, f, wpx - 0.36 * P):
                d.text((x + 0.16 * P, yy), ln, font=f, fill=H(TEXT))
                yy += f.size * 1.20
            yy += 0.20 * P
        if i < 4:
            cxp = x + wpx + GAP * P / 2
            cyp = ytop + 0.80 * P + body_h * 0.5
            s_ = 0.11 * P
            d.polygon([(cxp - s_, cyp - s_), (cxp + s_, cyp), (cxp - s_, cyp + s_)], fill=H(ACCENT))

    # hypothèses
    hy = ytop + 0.80 * P + body_h + 0.34 * P
    fh = font(7.2)
    hyp = ("Stabilité sécuritaire et sanitaire · disponibilité continue des intrants · motivation et stabilité "
           "des RECO et des prestataires formés · fiabilité des dénominateurs · appropriation communautaire et "
           "engagement des autorités · décaissements à temps.")
    hl = wrap(d, hyp, fh, W - 0.44 * P)
    hbox = 0.50 * P + len(hl) * fh.size * 1.20 + 0.16 * P
    rrect(d, [0, hy, W, hy + hbox], int(0.09 * P), fill="FDF1E6", outline=ACCENT, width=2)
    d.text((0.20 * P, hy + 0.12 * P), "HYPOTHÈSES CRITIQUES", font=font(7.8, True), fill=H("B4651E"))
    yy = hy + 0.46 * P
    for ln in hl:
        d.text((0.20 * P, yy), ln, font=fh, fill=H(TEXT))
        yy += fh.size * 1.20

    sy = hy + hbox + 0.16 * P
    rrect(d, [0, sy, W, sy + 0.62 * P], int(0.09 * P), fill=SECONDARY)
    t = ("AXE TRANSVERSAL : S&E, REDEVABILITÉ et APPRENTISSAGE  ·  genre et droits humains  ·  "
         "digitalisation (DHIS2, ODK)")
    d.text(((W - d.textlength(t, font=font(7.6, True))) / 2, sy + 0.17 * P), t,
           font=font(7.6, True), fill=H(WHITE))

    return autosave(img, name)


# =============================================================== FLUX DE DONNÉES
def flux(name="flux_donnees.png"):
    W_CM, H_CM = 17.0, 8.0
    img, d, W, Hh = canvas(W_CM, H_CM)
    P = PPCM

    def node(cx, cy, w, h, title, sub, fill, tcol=WHITE):
        rrect(d, [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], int(0.10 * P),
              fill=fill, outline=WHITE, width=3)
        f1, f2 = font(7.8, True), font(6.6)
        tl = wrap(d, title, f1, w - 0.30 * P)
        sl = wrap(d, sub, f2, w - 0.30 * P)
        th = len(tl) * f1.size * 1.10 + 0.08 * P + len(sl) * f2.size * 1.15
        yy = cy - th / 2
        for ln in tl:
            d.text((cx - d.textlength(ln, font=f1) / 2, yy), ln, font=f1, fill=H(tcol))
            yy += f1.size * 1.10
        yy += 0.08 * P
        for ln in sl:
            d.text((cx - d.textlength(ln, font=f2) / 2, yy), ln, font=f2, fill=H("EAF3FB"))
            yy += f2.size * 1.15

    def arrow(x1, y1, x2, y2, color="A9B4C0", w=3):
        d.line([x1, y1, x2, y2], fill=H(color), width=w)
        ang = math.atan2(y2 - y1, x2 - x1)
        L = 0.16 * P
        d.polygon([(x2, y2),
                   (x2 - L * math.cos(ang - 0.42), y2 - L * math.sin(ang - 0.42)),
                   (x2 - L * math.cos(ang + 0.42), y2 - L * math.sin(ang + 0.42))], fill=H(color))

    x1, x2, x3 = 2.60 * P, 8.50 * P, 14.40 * P
    ys = [0.85 * P, 2.45 * P, 4.05 * P]
    nw1, nw2, nw3 = 4.6 * P, 4.9 * P, 4.6 * P
    nh = 1.22 * P

    node(x1, ys[0], nw1, nh, "RECO", "Fiche de VAD · registre · tablette ODK", SECONDARY)
    node(x1, ys[1], nw1, nh, "CAC", "Compilation mensuelle · BCP", "3F86C9")
    node(x1, ys[2], nw1, nh, "CODESA / UCODESA", "Rapport de l'aire de santé", PRIMARY)

    node(x2, ys[0], nw2, nh, "FOSA / UNTA / UNTI", "Registres CPSr, CPN, PCIMA", SECONDARY)
    node(x2, ys[1], nw2, nh, "IT / BCZS / ECZS", "Canevas standardisés · MAA", "3F86C9")
    node(x2, ys[2], nw2, nh, "DPS Kwilu / PRONANUT", "Bulletins trimestriels", PRIMARY)

    node(x3, ys[0], nw3, nh, "DHIS2 / SNSAP", "SNIS national · 20 sites sentinelles", "14507F")
    node(x3, ys[1], nw3, nh, "UG-PDSS / MSPHP", "Rapports périodiques M · T · A", "14507F")
    node(x3, ys[2], nw3, nh, "Revues & évaluations", "MAA · semestrielles · mi-parcours", ACCENT)

    for xc in (x1, x2):
        arrow(xc, ys[0] + nh / 2, xc, ys[1] - nh / 2)
        arrow(xc, ys[1] + nh / 2, xc, ys[2] - nh / 2)
    arrow(x1 + nw1 / 2 - 0.12 * P, ys[2] - 0.10 * P, x2 - nw2 / 2 + 0.06 * P, ys[1] + 0.16 * P)
    for yv in ys:
        arrow(x2 + nw2 / 2, yv, x3 - nw3 / 2, yv)

    fy = 4.95 * P
    rrect(d, [0, fy, W, fy + 1.42 * P], int(0.10 * P), fill=LIGHT_BLUE, outline=PRIMARY, width=3)
    d.text((0.20 * P, fy + 0.13 * P), "BOUCLE DE RÉTROACTION", font=font(8.0, True), fill=H(PRIMARY))
    fb = ("Feedbacks trimestriels du Responsable S&E/HMIS vers les ECZS et les CAC · Bulletins de Performance "
          "Communautaire restitués aux communautés · plan de redressement validé en revue de performance · "
          "données désagrégées par sexe, âge et zone de santé.")
    yy = fy + 0.52 * P
    for ln in wrap(d, fb, font(7.4), W - 0.40 * P):
        d.text((0.20 * P, yy), ln, font=font(7.4), fill=H(TEXT))
        yy += font(7.4).size * 1.20

    ly = fy + 1.62 * P
    lx = 0.05 * P
    f6 = font(7.2)
    for col, lab in ((SECONDARY, "niveau communautaire et périphérique"),
                     (PRIMARY, "niveau zonal et provincial"),
                     ("14507F", "niveau national / bailleur")):
        d.rounded_rectangle([lx, ly + 0.05 * P, lx + 0.26 * P, ly + 0.21 * P], radius=int(0.05 * P), fill=H(col))
        d.text((lx + 0.34 * P, ly), lab, font=f6, fill=H(GREY))
        lx += 0.34 * P + d.textlength(lab, font=f6) + 0.50 * P

    return autosave(img, name)


# =============================================================== DASHBOARD
FEUX = [
    ("Couverture des villages en CAC fonctionnelles", 71, 100),
    ("RECO formés (sur 8 314 attendus)", 0, 100),
    ("FOSA offrant le paquet nutritionnel complet", 0, 100),
    ("Enfants MAS référés effectivement pris en charge (cible ≥ 80 %)", 0, 80),
    ("Survivantes de VBG avec prise en charge holistique (cible ≥ 50 %)", 1.9, 50),
    ("Zones de santé rapportant des cas de VBG dans DHIS2", 60, 100),
    ("Femmes enceintes ayant bénéficié d'au moins 4 CPN", 24.3, 100),
    ("CAC tenant leurs réunions mensuelles de monitorage", 53.6, 100),
]


def dashboard(name="dashboard.png"):
    W_CM = 17.0
    ROW_H = 0.86
    h_cm = 1.02 + ROW_H * len(FEUX) + 0.62
    img, d, W, Hh = canvas(W_CM, h_cm)
    P = PPCM

    d.rectangle([0, 0, W, 0.86 * P], fill=H(PRIMARY))
    d.text((0.20 * P, 0.21 * P), "TABLEAU DE BORD — POSITIONNEMENT AU DÉMARRAGE (RÉFÉRENCE 2026)",
           font=font(9.4, True), fill=H(WHITE))

    gx0, gx1 = 7.05 * P, 12.95 * P
    y = 1.05 * P
    fl = font(8.0)
    for label, base, cible in FEUX:
        lines = wrap(d, label, fl, 6.60 * P)
        ty = y + (ROW_H * P - len(lines) * fl.size * 1.18) / 2
        for ln in lines:
            d.text((0.20 * P, ty), ln, font=fl, fill=H(TEXT))
            ty += fl.size * 1.18
        gy = y + (ROW_H * P - 0.22 * P) / 2
        d.rounded_rectangle([gx0, gy, gx1, gy + 0.22 * P], radius=int(0.09 * P), fill=H("E8EDF3"))
        span = gx1 - gx0
        ratio = min(base / cible, 1.0)
        col = "2E8B57" if ratio >= 0.66 else ("F4A460" if ratio >= 0.33 else "C0392B")
        if base > 0:
            d.rounded_rectangle([gx0, gy, gx0 + max(span * ratio, 0.08 * P), gy + 0.22 * P],
                                radius=int(0.09 * P), fill=H(col))
        d.line([gx1, gy - 0.06 * P, gx1, gy + 0.28 * P], fill=H("1F6FB2"), width=4)
        d.text((gx1 + 0.18 * P, y + (ROW_H * P - fl.size * 1.1) / 2),
               f"{base:g} %  →  cible {cible:g} %", font=font(7.8, True), fill=H(GREY))
        d.line([0.20 * P, y + ROW_H * P - 0.03 * P, W - 0.20 * P, y + ROW_H * P - 0.03 * P],
               fill=H("EDF1F5"), width=1)
        y += ROW_H * P

    ly = y + 0.12 * P
    lx = 0.20 * P
    f6 = font(7.6)
    for col, lab in ((SECONDARY, "Sur la bonne voie"), (ACCENT, "Attention requise"), ("C0392B", "En retard")):
        d.ellipse([lx, ly + 0.05 * P, lx + 0.18 * P, ly + 0.23 * P], fill=H(col))
        d.text((lx + 0.25 * P, ly), lab, font=f6, fill=H(TEXT))
        lx += 0.25 * P + d.textlength(lab, font=f6) + 0.45 * P
    d.text((lx, ly), "Codes attribués par rapport au rythme d'atteinte de la cible annuelle.",
           font=f6, fill=H(GREY))

    return autosave(img, name)


def build_all():
    res = {}
    for key, fn in (("gantt", gantt), ("toc", toc_edo), ("flux", flux), ("dashboard", dashboard)):
        path, w, h = fn()
        res[key] = {"path": path, "w_cm": w, "h_cm": h}
    return res


if __name__ == "__main__":
    for k, v in build_all().items():
        print(k, "%.2f x %.2f cm" % (v["w_cm"], v["h_cm"]))
