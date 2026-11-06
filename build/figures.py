# -*- coding: utf-8 -*-
"""Figures générées en PNG haute résolution, embarquées à l'identique dans le
DOCX et le PDF (garantit un rendu strictement identique).

Les figures sont dessinées à leur largeur d'insertion finale (6,5 po ≈ largeur
de composition A4) : les corps de texte restent donc à leur taille réelle.
Géométrie déterministe (pas de bbox "tight") pour que le repli soit exact.
"""
import os
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager as fm

import design as D

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)

for _f in (D.FONT_REG, D.FONT_BOLD, D.FONT_IT, D.FONT_BI):
    fm.fontManager.addfont(os.path.join(HERE, _f))
plt.rcParams["font.family"] = "Carlito"
plt.rcParams["savefig.dpi"] = 300

FIGW = 6.5          # pouces — largeur d'insertion cible
_SIZES = {}


def _c(h):
    return "#" + h.lstrip("#")


def _canvas(h_in, w_in=FIGW):
    fig = plt.figure(figsize=(w_in, h_in))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    _SIZES[id(ax)] = (w_in, h_in)
    return fig, ax


def _save(fig, path):
    fig.savefig(path, facecolor="white")
    plt.close(fig)


def _box(ax, x, y, w, h, text="", fc="#FFFFFF", ec=None, tc=None, fs=6.4,
         bold=False, radius=0.006, lw=0.8, ha="center", va="center"):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0,rounding_size={radius}",
                                linewidth=lw, facecolor=fc,
                                edgecolor=ec or _c(D.GREY_LN), zorder=2))
    if text:
        tx = x + w / 2 if ha == "center" else x + 0.008
        ax.text(tx, y + h / 2, text, ha=ha, va=va, fontsize=fs,
                color=tc or _c(D.GREY_TXT),
                fontweight="bold" if bold else "normal", zorder=3, linespacing=1.35)


def _arrow(ax, x1, y1, x2, y2, color=None, lw=1.2, style="-|>", rad=0.0, ms=9):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=ms, linewidth=lw,
                                 color=color or _c(D.TEAL),
                                 connectionstyle=f"arc3,rad={rad}", zorder=4,
                                 shrinkA=0, shrinkB=0))


def _nchars(ax, w_data, fs, char_em=0.515, margin=0.016):
    w_in = _SIZES[id(ax)][0]
    return max(8, int(((w_data - margin) * w_in * 72.0) / (char_em * fs)))


def _wrap(text, n):
    out = []
    for para in text.split("\n"):
        if not para.strip():
            out.append("")
        else:
            out.extend(textwrap.wrap(para, width=n, break_long_words=False,
                                     break_on_hyphens=False))
    return "\n".join(out)


def _textcol(ax, x, ytop, w, text, fs=6.3, color=None, ls=1.55):
    ax.text(x, ytop, _wrap(text, _nchars(ax, w, fs)), ha="left", va="top",
            fontsize=fs, color=color or _c(D.GREY_TXT), linespacing=ls, zorder=3)


