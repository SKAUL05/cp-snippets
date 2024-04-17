import math
import datetime
import collections
import statistics
import itertools
from functools import reduce


def ip(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split()))


tc = int(input())
ash, faf = "Ashishgup", "FastestFinger"
for _ in range(tc):
    n = int(input())
    if n == 1:
        print(faf)

    elif n == 2:
        print(ash)
    elif n % 2 == 1:
        print(ash)
    elif not n & (n - 1):
        print(faf)
    elif ip(n // 2):
        print(faf)
    else:
        print(ash)
