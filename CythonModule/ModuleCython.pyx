# -*- coding: utf-8 -*-

from __future__ import division

def calc(array):
    return _calc(array)

cdef int _calc(array):
    cdef int summ = 0
    for a in array:
        summ += a.num1
    return summ
