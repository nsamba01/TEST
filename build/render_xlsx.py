# -*- coding: utf-8 -*-
"""Rendu XLSX — classeur du cadre de performance (livrable 03).

Même source de données que les livrables 01, 02 et 04 (data.py), donc valeurs
strictement identiques. Mise en forme professionnelle : en-têtes figés et
filtrés, volets figés, largeurs ajustées, renvoi à la ligne, code couleur de
traçabilité, mise en forme conditionnelle des cellules « À préciser ».
"""
import re
from collections import Counter

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import design as D
import data as T

NAVY = D.NAVY
TEAL = D.TEAL
GOLD = D.GOLD
GREY_BG = D.GREY_BG
GREY_LN = D.GREY_LN
RED = D.RED

F_TITLE = Font(name=D.FONT, size=16, bold=True, color=NAVY)
F_SUB = Font(name=D.FONT, size=9.5, italic=True, color=D.GREY_MID)
F_HEAD = Font(name=D.FONT, size=8.5, bold=True, color="FFFFFF")
F_CELL = Font(name=D.FONT, size=8.5, color=D.GREY_TXT)
F_CELL_B = Font(name=D.FONT, size=8.5, bold=True, color=D.GREY_TXT)
F_NA = Font(name=D.FONT, size=8.5, italic=True, color=RED)
F_KPI = Font(name=D.FONT, size=20, bold=True, color=NAVY)

FILL_HEAD = PatternFill("solid", fgColor=NAVY)
FILL_ZEBRA = PatternFill("solid", fgColor=GREY_BG)
FILL_LVL = PatternFill("solid", fgColor="E6ECF0")

THIN = Side(style="thin", color=GREY_LN)
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

WRAP = Alignment(wrap_text=True, vertical="top", horizontal="left")
CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")


def _formule(t):
    t = _strip(t)
    i = t.find("Numérateur :")
    return t[:i].rstrip(" ;,") if i > 0 else t


def _strip(t):
    return re.sub(r"<[^>]+>", "", str(t)).replace("&nbsp;", " ").strip()


def _sheet_title(ws, title, subtitle, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=title)
    c.font = F_TITLE
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 26
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c = ws.cell(row=2, column=1, value=subtitle)
    c.font = F_SUB
    c.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[2].height = 24


