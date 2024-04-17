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
    v = (4 * n) - 1
    v1, v2 = map(int, input().split())
    xx, yy = v1, v2
    for _ in range(1, v):
        x, y = map(int, input().split())
        xx = xx ^ x
        yy = yy ^ y

    print(xx, yy)
