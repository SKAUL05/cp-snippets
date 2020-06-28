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

for _ in range(tc):
    n = int(input())
    s = input()
    m = 1000000
    ss = 0
    for i in s:
        if i == "(":
            ss += 1
        elif i == ")":
            ss -= 1
        m = min(m, ss)
    print(-1 * m)
