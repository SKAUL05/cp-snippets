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
    a, b, n, m = map(int, input().split())
    if a + b < m + n or (m > min(a, b)):
        print("No")
    else:
        print("Yes")
