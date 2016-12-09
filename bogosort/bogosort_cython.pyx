# -*- coding: utf-8 -*-

from __future__ import division
from typing import List
import random
import copy
import numpy as np
cimport numpy as np

cdef int is_sorted(array):
    cdef int i = 1
    cdef int length = len(array)
    while i < length:
        if array[i - 1] > array[i]:
            return False
        i += 1
    return True

cdef int _bogosort(array, int verbose=False):
    result = copy.deepcopy(array)
    judge = is_sorted
    shuffle = np.random.shuffle
    cdef int count = 0
    print('[befor]: {}'.format(array))
    while True:
        if judge(result):
            break
        shuffle(result)
        if verbose:
            print('[{0:05d}]: {1}'.format(count, result))
        count += 1
    print('[after] : {}'.format(result))
    return count

def bogosort(array, verbose=False):
    return _bogosort(array, verbose)
