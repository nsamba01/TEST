# -*- coding: utf-8 -*-
"""Aperçu : png des pages + contrôle de débordement."""
import sys, os
sys.path.insert(0, '.')
import pymupdf

def preview(path, outdir, pages=None, zoom=1.55):
    os.makedirs(outdir, exist_ok=True)
    d = pymupdf.open(path)
    n = len(d)
    sel = pages if pages is not None else range(n)
    for i in sel:
        if i >= n:
            continue
        p = d[i]
        pix = p.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
        pix.save(os.path.join(outdir, "p%03d.png" % (i + 1)))
    return n

def overflows(path):
    """Détecte tout texte hors des marges."""
    d = pymupdf.open(path)
    bad = []
    for i, p in enumerate(d):
        w, h = p.rect.width, p.rect.height
        for b in p.get_text("blocks"):
            x0, y0, x1, y1 = b[:4]
            if x0 < 20 or x1 > w - 20 or y0 < 18 or y1 > h - 18:
                bad.append((i + 1, round(x0), round(y0), round(x1), round(y1), b[4][:60].replace("\n", " ")))
    return bad

if __name__ == "__main__":
    pdf = sys.argv[1]
    out = sys.argv[2]
    sel = [int(x) - 1 for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None
    print("pages:", preview(pdf, out, sel))
    for b in overflows(pdf)[:40]:
        print("DEBORD", b)
