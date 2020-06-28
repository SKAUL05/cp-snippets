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
    s, n = map(int, input().split())

    if s % n == 0 and s >= n:
        print(s // n)
    elif s < n:
        if s == 1:
            print(1)
        elif s % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        l = s // n
        x = s % n
        if x == 1:
            l += 1
        elif x % 2 == 0:
            l += 1
        else:
            l += 2
        print(l)
