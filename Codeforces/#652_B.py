import math
import datetime
import collections
import statistics
import itertools


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


tc = int(input())

while tc:
    n = int(input())
    s = list(input())
    oo = 0
    ii = 0
    for i in range(0, n):
        if s[i] == "0":
            ##            print('here')
            oo += 1
        else:
            break
    vv = s
    vv = vv[::-1]
    for i in range(0, n):
        if vv[i] == "1":
            ii += 1
        else:
            break
    cc = False
    if len(s) > ii + oo:
        cc = True
    ##    print(oo,ii,cc)
    rf = ["0"] * (oo + 1) + ["1"] * (ii) if cc else ["0"] * (oo) + ["1"] * (ii)
    rf = "".join(rf)
    print(rf)

    tc -= 1