# ======================================================================
# 1. Logique d'intervention (chaîne verticale)
# ======================================================================
def fig_theorie_changement(path):
    stages = [
        ("RESSOURCES", "(intrants)", D.NAVY_L, "#FFFFFF",
         ["Financement UG-PDSS / Banque mondiale",
          "Consortium SANRU – ICHESS – FONLIV – FDSS",
          "Personnel clé et d’appoint : UGP Kikwit et 5 sous-bureaux",
          "3 véhicules, 25 motos, 33 ordinateurs",
          "Intrants nutritionnels (UNICEF, CAMEBASU)",
          "2 738 smartphones et registre électronique"]),
        ("ACTIVITÉS", "", D.NAVY, "#FFFFFF",
         ["Former les prestataires (RECO, FOSA, ECZS)",
          "Doter les sites en intrants et équipements",
          "Mettre en place et redynamiser CAC, CODESA, UCODESA",
          "Organiser les VAD et le dépistage communautaire",
          "Appuyer CPSr, PCIMA, ANJE, CPN et CPoN",
          "Sensibiliser sur les VBG/EAS/HS",
          "Renforcer la coordination multisectorielle"]),
        ("EXTRANTS", "(outputs)", D.TEAL, "#FFFFFF",
         ["8 314 RECO et 846 prestataires de FOSA formés",
          "3 188 CAC, 250 CODESA et 10 UCODESA fonctionnels",
          "423 FOSA approvisionnées et dotées",
          "30 FARN opérationnels, 190 SSC appuyés",
          "6 FOSA dotées en kits PEP",
          "2 500 pairs-éducateurs formés"]),
        ("EFFETS", "(outcomes)", D.TEAL_L, "#" + D.NAVY,
         ["Accès et utilisation améliorés des services communautaires (RI 1.1)",
          "Qualité des services communautaires améliorée (RI 1.3)",
          "Communautés engagées contre les VBG (RI 2.2)",
          "Structures communautaires renforcées (RI 3.1 – 3.2)",
          "Offre et utilisation des services de nutrition dans les 423 FOSA (RI 4.1 – 4.2)"]),
        ("IMPACT", "", D.GREY_BG2, "#" + D.NAVY,
         ["Accroître l’accès et l’utilisation du paquet de services de nutrition de qualité dans les FOSA et dans la communauté.",
          "Contribution à la réduction de la mortalité et de la morbidité liées à la malnutrition (enfants de 6-59 mois, FEFA) dans les 10 ZS du Kwilu."]),
    ]

    FS = 6.2
    LS = 1.62
    line_in = FS * LS / 72.0
    pad_in = 0.13
    gap_in = 0.16
    xl, wl = 0.004, 0.152
    xp = 0.170
    wp = 1.0 - xp - 0.004

    # --- passe 1 : nombre de lignes par bloc (repli identique dans les 2 passes)
    w_pt = (wp - 0.016) * FIGW * 72.0
    nchars = max(8, int(w_pt / (0.515 * FS)))
    wrapped = []
    for _, _, _, _, items in stages:
        txt = "\n".join("• " + t for t in items)
        wrapped.append(_wrap(txt, nchars))
    heights = [(w.count("\n") + 1) * line_in + pad_in for w in wrapped]
    total_in = sum(heights) + gap_in * (len(stages) - 1) + 0.52

    fig, ax = _canvas(total_in)
    y = 1.0 - 0.045
    for i, ((name, sub, fc, tc, _), txt, hi) in enumerate(zip(stages, wrapped, heights)):
        h = hi / total_in
        y -= h
        _box(ax, xl, y, wl, h, "", _c(fc), ec=_c(fc), radius=0.006)
        ax.text(xl + wl / 2, y + h / 2, name + ("\n" + sub if sub else ""),
                ha="center", va="center", fontsize=6.0, color=tc,
                fontweight="bold", zorder=3, linespacing=1.4)
        _box(ax, xp, y, wp, h, "", "#FFFFFF" if i not in (3, 4) else _c(D.TEAL_L),
             ec=_c(D.GREY_LN), radius=0.006)
        ax.text(xp + 0.010, y + h - (pad_in / 2) / total_in, txt, ha="left", va="top",
                fontsize=FS, color=_c(D.GREY_TXT), linespacing=LS, zorder=3)
        if i < len(stages) - 1:
            y -= gap_in / total_in
            _arrow(ax, xl + wl / 2, y + gap_in / total_in - 0.001, xl + wl / 2, y + 0.002,
                   color=_c(D.TEAL), lw=1.1, ms=7)

    ax.text(0.5, 0.004,
            "Logique reconstituée à partir de Tech-4. Les volumes indiqués sont ceux du document source.",
            ha="center", va="bottom", fontsize=5.6, color=_c(D.GREY_MID), style="italic")
    _save(fig, path)


