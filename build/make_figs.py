# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
import figures
import content_plan3 as C3

figures.fig_gantt('figures/gantt_2027.png', 2027, C3.ROWS_2027)
figures.fig_gantt('figures/gantt_2028.png', 2028, C3.ROWS_2028)
print('gantt ok')
