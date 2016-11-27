import sys
import time
import random
from collections import deque

def random1(n):
    start = time.time()
    a = []
    for i in range(n):
        a.append(random.uniform(-0.1, 0.1))
    end = time.time()
    print('time: {}[sec]'.format(end - start))
# >>> random1(10000)
# time: 0.009397029876708984[sec]
# >>> random1(100000)
# time: 0.04796004295349121[sec]
# >>> random1(1000000)
# time: 0.4517390727996826[sec]
# >>> random1(10000000)
# time: 4.388804912567139[sec]

def random2(n):
    start = time.time()
    a = []
    ran = random.uniform
    for i in range(n):
        a.append(ran(-0.1, 0.1))
    end = time.time()
    print('time: {}[sec]'.format(end - start))
# >>> random2(10000)
# time: 0.005746126174926758[sec]
# >>> random2(100000)
# time: 0.042571067810058594[sec]
# >>> random2(1000000)
# time: 0.39870214462280273[sec]
# >>> random2(10000000)
# time: 3.9888651371002197[sec]

def random3(n):
    start = time.time()
    a = deque()
    ran = random.uniform
    for i in range(n):
        a.append(ran(-0.1, 0.1))
    end = time.time()
    print('time: {}[sec]'.format(end - start))
# >>> random3(10000)
# time: 0.0057849884033203125[sec]
# >>> random3(100000)
# time: 0.04150891304016113[sec]
# >>> random3(1000000)
# time: 0.39781713485717773[sec]
# >>> random3(10000000)
# time: 3.9875411987304688[sec]

def random4(n):
    start = time.time()
    a = []
    ran = random.uniform
    append = a.append
    for i in range(n):
        append(ran(-0.1, 0.1))
    end = time.time()
    print('time: {}[sec]'.format(end - start))
# >>> random4(10000)
# time: 0.0057561397552490234[sec]
# >>> random4(100000)
# time: 0.03983592987060547[sec]
# >>> random4(1000000)
# time: 0.37607598304748535[sec]
# >>> random4(10000000)
# time: 3.709289073944092[sec]

def random5(n):
    start = time.time()
    a = [None] * n
    ran = random.uniform
    for i in range(n):
        a[i] = ran(-0.1, 0.1)
    end = time.time()
    print('time: {}[sec]'.format(end - start))
# >>> random5(10000)
# time: 0.004542112350463867[sec]
# >>> random5(100000)
# time: 0.03930377960205078[sec]
# >>> random5(1000000)
# time: 0.3628501892089844[sec]
# >>> random5(10000000)
# time: 3.876703977584839[sec]

if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
    except:
        num = 10000

    random1(num)
    random2(num)
    random3(num)
    random4(num)
    random5(num)
