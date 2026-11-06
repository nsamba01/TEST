# -*- coding: utf-8 -*-
import sys, time
sys.path.insert(0, '.')
import content_plan, render_pdf

t0 = time.time()
doc = content_plan.build()
print("blocs:", len(doc.blocks), "entrées TOC:", len(doc.toc_entries))
info = render_pdf.build_pdf(doc, "/tmp/plan_test.pdf")
print(info, "%.1fs" % (time.time() - t0))
