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


def recr(ch, lef, rig, ss):
    if lef == rig:
        if ss[lef] != ch:
            return 1
        else:
            return 0

    l = rig - lef + 1
    cnt = 0
    for i in range(lef, lef + l // 2):
        if ss[i] != ch:
            cnt += 1
    ret = cnt + recr(chr(ord(ch) + 1), lef + l // 2, rig, ss)
    cnt = 0
    for i in range(lef + l // 2, rig + 1):
        if ss[i] != ch:
            cnt += 1
    ret = min(ret, cnt + recr(chr(ord(ch) + 1), lef, lef + l // 2 - 1, ss))
    return ret


tc = int(input())
for _ in range(tc):
    n = int(input())
    ss = input()
    ch = "a"
    print(recr(ch, 0, n - 1, ss))