def _header(ws, row, headers):
    for i, h in enumerate(headers, 1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    ws.row_dimensions[row].height = 34


def _widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def _na_rule(ws, rng):
    ws.conditional_formatting.add(
        rng, FormulaRule(formula=['ISNUMBER(SEARCH("préciser",%s))' % rng.split(":")[0]],
                         font=Font(name=D.FONT, size=8.5, italic=True, color=RED),
                         fill=PatternFill("solid", fgColor="F8EDED"), stopIfTrue=False))


# --------------------------------------------------------------------------
def build_xlsx(path):
    wb = Workbook()

    ws = wb.active
    ws.title = "Lecture"
    _lecture(ws)

    _cadre(wb.create_sheet("Cadre de performance"))
    _suivi(wb.create_sheet("Suivi annuel"))
    _fiches(wb.create_sheet("Fiches techniques"))
    _synthese(wb.create_sheet("Synthèse"))
    _contexte(wb.create_sheet("Données de contexte"))
    _tracabilite(wb.create_sheet("Traçabilité"))

    wb.save(path)
    return path


# --------------------------------------------------------------------------
def _lecture(ws):
    ws.sheet_view.showGridLines = False
    _widths(ws, [3, 34, 62, 30])
    _sheet_title(ws, "CADRE DE PERFORMANCE 2027–2028",
                 "Projet Multisectoriel de Nutrition et de Santé — volet Nutrition à Assise Communautaire "
                 "(PMNS-NAC), province du Kwilu · Consortium SANRU-ICHESS-FONLIV-FDSS · "
                 "DP N° ZR-DRC-MSP-235334-CS-QCBS", 4)
    r = 4
    ws.cell(row=r, column=2, value="Document source").font = F_CELL_B
    ws.cell(row=r, column=3,
            value="Tech-4 — « Description de l’approche, de la méthodologie et du programme de travail »"
            ).font = F_CELL
    r += 1
    ws.cell(row=r, column=2, value="Période couverte").font = F_CELL_B
    ws.cell(row=r, column=3, value="Année 1 : 1ᵉʳ janvier – 31 décembre 2027 · "
                                   "Année 2 : 1ᵉʳ janvier – 31 décembre 2028").font = F_CELL
    r += 1
    ws.cell(row=r, column=2, value="Version").font = F_CELL_B
    ws.cell(row=r, column=3, value="1.0 — document de travail soumis à validation").font = F_CELL
    r += 2

    heads = ["Onglet", "Contenu", "Usage"]
    for i, h in enumerate(heads, 2):
        c = ws.cell(row=r, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    r += 1
    tabs = [
        ("Cadre de performance", "Les 41 indicateurs et les 14 colonnes du cadre de performance",
         "Consultation, filtrage par niveau, objectif ou fréquence"),
        ("Suivi annuel", "Grille de saisie des réalisations 2027 et 2028",
         "Saisie périodique ; aucune colonne de réalisation n’est préremplie"),
        ("Fiches techniques", "Une ligne par indicateur, toutes les rubriques de la fiche",
         "Vérification des définitions, formules et responsabilités"),
        ("Synthèse", "Dénombrement des indicateurs par niveau et par objectif", "Lecture de synthèse"),
        ("Données de contexte", "Valeurs provinciales et nationales citées par Tech-4",
         "Contexte documenté — ne constitue pas une valeur de référence du projet"),
        ("Traçabilité", "Correspondance entre chaque indicateur et le passage de Tech-4",
         "Contrôle de fidélité documentaire"),
    ]
    for name, cont, use in tabs:
        ws.cell(row=r, column=2, value=name).font = F_CELL_B
        c = ws.cell(row=r, column=3, value=cont)
        c.font = F_CELL
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c2 = ws.cell(row=r, column=4, value=use)
        c2.font = F_CELL
        c2.alignment = Alignment(wrap_text=True, vertical="top")
        for col in (2, 3, 4):
            ws.cell(row=r, column=col).border = BORDER
        ws.row_dimensions[r].height = 30
        r += 1

    r += 2
    ws.cell(row=r, column=2, value="Conventions de lecture").font = Font(
        name=D.FONT, size=11, bold=True, color=NAVY)
    r += 1
    conv = [
        ("Caractères normaux", "Valeur explicitement documentée par Tech-4.", D.GREY_TXT, False),
        ("À préciser", "Information absente du document source — à produire (évaluation de base, "
                       "atelier de validation des cibles).", RED, True),
        ("Cible globale", "Volume fixé par Tech-4 pour toute la durée du projet ; il ne s’agit pas "
                          "d’une cible annuelle.", D.GREY_TXT, False),
        ("Recommandation", "Proposition méthodologique soumise à validation ; elle n’engage pas le projet.",
         GOLD, True),
    ]
    for lab, desc, col, ital in conv:
        c = ws.cell(row=r, column=2, value=lab)
        c.font = Font(name=D.FONT, size=9, bold=True, color=col, italic=ital)
        c.border = BORDER
        c2 = ws.cell(row=r, column=3, value=desc)
        c2.font = F_CELL
        c2.alignment = Alignment(wrap_text=True, vertical="top")
        c2.border = BORDER
        ws.row_dimensions[r].height = 26
        r += 1

    r += 2
    ws.cell(row=r, column=2,
            value="Aucune valeur de référence ni aucune cible annuelle n’a été inventée. "
                  "Les cellules en rouge italique signalent une information manquante dans le document source."
            ).font = F_SUB


# --------------------------------------------------------------------------
def _cadre(ws):
    ws.sheet_view.showGridLines = False
    headers = ["Niveau de résultat", "Objectif / résultat attendu", "Code", "Indicateur", "Définition",
               "Mode de calcul (formule)", "Numérateur", "Dénominateur", "Unité",
               "Situation de référence", "Cible 2027", "Cible 2028", "Cible globale Tech-4",
               "Source de vérification", "Méthode de collecte", "Fréquence", "Responsable de collecte",
               "Responsable de validation", "Hypothèses et risques", "Source dans Tech-4"]
    widths = [11, 30, 8, 34, 40, 40, 24, 24, 11, 40, 10, 10, 34, 32, 32, 16, 20, 22, 32, 22]
    _widths(ws, widths)
    _sheet_title(ws, "Cadre de performance 2027–2028 — tableau principal",
                 "41 indicateurs · 14 colonnes de suivi + 5 colonnes de traçabilité · "
                 "Aucune cible annuelle n’est documentée dans Tech-4 : les colonnes 2027 et 2028 sont « À préciser ».",
                 len(headers))
    hr = 4
    _header(ws, hr, headers)
    r = hr + 1
    for i in T.INDICATEURS:
        vals = [i["niveau"], "%s — %s" % (i["obj_c"], _strip(i["resultat"])), i["code"], i["intitule"],
                i["definition"], _formule(i["formule"]), i["numerateur"], i["denominateur"], i["unite"],
                i["ref"], i["c27"], i["c28"], i.get("cible_globale") or T.NA,
                i["sv"], i["methode"], i["frequence"], i["r_collecte"], i["r_valid"],
                i.get("hypotheses") or T.NA, i["src"]]
        for ci, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=ci, value=_strip(v))
            c.font = F_CELL
            c.alignment = WRAP
            c.border = BORDER
            if r % 2 == 0:
                c.fill = FILL_ZEBRA
            if ci == 1:
                c.fill = FILL_LVL
                c.font = F_CELL_B
            if ci == 3:
                c.font = F_CELL_B
        ws.row_dimensions[r].height = 46
        r += 1

    ws.freeze_panes = "D5"
    ws.auto_filter.ref = "A%d:T%d" % (hr, r - 1)
    for col in ("J", "K", "L", "M", "S"):
        _na_rule(ws, "%s5:%s%d" % (col, col, r - 1))
    ws.print_title_rows = "4:4"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True


# --------------------------------------------------------------------------
def _suivi(ws):
    ws.sheet_view.showGridLines = False
    headers = ["Code", "Indicateur", "Unité", "Référence", "Cible 2027", "Réalisation 2027",
               "Écart 2027", "Cible 2028", "Réalisation 2028", "Écart 2028",
               "Commentaire et analyse des écarts", "Responsable de collecte", "Fréquence"]
    widths = [9, 46, 12, 40, 12, 14, 12, 12, 14, 12, 46, 24, 18]
    _widths(ws, widths)
    _sheet_title(ws, "Suivi annuel de la performance — grille de saisie",
                 "Les colonnes « Réalisation » et « Écart » sont volontairement vides. "
                 "Aucun taux d’atteinte n’est calculé : les cibles annuelles ne sont pas encore arrêtées.",
                 len(headers))
    hr = 4
    _header(ws, hr, headers)
    r = hr + 1
    for i in T.INDICATEURS:
        vals = [i["code"], i["intitule"], i["unite"], _strip(i["ref"]), _strip(i["c27"]), None, None,
                _strip(i["c28"]), None, None, None, i["r_collecte"], _strip(i["frequence"])]
        for ci, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=ci, value=v)
            c.font = F_CELL
            c.alignment = WRAP
            c.border = BORDER
            if r % 2 == 0:
                c.fill = FILL_ZEBRA
            if ci == 1:
                c.font = F_CELL_B
            if ci in (6, 9):
                c.fill = PatternFill("solid", fgColor="FFFDF5")
        ws.row_dimensions[r].height = 30
        r += 1

    ws.freeze_panes = "C5"
    ws.auto_filter.ref = "A%d:M%d" % (hr, r - 1)
    for col in ("D", "E", "H"):
        _na_rule(ws, "%s5:%s%d" % (col, col, r - 1))
    ws.print_title_rows = "4:4"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True