# ======================================================================
# 2. Modèle EDO
# ======================================================================
def fig_edo(path):
    fig, ax = _canvas(3.55)

    # --- Offre / Demande
    for x0, titre, corps in [
        (0.006, "OFFRE / SERVICES",
         "Le personnel est capable d’offrir des prestations de nutrition de qualité "
         "accessibles à la communauté."),
        (0.694, "DEMANDE",
         "Les individus, les familles et les communautés ont les connaissances et la "
         "capacité de rechercher et d’utiliser des services de nutrition de qualité."),
    ]:
        _box(ax, x0, 0.655, 0.300, 0.290, "", _c(D.TEAL_L), ec=_c(D.TEAL), radius=0.010)
        ax.text(x0 + 0.150, 0.912, titre, ha="center", va="top",
                fontsize=6.4, color=_c(D.NAVY), fontweight="bold", zorder=3)
        _textcol(ax, x0 + 0.013, 0.842, 0.274, corps, fs=5.8)

    # --- État nutritionnel
    _box(ax, 0.330, 0.380, 0.340, 0.190, "ÉTAT\nNUTRITIONNEL\nAMÉLIORÉ",
         _c(D.NAVY), ec=_c(D.NAVY), tc="#FFFFFF", fs=7.8, bold=True, radius=0.014)

    # --- Environnement favorable
    _box(ax, 0.180, 0.030, 0.640, 0.215, "", _c(D.GREY_BG), ec=_c(D.GREY_LN), radius=0.010)
    ax.text(0.500, 0.222, "ENVIRONNEMENT FAVORABLE", ha="center", va="top",
            fontsize=6.2, color=_c(D.NAVY), fontweight="bold", zorder=3)
    _textcol(ax, 0.194, 0.183, 0.612,
             "L’environnement politique, du programme et communautaire, associé aux normes "
             "sociales et de genre, soutient le fonctionnement des systèmes de santé.",
             fs=5.6)

    # --- Flèches
    _arrow(ax, 0.156, 0.652, 0.372, 0.462, color=_c(D.GOLD), lw=1.9, rad=0.26, ms=10)
    _arrow(ax, 0.844, 0.652, 0.628, 0.462, color=_c(D.GOLD), lw=1.9, rad=-0.26, ms=10)
    _arrow(ax, 0.500, 0.248, 0.500, 0.377, color=_c(D.GOLD), lw=1.9, ms=10)

    # --- Libellés (dans les zones libres)
    ax.text(0.012, 0.618, "Renforcement de l’offre", ha="left", va="top",
            fontsize=5.5, color=_c(D.GOLD), style="italic")
    ax.text(0.982, 0.618, "Transformation des normes sociales", ha="right", va="top",
            fontsize=5.5, color=_c(D.GOLD), style="italic")
    ax.text(0.508, 0.312, "Renforcement de la demande", ha="left", va="center",
            fontsize=5.5, color=_c(D.GOLD), style="italic")

    ax.text(0.500, 0.975, "Interaction client – prestataire de qualité", ha="center",
            va="top", fontsize=5.9, color=_c(D.TEAL), style="italic")
    _save(fig, path)


