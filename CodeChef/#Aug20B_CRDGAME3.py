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
    n, k = map(int, input().split())

    if n < 10 and k < 10:
        print(1, 1)
    else:
        x = 0 if n < k else 1
        y = math.ceil(min(n, k) / 9)
        print(x, y)
