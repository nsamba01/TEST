# -*- coding: utf-8 -*-
"""Production des cinq livrables."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_plan
import doc_cadre
import doc_qc
import render_docx
import render_pdf
import render_xlsx

OUT = "/home/user/TEST/LIVRABLES_SUIVI_EVALUATION_2027_2028"
os.makedirs(OUT, exist_ok=True)


def run():
    t0 = time.time()
    jobs = [
        ("plan", content_plan.build, "01_Plan_Suivi_Evaluation_2027_2028", True, True),
        ("cadre", doc_cadre.build, "04_Cadre_Performance_2027_2028", False, True),
        ("qc", doc_qc.build, "05_Rapport_Controle_Qualite", True, False),
    ]
    for name, builder, base, want_docx, want_pdf in jobs:
        doc = builder()
        pages = None
        if want_pdf:
            pages = render_pdf.build_pdf(doc, os.path.join(OUT, base + ".pdf"))
            print("PDF  ", base + ".pdf")
        if want_docx:
            render_docx.build_docx(doc, os.path.join(OUT, base + ".docx"), toc_pages=pages)
            print("DOCX ", base + ".docx")
    # classeur : construit une fois, puis rendu PDF depuis le même contenu
    xlsx = os.path.join(OUT, "03_Cadre_Performance_2027_2028.xlsx")
    render_xlsx.build_xlsx(xlsx)
    print("XLSX ", os.path.basename(xlsx))
    # 02 : PDF du plan, version de diffusion
    src = os.path.join(OUT, "01_Plan_Suivi_Evaluation_2027_2028.pdf")
    dst = os.path.join(OUT, "02_Plan_Suivi_Evaluation_2027_2028.pdf")
    if os.path.exists(src):
        import shutil
        shutil.copyfile(src, dst)
        print("PDF  ", os.path.basename(dst))
    print("%.1fs" % (time.time() - t0))


if __name__ == "__main__":
    run()
