# -*- corging: utf-8 -*-

import random
import numpy as np
from benchmarker import Benchmarker


SIZE = 50
with Benchmarker(10000, width=25, cycle=3, extra=1) as bench:
    @bench('for: random.uniform')
    def _(bm):
        array = []
        append = array.append
        ran = random.uniform
        for i in bm:
            child = []
            c_append = child.append
            for j in range(SIZE):
                c_append(ran(-0.1, 0.1))
            append(child)
        np.array(array)

    @bench('numpy.random.rand')
    def _(bm):
        array = []
        append = array.append
        ran = np.random.rand
        for i in bm:
            rarray = ran(-0.1, 0.1, SIZE)
            append(rarray)
