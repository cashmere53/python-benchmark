# -*- coding: utf-8 -*-

import time
import random
import bogosort_normal as bogoNormal
import bogosort_numpy as bogoNumpy
import bogosort_cython as bogoCython

def main():
    arraySize = 10
    ntime = time.clock
    array = [x for x in range(arraySize)]
    random.shuffle(array)

    stime = ntime()
    result, count = bogoNormal.bogosort(array)
    etime = ntime()
    epochTime = etime - stime
    print('bogoNormal: {}[sec]\nspeed: {}[aps]'.format(epochTime, count/epochTime))

    stime = ntime()
    result, count = bogoNumpy.bogosort(array)
    etime = ntime()
    epochTime = etime - stime
    print('bogoNumpy: {}[sec]\nspeed: {}[aps]'.format(epochTime, count/epochTime))

    stime = ntime()
    count = bogoCython.bogosort(array)
    etime = ntime()
    epochTime = etime - stime
    # print('bogoNormal: {}[sec]'.format(epochTime))
    print('bogoCython: {}[sec]\nspeed: {}[aps]'.format(epochTime, count/epochTime))

if __name__ == '__main__':
    main()


