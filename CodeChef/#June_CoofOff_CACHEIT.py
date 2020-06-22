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
        elif ci[0] <= arr[i] <= ci[1]:
            pass

    print(f)
