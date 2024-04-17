import math
import datetime
import collections
import statistics
import itertools
from collections import Counter
from collections import OrderedDict


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


tc = int(input())

for _ in range(tc):
    s = input()
    p = input()

    mp = {}
    for i in s:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    for i in p:
        if i in mp:
            mp[i] -= 1
    mp = OrderedDict(sorted(mp.items()))
    strt, end = "", ""
    ch = ""
    num = 0
    for i, j in mp.items():
        if i < p[0]:
            while j > 0:
                strt += i
                j -= 1
        elif i == p[0]:
            ch = i
            num = j
        elif i > p[0]:
            while j > 0:
                end += i
                j -= 1
    i = 0
    f = ""
    ff = 0
    while i < len(p):
        if p[i] < ch:
            f = strt + p
            while num:
                f += ch
                num -= 1
            f += end
            ff = 1
            break
        elif p[i] > ch:
            f = strt
            while num:
                f += ch
                num -= 1
            f = f + p + end
            ff = 1
            break
        i += 1
    i = 0
    if ff == 0:
        f = s
    print(f)
