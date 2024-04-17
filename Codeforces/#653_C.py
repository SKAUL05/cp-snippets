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
