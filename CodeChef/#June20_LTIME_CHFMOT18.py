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
    s, n = map(int, input().split())

    if s % n == 0 and s >= n:
        print(s // n)
    elif s < n:
        if s == 1 or s % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        l = s // n
        x = s % n
        l += 1 if x == 1 or x % 2 == 0 else 2
        print(l)
