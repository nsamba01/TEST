# -*- coding: utf-8 -*-
"""Vérification finale des cinq livrables."""
import os
import re
import sys
import zipfile

import pymupdf
from docx import Document
from openpyxl import load_workbook

import data as T

OUT = "/home/user/TEST/LIVRABLES_SUIVI_EVALUATION_2027_2028"
FILES = [
    "01_Plan_Suivi_Evaluation_2027_2028.docx",
    "02_Plan_Suivi_Evaluation_2027_2028.pdf",
    "03_Cadre_Performance_2027_2028.xlsx",
    "04_Cadre_Performance_2027_2028.pdf",
    "05_Rapport_Controle_Qualite.docx",
]
CODES = [i["code"] for i in T.INDICATEURS]
ok = True


def say(tag, msg):
    print("%-6s %s" % (tag, msg))


# 1. présence
for f in FILES:
    p = os.path.join(OUT, f)
    if not os.path.exists(p):
        say("FAIL", "absent : " + f)
        ok = False
    else:
        say("OK", "%-46s %8.1f Ko" % (f, os.path.getsize(p) / 1024))

# 2. PDF
for f in ("02_Plan_Suivi_Evaluation_2027_2028.pdf", "04_Cadre_Performance_2027_2028.pdf"):
    d = pymupdf.open(os.path.join(OUT, f))
    thin = [i + 1 for i in range(len(d)) if len(d[i].get_text().strip()) < 300]
    if thin:
        say("WARN", "%s pages quasi vides : %s" % (f, thin))
    # débordements
    bad = []
    for i, p in enumerate(d):
        w, h = p.rect.width, p.rect.height
        for b in p.get_text("blocks"):
            if b[0] < 18 or b[2] > w - 18 or b[1] < 14 or b[3] > h - 14:
                bad.append((i + 1, b[4][:40]))
    if bad:
        say("FAIL", "%s débordements : %s" % (f, bad[:5]))
        ok = False
    # polices
    fonts = set()
    for i in range(min(len(d), 12)):
        for fnt in d[i].get_fonts():
            fonts.add(fnt[3])
    # marqueurs de balisage résiduels
    txt = "".join(d[i].get_text() for i in range(len(d)))
    residue = re.findall(r"</?(?:b|i|font)\b", txt)
    if residue:
        say("FAIL", "%s balises résiduelles : %d" % (f, len(residue)))
        ok = False
    say("OK", "%-46s %d pages · polices %s" % (f, len(d), sorted(fonts)[:3]))

# 3. DOCX
for f in ("01_Plan_Suivi_Evaluation_2027_2028.docx", "05_Rapport_Controle_Qualite.docx"):
    p = os.path.join(OUT, f)
    z = zipfile.ZipFile(p)
    assert z.testzip() is None
    doc = Document(p)
    paras = [x.text for x in doc.paragraphs]
    residue = [x for x in paras if re.search(r"</?(?:b|i|font)\b|&nbsp;", x)]
    if residue:
        say("FAIL", "%s balises résiduelles : %s" % (f, residue[:2]))
        ok = False
    empty = sum(1 for x in paras if not x.strip())
    say("OK", "%-46s %d sections · %d tableaux · %d §  (%d vides)"
        % (f, len(doc.sections), len(doc.tables), len(paras), empty))
    land = sum(1 for s in doc.sections if s.page_width > s.page_height)
    say("INFO", "   sections paysage : %d" % land)

# 4. XLSX
wb = load_workbook(os.path.join(OUT, "03_Cadre_Performance_2027_2028.xlsx"))
say("OK", "%-46s %d onglets : %s" % ("03_Cadre_Performance_2027_2028.xlsx",
                                     len(wb.sheetnames), ", ".join(wb.sheetnames)))
ws = wb["Cadre de performance"]
rows = [r for r in ws.iter_rows(min_row=5, values_only=True) if r[2]]
say("OK", "   cadre : %d lignes d’indicateurs · filtre %s · volets %s"
    % (len(rows), ws.auto_filter.ref, ws.freeze_panes))
xl_codes = [r[2] for r in rows]
if xl_codes == CODES:
    say("OK", "   codes Excel identiques au référentiel (ordre inclus)")
else:
    say("FAIL", "   codes Excel divergents")
    ok = False
# aucune cible annuelle inventée
allowed = {i["code"]: (i["c27"], i["c28"]) for i in T.INDICATEURS}
bad_targets = []
for r in rows:
    c27, c28 = allowed[r[2]]
    if (r[10] or "") != str(c27) or (r[11] or "") != str(c28):
        bad_targets.append(r[2])
if bad_targets:
    say("FAIL", "   cibles annuelles divergentes du référentiel : %s" % bad_targets[:3])
    ok = False
else:
    documented = [c for c, (a, b) in allowed.items() if "préciser" not in (str(a) + str(b))]
    say("OK", "   cibles 2027/2028 identiques au référentiel · %d documentée(s) dans Tech-4 : %s"
        % (len(documented), ", ".join(documented) or "aucune"))
ws2 = wb["Suivi annuel"]
suivi = [r for r in ws2.iter_rows(min_row=5, values_only=True) if r[0]]
filled = [r[0] for r in suivi if r[5] or r[8]]
say("OK", "   suivi annuel : %d lignes · réalisations vides : %s"
    % (len(suivi), "oui" if not filled else "NON %s" % filled[:3]))

# 5. cohérence des codes dans les PDF
for f in ("02_Plan_Suivi_Evaluation_2027_2028.pdf", "04_Cadre_Performance_2027_2028.pdf"):
    d = pymupdf.open(os.path.join(OUT, f))
    txt = "".join(d[i].get_text() for i in range(len(d)))
    missing = [c for c in CODES if c not in txt]
    if missing:
        say("WARN", "%s codes absents : %s" % (f, missing))
    else:
        say("OK", "%s contient les 41 codes" % f)

# 6. mentions de traçabilité
for f in ("02_Plan_Suivi_Evaluation_2027_2028.pdf", "04_Cadre_Performance_2027_2028.pdf"):
    d = pymupdf.open(os.path.join(OUT, f))
    txt = "".join(d[i].get_text() for i in range(len(d)))
    n_na = txt.count("préciser")
    n_rec = txt.count("ecommandation")
    say("INFO", "%s : %d mentions « à préciser » · %d mentions « recommandation »"
        % (f, n_na, n_rec))

print("\nRÉSULTAT :", "CONFORME" if ok else "À CORRIGER")
sys.exit(0 if ok else 1)
