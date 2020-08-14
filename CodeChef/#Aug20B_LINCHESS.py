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
    arr = input_list()

    mini = 100000000000
    ind = -1
    for i in arr:
        if k % i == 0:
            if k // i < mini:
                mini = k // i
                ind = i
    print(ind)
