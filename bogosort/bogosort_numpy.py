# -*- coding: utf-8 -*-

import copy
import numpy as np

def is_sorted(array):
    i = 1
    length = len(array)
    while i < length:
        if array[i - 1] > array[i]:
            return False
        i += 1
    return True

def bogosort(array, verbose=False):
    count = 0
    judge = is_sorted
    shuffle = np.random.shuffle
    result = np.array(copy.deepcopy(array))
    print('[befor]: {}'.format(array))
    while True:
        if judge(result):
            break
        shuffle(result)
        if verbose:
            print('[{0:05d}]: {1}'.format(count, result))
        count += 1
    print('[after] : {}'.format(result))
    return (result, count)

