# -*- coding: utf-8 -*-
import sys, time
sys.path.insert(0, '.')
import doc_cadre, render_pdf
t0 = time.time()
doc = doc_cadre.build()
print("blocs:", len(doc.blocks))
print(render_pdf.build_pdf(doc, "/tmp/cadre_test.pdf"), "%.1fs" % (time.time()-t0))
