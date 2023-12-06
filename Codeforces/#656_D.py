import datetime
import collections
import statistics
import itertools
import math


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


def recr(ch, lef, rig, ss):
    if lef == rig:
        return 1 if ss[lef] != ch else 0
    l = rig - lef + 1
    cnt = sum(1 for i in range(lef, lef + l // 2) if ss[i] != ch)
    ret = cnt + recr(chr(ord(ch) + 1), lef + l // 2, rig, ss)
    cnt = sum(1 for i in range(lef + l // 2, rig + 1) if ss[i] != ch)
    ret = min(ret, cnt + recr(chr(ord(ch) + 1), lef, lef + l // 2 - 1, ss))
    return ret


tc = int(input())
for _ in range(tc):
    n = int(input())
    ss = input()
    ch = "a"
    print(recr(ch, 0, n - 1, ss))