# --------------------------------------------------------------------------
def _fiches(ws):
    ws.sheet_view.showGridLines = False
    headers = ["Code", "Intitulé", "Niveau de résultat", "Objectif de rattachement", "Résultat attendu",
               "Définition", "Justification", "Unité", "Numérateur", "Dénominateur", "Formule",
               "Désagrégations", "Situation de référence", "Source de la référence", "Cible 2027",
               "Cible 2028", "Cible globale Tech-4", "Source de vérification", "Méthode de collecte",
               "Fréquence", "Responsable de collecte", "Responsable de validation",
               "Limites et biais connus", "Hypothèses et risques"]
    widths = [9, 40, 12, 30, 34, 44, 34, 11, 26, 26, 40, 26, 40, 22, 10, 10, 32, 34, 32,
              16, 20, 22, 40, 32]
    _widths(ws, widths)
    _sheet_title(ws, "Fiches techniques des 41 indicateurs",
                 "Une ligne par indicateur : définition, justification, mesure, référence, cibles, "
                 "responsabilités, limites et hypothèses. Mêmes rubriques que les fiches du livrable 04.",
                 len(headers))
    hr = 4
    _header(ws, hr, headers)
    r = hr + 1
    for i in T.INDICATEURS:
        vals = [i["code"], i["intitule"], i["niveau"], i["objectif"], _strip(i["resultat"]),
                i["definition"], i["justification"], i["unite"], i["numerateur"], i["denominateur"],
                _formule(i["formule"]), i["desagr"], _strip(i["ref"]), i["src"], _strip(i["c27"]),
                _strip(i["c28"]), i.get("cible_globale") or T.NA, i["sv"], i["methode"],
                _strip(i["frequence"]), i["r_collecte"], i["r_valid"], i["limites"],
                i.get("hypotheses") or T.NA]
        for ci, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=ci, value=_strip(v))
            c.font = F_CELL
            c.alignment = WRAP
            c.border = BORDER
            if r % 2 == 0:
                c.fill = FILL_ZEBRA
            if ci == 1:
                c.font = F_CELL_B
        ws.row_dimensions[r].height = 58
        r += 1
    ws.freeze_panes = "C5"
    ws.auto_filter.ref = "A%d:X%d" % (hr, r - 1)
    for col in ("M", "O", "P", "Q"):
        _na_rule(ws, "%s5:%s%d" % (col, col, r - 1))
    ws.print_title_rows = "4:4"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True


