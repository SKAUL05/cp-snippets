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
    arr = input_list()
    x = arr[::-1]

    c = 0
    l = n
    for i in range(1, l):
        if c == 0:
            if x[i] < x[i - 1]:
                c += 1
        if x[i] > x[i - 1]:
            if c == 1:
                break
        l -= 1

    print(l - 1)
