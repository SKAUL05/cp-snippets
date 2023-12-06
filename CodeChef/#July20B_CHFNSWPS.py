import math
import datetime
import collections
import statistics
import itertools
from collections import defaultdict


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


def def_value():
    return 0


tc = int(input())
cc = 0
for _ in range(tc):
    n = int(input())
    a = input_list()
    b = input_list()
    zzz = 1000000000000
    ans = 0
    aa, bb, d = defaultdict(def_value), defaultdict(def_value), defaultdict(def_value)
    xx, yy = [], []
    zz = False
    for i in range(n):
        zzz = min(a[i], zzz)
        zzz = min(b[i], zzz)
        if a[i] not in aa:
            aa[a[i]] = 1
        else:
            aa[a[i]] += 1
        if b[i] not in aa:
            aa[b[i]] = 1
        else:
            aa[b[i]] += 1

    for i, j in aa.items():
        if j % 2 == 1:
            zz = True
            break
        else:
            bb[i] = j // 2
    if zz:
        print(-1)
    else:
        import copy

        d = copy.deepcopy(bb)
        for i in range(n):
            if bb[a[i]]:
                bb[a[i]] -= 1
            else:
                xx.append(a[i])
        for i in range(n):
            if d[b[i]]:
                d[b[i]] -= 1
            else:
                yy.append(b[i])
        xx.sort()
        yy.sort(reverse=True)
        if not xx:
            print(0)
        else:
            for i in range(len(xx)):
                ans += min(2 * zzz, min(xx[i], yy[i]))
            print(ans)
