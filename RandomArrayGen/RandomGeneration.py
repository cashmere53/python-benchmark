# -*- corging: utf-8 -*-

import random
import numpy as np
from BenchmarkerPlus import BenchmarkerPlus

with BenchmarkerPlus(size=100, loop=10000, cycle=3, extra=1) as bench:
    @bench('for: random.uniform')
    def _(bm):
        array = []
        append = array.append
        ran = random.uniform
        for i in bm:
            child = []
            c_append = child.append
            for j in range(bench.size):
                c_append(ran(-0.1, 0.1))
            append(child)
        np.array(array)

    @bench('numpy.random.uniform')
    def _(bm):
        array = []
        append = array.append
        ran = np.random.uniform
        for i in bm:
            rarray = ran(-0.1, 0.1, bench.size)
            append(rarray)
