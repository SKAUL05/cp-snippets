import math
import datetime
import collections
import statistics
import itertools


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def input_list():
    ll = list(map(int, input().split(" ")))
    return ll


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
    if cc:
        rf = ["0"] * (oo + 1) + ["1"] * (ii)
        rf = "".join(rf)
    else:
        rf = ["0"] * (oo) + ["1"] * (ii)
        rf = "".join(rf)
    print(rf)

    tc -= 1
