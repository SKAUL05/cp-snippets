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
    h, p = map(int, input().split())
    while h > 0 and p > 0:
        h -= p
        p = int(p / 2)

    if h > 0:
        print(0)
    else:
        print(1)
