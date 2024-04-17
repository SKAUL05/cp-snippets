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
    x = []
    arr = input_list()
    for i in arr:
        if i not in x:
            x.append(i)

    for i in x:
        print(i, end=" ")
    print(" ")
