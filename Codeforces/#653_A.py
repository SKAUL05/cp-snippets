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
    x, y, n = map(int, input().split())
    if n % x == y:
        print(n)
    else:
        cc = (n - y) // x
        f = (cc * x) + y
        print(f)