# --------------------------------------------------------------------------
def _synthese(ws):
    ws.sheet_view.showGridLines = False
    _widths(ws, [3, 34, 12, 12, 12, 12, 12, 12])
    _sheet_title(ws, "Synthèse du cadre de performance",
                 "Dénombrement des indicateurs par niveau de résultat et par objectif.", 7)
    r = 4
    heads = ["", "Niveau / objectif", "Impact", "Effet", "Extrant", "Réalisation", "Total"]
    for i, h in enumerate(heads, 2):
        c = ws.cell(row=r, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    r += 1

    by_lvl_start = r
    tot = Counter(i["niveau"] for i in T.INDICATEURS)
    for lvl in ("Impact", "Effet", "Extrant", "Réalisation"):
        ws.cell(row=r, column=2, value=lvl).font = F_CELL_B
        ws.cell(row=r, column=2).border = BORDER
        col = {"Impact": 3, "Effet": 4, "Extrant": 5, "Réalisation": 6}[lvl]
        c = ws.cell(row=r, column=col, value=tot.get(lvl, 0))
        c.font = F_CELL
        c.alignment = CENTER
        c.border = BORDER
        ws.cell(row=r, column=7, value=tot.get(lvl, 0)).font = F_CELL_B
        ws.cell(row=r, column=7).border = BORDER
        ws.cell(row=r, column=7).alignment = CENTER
        r += 1

    r += 2
    heads2 = ["", "Objectif", "Impact", "Effet", "Extrant", "Réalisation", "Total"]
    for i, h in enumerate(heads2, 2):
        c = ws.cell(row=r, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    r += 1
    labels = {"OG": "Objectif global", "OS1": "OS1 — Sites communautaires et NAC",
              "OS2": "OS2 — VBG et prise en charge des victimes",
              "OS3": "OS3 — Structures de participation communautaire",
              "OS4": "OS4 — Appui au système de santé",
              "OS5": "RI 4.5 — Suivi-évaluation et apprentissage"}
    by_obj_start = r
    for code in ["OG", "OS1", "OS2", "OS3", "OS4", "OS5"]:
        sub = [i for i in T.INDICATEURS if i["obj_c"] == code]
        c = Counter(i["niveau"] for i in sub)
        ws.cell(row=r, column=2, value=labels[code]).font = F_CELL
        ws.cell(row=r, column=2).border = BORDER
        for col, lvl in ((3, "Impact"), (4, "Effet"), (5, "Extrant"), (6, "Réalisation")):
            cc = ws.cell(row=r, column=col, value=c.get(lvl, 0))
            cc.font = F_CELL
            cc.alignment = CENTER
            cc.border = BORDER
        cc = ws.cell(row=r, column=7, value=len(sub))
        cc.font = F_CELL_B
        cc.alignment = CENTER
        cc.border = BORDER
        r += 1

    ch = BarChart()
    ch.type = "col"
    ch.style = 10
    ch.title = "Indicateurs par niveau de résultat"
    ch.y_axis.title = "Nombre d’indicateurs"
    data = Reference(ws, min_col=3, max_col=6, min_row=by_lvl_start - 1, max_row=by_lvl_start + 3)
    ch.add_data(data, titles_from_data=False)
    ch.height, ch.width = 7.5, 16
    ch.legend = None
    ws.add_chart(ch, "I4")


# --------------------------------------------------------------------------
def _contexte(ws):
    ws.sheet_view.showGridLines = False
    rows = [
        ("Retard de croissance, enfants de moins de 5 ans (Kwilu)", "47 %", "MICS-Palu 2017-2018 / MICS 6"),
        ("Retard de croissance, enfants de moins de 5 ans (national)", "42 %", "MICS 2017-2018"),
        ("Insuffisance pondérale, enfants de moins de 5 ans (Kwilu)", "34,8 %", "MICS 2017-2018"),
        ("Allaitement maternel exclusif (Kwilu)", "32,7 %", "MICS 2017-2018"),
        ("Allaitement maternel exclusif (national)", "53,5 %", "MICS 2017-2018"),
        ("Initiation précoce de l’allaitement (Kwilu)", "29,2 %", "MICS 2017-2018"),
        ("Alimentation de complément adéquate (Kwilu)", "18 %", "MICS 2017-2018"),
        ("Diversité alimentaire minimale (Kwilu)", "27,1 %", "MICS 2017-2018"),
        ("Fréquence minimale des repas (Kwilu)", "47 %", "MICS 2017-2018"),
        ("Lavage des mains aux moments critiques (Kwilu)", "18 %", "MICS 2017-2018"),
        ("Quatre consultations prénatales ou plus (Kwilu)", "24,3 %", "MICS 2017-2018"),
        ("Consultation préscolaire redynamisée (Kwilu)", "47,1 %", "PRONANUT Kwilu, rapport annuel 2020"),
        ("ANJE (Kwilu)", "50 %", "PRONANUT Kwilu, rapport annuel 2020"),
        ("PCIMA et NAC (Kwilu)", "0 %", "PRONANUT Kwilu, rapport annuel 2020"),
        ("Réunions mensuelles des CAC tenues", "53,6 % (2 250 sur 3 188)", "DHIS2 2021"),
        ("Couverture des CAC installés", "71 %", "DPS Kwilu 2021"),
        ("Plans d’action communautaire (PAC)",
         "16 %", "Plan stratégique national de santé communautaire 2019-2022"),
        ("Insécurité alimentaire sévère (Kwilu)", "49,9 %", "IPC 2021-2022"),
        ("Insécurité alimentaire sévère (national)", "43,7 %", "IPC 2021-2022"),
        ("Cas de VBG déclarés (Kwilu)", "366 cas, 0,49 % ; 41 % ont moins de 18 ans",
         "DHIS2 2021 / sous-cluster VBG"),
        ("Personnel de santé formé au PCIMA", "27 %", "PNDS recadré 2019-2022"),
    ]
    _widths(ws, [5, 52, 34, 40])
    _sheet_title(ws, "Données de contexte citées par Tech-4",
                 "Ces valeurs sont des données provinciales ou nationales. Elles ne constituent pas des valeurs "
                 "de référence du projet et ne sont jamais utilisées comme cible.", 4)
    hr = 4
    for i, h in enumerate(["", "Indicateur de contexte", "Valeur", "Source citée par Tech-4"], 2):
        c = ws.cell(row=hr, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    r = hr + 1
    for i, (lab, val, src) in enumerate(rows):
        for ci, v in ((2, lab), (3, val), (4, src)):
            c = ws.cell(row=r, column=ci, value=v)
            c.font = F_CELL
            c.alignment = WRAP
            c.border = BORDER
            if r % 2 == 0:
                c.fill = FILL_ZEBRA
        ws.row_dimensions[r].height = 22
        r += 1
    ws.freeze_panes = "C5"
    ws.auto_filter.ref = "B%d:D%d" % (hr, r - 1)


# --------------------------------------------------------------------------
def _tracabilite(ws):
    ws.sheet_view.showGridLines = False
    _widths(ws, [10, 50, 12, 32, 30, 12])
    _sheet_title(ws, "Traçabilité documentaire des indicateurs",
                 "Correspondance entre chaque indicateur et le passage du document source dont il est issu.",
                 6)
    hr = 4
    for i, h in enumerate(["Code", "Indicateur", "Niveau", "Source dans Tech-4", "Justification",
                           "Origine"], 1):
        c = ws.cell(row=hr, column=i, value=h)
        c.font = F_HEAD
        c.fill = FILL_HEAD
        c.alignment = CENTER
        c.border = BORDER
    r = hr + 1
    for i in T.INDICATEURS:
        orig = "Formulé dans Tech-4"
        j = i["justification"].lower()
        if "proposition" in j or "dérivé" in j:
            orig = "Dérivé / proposé"
        vals = [i["code"], i["intitule"], i["niveau"], i["src"], i["justification"], orig]
        for ci, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=ci, value=_strip(v))
            c.font = F_CELL
            c.alignment = WRAP
            c.border = BORDER
            if r % 2 == 0:
                c.fill = FILL_ZEBRA
            if ci == 1:
                c.font = F_CELL_B
            if ci == 6 and orig != "Formulé dans Tech-4":
                c.font = Font(name=D.FONT, size=8.5, italic=True, color=GOLD)
        ws.row_dimensions[r].height = 34
        r += 1
    ws.freeze_panes = "B5"
    ws.auto_filter.ref = "A%d:F%d" % (hr, r - 1)
    ws.print_title_rows = "4:4"
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
