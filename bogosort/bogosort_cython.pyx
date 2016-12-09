# -*- coding: utf-8 -*-

from __future__ import division
from typing import List
import random
import copy
import numpy as np
cimport numpy as np

<<<<<<< HEAD
cdef int is_sorted(array):
=======
def is_sorted(array):
>>>>>>> ab04b950df16a998b947a0b34f1f88ad35c26302
    cdef int i = 1
    cdef int length = len(array)
    while i < length:
        if array[i - 1] > array[i]:
            return False
        i += 1
    return True

<<<<<<< HEAD
cdef int _bogosort(array, int verbose=False):
=======
def bogosort(array, verbose=False):
>>>>>>> ab04b950df16a998b947a0b34f1f88ad35c26302
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

<<<<<<< HEAD
def bogosort(array, verbose=False):
    return _bogosort(array, verbose)
=======
>>>>>>> ab04b950df16a998b947a0b34f1f88ad35c26302
