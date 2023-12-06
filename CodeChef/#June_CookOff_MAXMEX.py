import math
import datetime
import collections
import statistics
import itertools
from collections import Counter


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    ar = input_list()
    x = Counter(ar)
    c = False
    for i in range(1, m):
        if i not in x:
            print(-1)
            c = True
            break
    if not c:
        print(n - x[m])
