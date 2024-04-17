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
    brr = input_list()
    ma = min(arr)
    mb = min(brr)
    count = 0
    res = arr.count(arr[0]) == len(arr)
    rest = brr.count(brr[0]) == len(brr)
    i = 0
    while (not res or not rest) and i < n:
        if arr[i] > ma and brr[i] > mb:
            xx, yy = arr[i], brr[i]
            arr[i] = ma
            brr[i] = mb
            count += max((xx - ma), (yy - mb))

        elif arr[i] > ma:
            x = arr[i]
            arr[i] = ma
            count += x - ma
            i += 1
        elif brr[i] > mb:
            y = brr[i]
            brr[i] = mb
            count += y - mb
            i += 1
        else:
            i += 1

        res = arr.count(arr[0]) == len(arr)
        rest = brr.count(brr[0]) == len(brr)

    print(count)
