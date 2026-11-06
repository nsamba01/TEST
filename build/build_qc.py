# -*- coding: utf-8 -*-
import sys, time
sys.path.insert(0, '.')
import doc_qc, render_pdf
t0=time.time()
doc = doc_qc.build()
print("blocs:", len(doc.blocks))
print(render_pdf.build_pdf(doc, "/tmp/qc_test.pdf"), "%.1fs"%(time.time()-t0))
