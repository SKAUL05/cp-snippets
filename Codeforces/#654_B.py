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
    n, r = map(int, input().split())
    ans = (n * (n - 1) // 2) + 1 if r >= n else (r * (r + 1)) // 2
    print(ans)
