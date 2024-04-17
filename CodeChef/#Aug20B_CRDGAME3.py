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
    n, k = map(int, input().split())

    if n < 10 and k < 10:
        print(1, 1)
    else:
        x = 0 if n < k else 1
        y = math.ceil(min(n, k) / 9)
        print(x, y)
