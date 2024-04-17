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
    a, b, c = map(int, input().split())
    l, r = -1, -1
    l = 1 if a < c else -1
    r = b if c < a * b else -1
    print(l, r)