# ======================================================================
# 3. Dispositif institutionnel du suivi-évaluation
# ======================================================================
def fig_dispositif(path):
    fig, ax = _canvas(4.35)

    _box(ax, 0.230, 0.885, 0.540, 0.090, "", _c(D.NAVY), ec=_c(D.NAVY))
    ax.text(0.500, 0.960, "COMITÉ DE PILOTAGE DU CONSORTIUM (CPP)", ha="center", va="top",
            fontsize=6.2, color="#FFFFFF", fontweight="bold", zorder=3)
    ax.text(0.500, 0.918, "Revue trimestrielle des performances", ha="center", va="top",
            fontsize=5.6, color="#FFFFFF", zorder=3)

    _box(ax, 0.008, 0.672, 0.290, 0.158, "", _c(D.TEAL_L), ec=_c(D.TEAL))
    ax.text(0.153, 0.812, "DPS Kwilu – PRONANUT", ha="center", va="top",
            fontsize=5.8, color=_c(D.NAVY), fontweight="bold", zorder=3)
    _textcol(ax, 0.018, 0.768, 0.270,
             "Validation technique, revues semestrielles, audits de qualité des données.", fs=5.2)

    _box(ax, 0.702, 0.672, 0.290, 0.158, "", _c(D.TEAL_L), ec=_c(D.TEAL))
    ax.text(0.847, 0.812, "UG-PDSS", ha="center", va="top",
            fontsize=5.8, color=_c(D.NAVY), fontweight="bold", zorder=3)
    _textcol(ax, 0.712, 0.768, 0.270,
             "Revues de performance, rapports périodiques et rapports annuels.", fs=5.2)

    _box(ax, 0.330, 0.690, 0.340, 0.122, "", _c(D.GOLD), ec=_c(D.GOLD))
    ax.text(0.500, 0.798, "DIRECTEUR DE PROJET", ha="center", va="top",
            fontsize=6.0, color="#FFFFFF", fontweight="bold", zorder=3)
    ax.text(0.500, 0.752, "Validation finale", ha="center", va="top",
            fontsize=5.4, color="#FFFFFF", zorder=3)

    _arrow(ax, 0.500, 0.883, 0.500, 0.815, color=_c(D.NAVY_L), lw=1.1, ms=8)
    _arrow(ax, 0.328, 0.751, 0.300, 0.751, color=_c(D.TEAL), lw=1.0, style="<|-|>", ms=7)
    _arrow(ax, 0.672, 0.751, 0.700, 0.751, color=_c(D.TEAL), lw=1.0, style="<|-|>", ms=7)

    _box(ax, 0.255, 0.520, 0.490, 0.105, "", _c(D.NAVY_L), ec=_c(D.NAVY_L))
    ax.text(0.500, 0.610, "RESPONSABLE S&E / HMIS", ha="center", va="top",
            fontsize=6.0, color="#FFFFFF", fontweight="bold", zorder=3)
    ax.text(0.500, 0.570, "Pilotage du plan · consolidation · analyse · assurance qualité",
            ha="center", va="top", fontsize=5.1, color="#FFFFFF", zorder=3)
    _arrow(ax, 0.500, 0.688, 0.500, 0.628, color=_c(D.NAVY_L), lw=1.1, style="<|-|>", ms=8)

    row = [
        "Spécialiste en Nutrition\nCollecte thématique",
        "Marchés publics\net logistique\nIntrants",
        "Engagement\ncommunautaire et genre\nVolet VBG",
        "Conseillers des ZS\nen NAC et en\nengagement (14)",
        "RH et IT\nRegistre\nélectronique",
    ]
    x = 0.008
    for txt in row:
        _box(ax, x, 0.340, 0.190, 0.140, "", _c(D.GREY_BG), ec=_c(D.GREY_LN))
        ax.text(x + 0.095, 0.462, txt, ha="center", va="top", fontsize=5.0,
                color=_c(D.GREY_TXT), zorder=3, linespacing=1.6)
        _arrow(ax, x + 0.095, 0.482, x + 0.095, 0.518, color=_c(D.TEAL_M), lw=0.9, ms=6)
        x += 0.198

    _box(ax, 0.008, 0.045, 0.984, 0.195, "", _c(D.TEAL_L), ec=_c(D.TEAL))
    ax.text(0.024, 0.215, "NIVEAU PÉRIPHÉRIQUE — COLLECTE ET CONTRÔLE DE PREMIER NIVEAU",
            ha="left", va="top", fontsize=5.8, color=_c(D.NAVY), fontweight="bold")
    ax.text(0.024, 0.170,
            "10 ECZS · 423 FOSA · 3 188 CAC · 250 CODESA · 10 UCODESA · 8 314 RECO\n"
            "Registres électroniques communautaires · DHIS2\n"
            "Supervisions formatives mensuelles · Monitorage amélioré pour l’action (MAA) trimestriel",
            ha="left", va="top", fontsize=5.3, color=_c(D.GREY_TXT), linespacing=1.9)
    _save(fig, path)


# ======================================================================
# 4. Répartition des indicateurs
# ======================================================================
def fig_indic_repartition(path, counts):
    labels = list(counts.keys())
    vals = [counts[k] for k in labels]
    from matplotlib.ticker import MaxNLocator
    fig, ax = plt.subplots(figsize=(6.5, 1.95))
    fig.subplots_adjust(left=0.150, right=0.975, top=0.780, bottom=0.245)
    colors = [_c(D.NAVY), _c(D.NAVY_L), _c(D.TEAL), _c(D.TEAL_M)]
    bars = ax.barh(labels[::-1], vals[::-1], color=colors[:len(labels)][::-1],
                   height=0.62, edgecolor="none")
    for b, v in zip(bars, vals[::-1]):
        ax.text(b.get_width() + 0.22, b.get_y() + b.get_height() / 2, str(v),
                va="center", fontsize=8.2, color=_c(D.NAVY), fontweight="bold")
    ax.set_xlim(0, max(vals) * 1.18)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.set_xlabel("Nombre d’indicateurs", fontsize=6.6, color=_c(D.GREY_MID))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(_c(D.GREY_LN))
    ax.tick_params(axis="y", length=0, labelsize=7.4, colors=_c(D.GREY_TXT))
    ax.tick_params(axis="x", labelsize=6.4, colors=_c(D.GREY_MID), length=2)
    fig.text(0.012, 0.965,
             "Répartition des indicateurs du cadre de performance par niveau de résultat",
             fontsize=7.4, color=_c(D.NAVY), fontweight="bold", va="top")
    _save(fig, path)


