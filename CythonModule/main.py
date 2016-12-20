# -*- coding: utf-8 -*-

import random
from benchmarker import Benchmarker
from Number import Number
import ModuleCPython as mcp
import ModuleCython as mcy

if __name__ == '__main__':
    array = [None] * 10000
    for i in range(len(array)):
        array[i] = Number()
    # print(array)

    with Benchmarker(loop=10000) as bench:
        @bench('normal')
        def _(bm):
            summ = 0
            for i in bm:
                summ += mcp.calc(array)

        @bench('cython')
        def _(bm):
            summ = 0
            for i in bm:
                summ += mcy.calc(array)

