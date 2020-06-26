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
    a, b, c = map(int, input().split())
    l, r = -1, -1
    if a < c:
        l = 1
    else:
        l = -1
    if c < a * b:
        r = b
    else:
        r = -1
    print(l, r)