# ======================================================================
# 5. Couverture des interventions dans les FOSA (PRONANUT 2020)
# ======================================================================
def fig_couverture_fosa(path):
    fig, ax = plt.subplots(figsize=(6.5, 2.45))
    fig.subplots_adjust(left=0.098, right=0.975, top=0.720, bottom=0.165)
    lab = ["CPSr", "ANJE", "PCIMA", "NAC"]
    val = [47.1, 50.0, 0.0, 0.0]
    bars = ax.bar(lab, val, color=[_c(D.NAVY_L), _c(D.TEAL), _c(D.GREY_MID), _c(D.GREY_MID)],
                  width=0.44, edgecolor="none")
    for b, v in zip(bars, val):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.6, ("%.1f %%" % v).replace(".", ","),
                ha="center", fontsize=7.6, color=_c(D.NAVY), fontweight="bold")
    ax.set_ylim(0, 60)
    ax.set_ylabel("Couverture (%)", fontsize=6.6, color=_c(D.GREY_MID))
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(_c(D.GREY_LN))
    ax.spines["bottom"].set_color(_c(D.GREY_LN))
    ax.tick_params(labelsize=7.4, colors=_c(D.GREY_TXT), length=2)
    fig.text(0.012, 0.965, "Couverture des interventions de nutrition dans les FOSA des 10 ZS",
             fontsize=7.4, color=_c(D.NAVY), fontweight="bold", va="top")
    fig.text(0.012, 0.902, "Rapport annuel PRONANUT Kwilu 2020, cité par Tech-4",
             fontsize=6.0, color=_c(D.GREY_MID), va="top", style="italic")
    _save(fig, path)


# ======================================================================
# 6. Couverture et fonctionnalité des CAC par ZS
# ======================================================================
def fig_cac(path, zs_data):
    import numpy as np
    names = [r[0] for r in zs_data]
    couv = [r[1] for r in zs_data]
    fonc = [r[2] for r in zs_data]
    y = np.arange(len(names))
    from matplotlib.ticker import MaxNLocator
    fig, ax = plt.subplots(figsize=(6.5, 3.45))
    fig.subplots_adjust(left=0.175, right=0.975, top=0.760, bottom=0.135)
    ax.barh(y - 0.19, couv, height=0.36, color=_c(D.NAVY_L), label="Couverture en CAC (%)")
    ax.barh(y + 0.19, fonc, height=0.36, color=_c(D.TEAL),
            label="Réunions mensuelles tenues en 2021 (%)")
    ax.set_yticks(y); ax.set_yticklabels(names, fontsize=6.8)
    ax.invert_yaxis()
    ax.set_xlim(0, 108)
    ax.set_xlabel("%", fontsize=6.2, color=_c(D.GREY_MID))
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(_c(D.GREY_LN))
    ax.tick_params(axis="y", length=0, colors=_c(D.GREY_TXT))
    ax.tick_params(axis="x", labelsize=6.2, colors=_c(D.GREY_MID), length=2)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.legend(fontsize=6.0, frameon=False, loc="lower left",
              bbox_to_anchor=(0.0, 1.015), ncol=2, handlelength=1.4, borderaxespad=0.)
    fig.text(0.012, 0.975, "Couverture en CAC et fonctionnalité par zone de santé",
             fontsize=7.4, color=_c(D.NAVY), fontweight="bold", va="top")
    fig.text(0.012, 0.935, "DPS Kwilu 2021 / DHIS2, cité par Tech-4 (10 ZS ciblées)",
             fontsize=6.0, color=_c(D.GREY_MID), va="top", style="italic")
    _save(fig, path)


