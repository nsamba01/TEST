# -*- coding: utf-8 -*-
"""Point d'entrée : génère les deux livrables en DOCX et en PDF."""
import os
import sys
import diagrams
import render
import data as D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables")
os.makedirs(OUT, exist_ok=True)


def resolve_images(blocks, assets):
    for b in blocks:
        if b["t"] == "img":
            a = assets[b["key"]]
            b["path"] = a["path"]
            b["w_cm"] = a["w_cm"]
            b["h_cm"] = a["h_cm"]
    return blocks


def main(which=None):
    assets = diagrams.build_all()
    print("diagrammes :", ", ".join(assets))

    if which in (None, "l1"):
        import l1
        blocks = resolve_images(l1.blocks(), assets)
        base = "Plan_Suivi-Evaluation_2027-2028_Techn4_Kwilu"
        header = "Plan de Suivi-Évaluation 2027-2028 — Services NAC · Kwilu"
        render.render_docx(blocks, os.path.join(OUT, base + ".docx"), header, D.__dict__.get("FOOTER", "Plan S&E – Tech-4 | 2027-2028"), "Plan de Suivi-Évaluation 2027-2028 — Services NAC, Kwilu")
        print("DOCX L1 OK")
        render.render_pdf(blocks, os.path.join(OUT, base + ".pdf"), header, "Plan S&E – Tech-4 | 2027-2028", "Plan de Suivi-Évaluation 2027-2028 — Services NAC, Kwilu")
        print("PDF L1 OK")

    if which in (None, "l2"):
        import l2
        blocks = resolve_images(l2.blocks(), assets)
        base = "Cadre_de_Performance_2027-2028_Techn4_Kwilu"
        header = "Cadre de Performance 2027-2028 — Services NAC · Kwilu"
        render.render_docx(blocks, os.path.join(OUT, base + ".docx"), header, "Cadre de performance – Tech-4 | 2027-2028", "Cadre de Performance 2027-2028 — Services NAC, Kwilu")
        print("DOCX L2 OK")
        render.render_pdf(blocks, os.path.join(OUT, base + ".pdf"), header, "Cadre de performance – Tech-4 | 2027-2028", "Cadre de Performance 2027-2028 — Services NAC, Kwilu")
        print("PDF L2 OK")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
