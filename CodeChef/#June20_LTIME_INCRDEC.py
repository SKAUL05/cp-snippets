import math
import datetime
import collections
import statistics
import itertools
from collections import Counter


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def input_list():
    ll = list(map(int, input().split(" ")))
    return ll


tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = input_list()
    l = {}
    x = list(set(arr))
    x.sort()
    fl = False
    for i in arr:
        if i not in l:
            l[i] = 1
        else:
            l[i] += 1
        if l[i] > 2:
            fl = True
            break
    l = collections.OrderedDict(sorted(l.items()))
    if fl or l[x[-1]] > 1:
        print("NO")
        continue
    else:
        print("YES")
        for i, j in l.items():
            print(i, end=" ")
            l[i] -= 1
        ss = []
        for i, j in l.items():
            if j >= 1:
                ss.append(i)

        ss = ss[::-1]
        for i in ss:
            print(i, end=" ")
        print(" ")