# ======================================================================
# 7. Chaîne de valeur des données
# ======================================================================
def fig_chaine_donnees(path):
    fig, ax = _canvas(1.85)
    etapes = [
        ("COLLECTE", "RECO · FOSA\nregistres papier\net électroniques"),
        ("TRANSMISSION", "CAC · CODESA\nBCZS · DHIS2"),
        ("VALIDATION", "ECZS · DPS\nPRONANUT"),
        ("ANALYSE", "Responsable\nS&E / HMIS"),
        ("UTILISATION", "Revues · MAA\nCPP · UG-PDSS"),
    ]
    x, w = 0.004, 0.176
    for i, (t, s) in enumerate(etapes):
        fc = _c(D.NAVY_L) if i < 4 else _c(D.GOLD)
        _box(ax, x, 0.620, w, 0.320, "", fc, ec=fc, radius=0.010)
        ax.text(x + w / 2, 0.900, t, ha="center", va="top", fontsize=5.6,
                color="#FFFFFF", fontweight="bold", zorder=3)
        ax.text(x + w / 2, 0.832, s, ha="center", va="top", fontsize=4.9,
                color="#FFFFFF", zorder=3, linespacing=1.65)
        if i < 4:
            _arrow(ax, x + w + 0.001, 0.780, x + w + 0.020, 0.780,
                   color=_c(D.TEAL), lw=1.1, ms=7)
        x += 0.196

    _box(ax, 0.004, 0.455, 0.992, 0.120, "", _c(D.GREY_BG), ec=_c(D.GREY_LN), radius=0.010)
    ax.text(0.016, 0.552,
            "Contrôles de qualité à chaque étape : complétude · promptitude · cohérence · exactitude "
            "(triade retenue par Tech-4, §RI 4.5)",
            ha="left", va="top", fontsize=5.5, color=_c(D.GREY_TXT))

    _box(ax, 0.004, 0.030, 0.992, 0.375, "", _c(D.TEAL_L), ec=_c(D.TEAL), radius=0.010)
    ax.text(0.016, 0.375, "DISPOSITIFS DE CONTRÔLE", ha="left", va="top",
            fontsize=5.8, color=_c(D.NAVY), fontweight="bold")
    ax.text(0.016, 0.310,
            "Audits de qualité des données lors des sessions de MAA (trimestrielles) · Third Party Monitoring (TPM) ponctuel\n"
            "Supervisions formatives mensuelles · Revues semestrielles de la nutrition sous la direction du Gouverneur et du\n"
            "Ministre provincial de la Santé · Bulletins trimestriels de la DPS",
            ha="left", va="top", fontsize=5.2, color=_c(D.GREY_TXT), linespacing=1.85)
    _save(fig, path)


def build_all(counts, zs_data):
    paths = {}
    for key, fn, args in [("theorie", fig_theorie_changement, ()),
                          ("edo", fig_edo, ()),
                          ("dispositif", fig_dispositif, ()),
                          ("repartition", fig_indic_repartition, (counts,)),
                          ("couverture", fig_couverture_fosa, ()),
                          ("cac", fig_cac, (zs_data,)),
                          ("chaine", fig_chaine_donnees, ())]:
        p = os.path.join(OUT, "fig_%s.png" % key)
        fn(p, *args)
        paths[key] = p
    return paths


if __name__ == "__main__":
    zs = [("Djuma", 100, 75.9), ("Gungu", 67, 37.4), ("Kikwit Nord", 9, 45.5),
          ("Kimputu", 98, 71.5), ("Kingandu", 100, 51.6), ("Moanza", 99, 49.4),
          ("Mosango", 92, 26.7), ("Pay Kongila", 98, 33.2), ("Sia", 98, 34.4),
          ("Yasa Bonga", 96, 94.4)]
    build_all({"Impact": 2, "Effet": 19, "Extrant": 16, "Réalisation": 4}, zs)
    print("figures ok")


# ======================================================================
# 8. Calendriers de type Gantt (2027 et 2028)
# ======================================================================
PHASE_COLORS = {
    "collecte":  ("#1B5E88", "Collecte des données"),
    "qualite":   ("#17868C", "Contrôle qualité"),
    "analyse":   ("#7FB8BC", "Analyse des données"),
    "rapports":  ("#B7873C", "Production des rapports"),
    "revues":    ("#5A6E7F", "Revues de performance"),
    "evaluation": ("#9B2226", "Évaluations"),
    "capital":   ("#2A6F4F", "Capitalisation et apprentissage"),
}


