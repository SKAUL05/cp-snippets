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
    n, b, m = map(int, input().split())
    x = list(range(n))
    arr = input_list()
    f = 0
    ci = []
    for i in range(len(arr)):
        if not ci:
            f += 1
            if arr[i] < b:
                l = 0
                h = b
            elif arr[i] == b:
                l = b
                h = b + b
            else:
                l = arr[i] - (arr[i] % b)
                h = l + b
            ci = [l, h - 1]
        elif not (ci[0] <= arr[i] <= ci[1]):
            f += 1
            if arr[i] < b:
                l = 0
                h = b
            elif arr[i] == b:
                l = b
                h = b + b
            else:
                l = arr[i] - (arr[i] % b)
                h = l + b
            ci = [l, h - 1]
    print(f)
