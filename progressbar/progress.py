# -*- coding: utf-8 -*-
import progressbar as pb
import time

bar1 = pb.ProgressBar(max_value=1000)
for i in range(1000):
    time.sleep(0.02)
    bar1.update(i+1)