def fig_gantt(path, year, rows):
    """rows : liste de (libelle, phase, [mois 1..12 en 0/1], marqueur source)"""
    n = len(rows)
    rowh = 0.200
    header_in = 0.34
    legend_in = 0.66
    title_in = 0.34
    fig_h = title_in + header_in + n * rowh + legend_in
    fig = plt.figure(figsize=(FIGW, fig_h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    x_lab = 0.006
    w_lab = 0.324
    x_src = 0.358
    x_grid = 0.388
    w_grid = 0.994 - x_grid
    cw = w_grid / 12.0

    top = 1.0 - title_in / fig_h
    ax.text(0.004, 0.996, "Calendrier opérationnel du suivi-évaluation — exercice %d" % year,
            ha="left", va="top", fontsize=7.8, color=_c(D.NAVY), fontweight="bold")

    months = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
    hh = header_in / fig_h
    yh = top - hh
    ax.add_patch(plt.Rectangle((x_lab, yh), 1 - x_lab - 0.004, hh,
                               facecolor=_c(D.GREY_BG), edgecolor="none", zorder=1))
    ax.text(x_lab + 0.006, yh + hh / 2, "ACTIVITÉS DE SUIVI-ÉVALUATION",
            ha="left", va="center", fontsize=5.6, color=_c(D.NAVY), fontweight="bold")
    ax.text(x_src + 0.012, yh + hh / 2, "SOURC.", ha="center", va="center",
            fontsize=4.6, color=_c(D.NAVY), fontweight="bold")
    for i, m in enumerate(months):
        ax.text(x_grid + cw * (i + 0.5), yh + hh / 2, m,
                ha="center", va="center", fontsize=5.8, color=_c(D.NAVY), fontweight="bold")
        ax.plot([x_grid + cw * i, x_grid + cw * i], [yh, top - 0.003],
                color="#FFFFFF", lw=0.6, zorder=3)

    y = yh
    for j, (label, phase, months_on, src) in enumerate(rows):
        h = rowh / fig_h
        y -= h
        if j % 2 == 0:
            ax.add_patch(plt.Rectangle((x_lab, y), 1 - x_lab - 0.004, h,
                                       facecolor="#F7F9FA", edgecolor="none", zorder=0))
        maxch = int(((x_src - x_lab - 0.014) * FIGW) / (5.05 * 0.468 / 72.0))
        lab = label if len(label) <= maxch else label[:maxch - 1].rstrip(" ,;:") + "…"
        ax.text(x_lab + 0.006, y + h / 2, lab, ha="left", va="center",
                fontsize=5.05, color=_c(D.GREY_TXT), zorder=3)
        ax.text(x_src + 0.012, y + h / 2, src, ha="center", va="center",
                fontsize=4.5, color=_c(D.TEAL) if src == "T4" else _c(D.GOLD),
                fontweight="bold", zorder=3)
        ax.plot([x_lab, 1 - 0.004], [y, y], color="#E3E9ED", lw=0.4, zorder=1)
        col = PHASE_COLORS[phase][0]
        for i in range(12):
            ax.plot([x_grid + cw * i, x_grid + cw * i], [y, y + h],
                    color="#EDF1F4", lw=0.4, zorder=1)
            if months_on[i]:
                ax.add_patch(plt.Rectangle((x_grid + cw * i + cw * 0.11, y + h * 0.26),
                                           cw * 0.78, h * 0.48,
                                           facecolor=col, edgecolor="none", zorder=3))

    # ---- légende (deux lignes)
    keys = list(PHASE_COLORS.keys())
    rows_leg = [keys[:4], keys[4:]]
    def dy(inches):
        return inches / fig_h
    for r, group in enumerate(rows_leg):
        x = x_lab + 0.002
        yy = y - dy(0.16) - r * dy(0.135)
        for k in group:
            col, lab = PHASE_COLORS[k]
            hb = dy(0.075)
            ax.add_patch(plt.Rectangle((x, yy - hb / 2), 0.011, hb,
                                       facecolor=col, edgecolor="none", zorder=3))
            ax.text(x + 0.016, yy, lab, ha="left", va="center", fontsize=4.85,
                    color=_c(D.GREY_TXT))
            x += 0.016 + len(lab) * 0.00505 + 0.022
    ax.text(x_lab + 0.002, y - dy(0.16) - 2 * dy(0.135) - dy(0.02),
            "T4 = calendrier directement issu de Tech-4     ·     R = proposition méthodologique soumise à validation",
            ha="left", va="top", fontsize=4.7, color=_c(D.GREY_MID), style="italic")
    _save(fig, path)


# ======================================================================
# 9. Couverture (image pleine page partagée par le PDF et le DOCX)
# ======================================================================
def fig_cover(path, meta, w_in, h_in):
    """Couverture pleine page en coordonnées pouces (identique PDF / DOCX)."""
    fig = plt.figure(figsize=(w_in, h_in))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w_in); ax.set_ylim(0, h_in); ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0), w_in, h_in, facecolor=_c(D.NAVY_D),
                               edgecolor="none", zorder=0))
    for r, a in ((2.55, 0.13), (1.95, 0.10), (1.35, 0.09)):
        ax.add_patch(plt.Circle((w_in + 0.45, h_in - 1.55), r, facecolor=_c(D.NAVY_L),
                                alpha=a, edgecolor="none", zorder=1))
    ax.add_patch(plt.Rectangle((0, h_in - 0.085), w_in, 0.085,
                               facecolor=_c(D.TEAL), edgecolor="none", zorder=4))

    X = 0.72
    ax.text(X, h_in - 0.92, meta.get("cover_kicker", "").upper(), ha="left", va="center",
            fontsize=8.4, color=_c(D.TEAL_M), fontweight="bold")
    ax.plot([X, X + 0.92], [h_in - 1.24, h_in - 1.24], color=_c(D.GOLD), lw=2.6,
            solid_capstyle="butt")

    org = meta.get("cover_org", [])
    if org:
        ax.text(X, h_in - 1.60, org[0], ha="left", va="center", fontsize=9.8,
                color="#FFFFFF", fontweight="bold")
    for i, line in enumerate(org[1:]):
        ax.text(X, h_in - 1.88 - i * 0.26, line, ha="left", va="center", fontsize=9.4,
                color=_c(D.TEAL_M))

    ax.text(X, h_in - 3.02, meta.get("cover_title", "PLAN DE SUIVI-ÉVALUATION"), ha="left",
            va="center", fontsize=21.5, color="#FFFFFF", fontweight="bold")
    ax.text(X, h_in - 3.62, meta.get("cover_year", "2027 – 2028"), ha="left", va="center",
            fontsize=21.5, color=_c(D.TEAL_M), fontweight="bold")
    y = h_in - 4.22
    for line in meta.get("cover_sub", []):
        ax.text(X, y, line, ha="left", va="center", fontsize=9.6, color="#DDE7EC")
        y -= 0.30

    bx, btop, bw, bh = X, h_in - 4.95, 6.82, 2.62
    by = btop - bh
    ax.add_patch(plt.Rectangle((bx, by), bw, bh, facecolor="#12496B", edgecolor="none",
                               zorder=2))
    ax.text(bx + 0.26, btop - 0.30, "PROJET DE RÉFÉRENCE", ha="left", va="center",
            fontsize=7.2, color=_c(D.TEAL_M), fontweight="bold")
    yy = btop - 0.62
    for i, line in enumerate(meta.get("cover_projet", [])):
        ax.text(bx + 0.26, yy, line, ha="left", va="center",
                fontsize=11.2 if i < 2 else 8.0,
                color="#FFFFFF" if i < 2 else "#CFE0E8",
                fontweight="bold" if i < 2 else "normal")
        yy -= 0.30 if i < 2 else 0.24
    yy -= 0.10
    for line in meta.get("cover_source", []):
        ax.text(bx + 0.26, yy, line, ha="left", va="center", fontsize=7.5, color="#BCD3DE")
        yy -= 0.24

    ax.text(X, 2.62, meta.get("cover_periode", ""), ha="left", va="center", fontsize=9.0,
            color="#DDE7EC")
    ax.text(X, 2.32, meta.get("cover_version", ""), ha="left", va="center", fontsize=8.6,
            color=_c(D.TEAL_M))
    ax.plot([X, w_in - 0.72], [2.02, 2.02], color="#2F5F79", lw=0.9)
    yy = 1.74
    for line in meta.get("cover_footer", []):
        ax.text(X, yy, line, ha="left", va="center", fontsize=6.9, color="#A8C2D0",
                style="italic")
        yy -= 0.24
    _save(fig, path)
