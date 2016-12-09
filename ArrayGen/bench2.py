import sys
import time
import random
import numpy as np
from collections import deque
from benchmarker import Benchmarker

loop = 100000
with Benchmarker(loop, cycle=5, extra=1) as bench:
    @bench('normal')
    def _(bm):
        a = []
        for i in bm:
            a.append(random.uniform(-0.1, 0.1))

    @bench('random cache')
    def _(bm):
        a = []
        ran = random.uniform
        for i in bm:
            a.append(ran(-0.1, 0.1))

    @bench('append cache')
    def _(bm):
        a = []
        append = a.append
        for i in bm:
            append(random.uniform(-0.1, 0.1))

    @bench('random & append cache')
    def _(bm):
        a = []
        ran = random.uniform
        append = a.append
        for i in bm:
            append(ran(-0.1, 0.1))

    @bench('op: precreate array')
    def _(bm):
        a = [None] * bench.loop
        ran = random.uniform
        for i in a:
            i = ran(-0.1, 0.1)

    @bench('op: use deque')
    def _(bm):
        a = deque()
        append = a.append
        ran = random.uniform
        for i in bm:
            append(ran(-0.1, 0.1))

    # too fast
    # @bench('op: use numpy.random.uniform')
    # def _(bm):
    #     np.random.uniform(-0.1, 0.1, bench.loop)

