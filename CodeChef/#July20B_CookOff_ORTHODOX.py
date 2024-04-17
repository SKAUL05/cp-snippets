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
    import copy

    arr = input_list()
    dird = {}
    c = False
    for i in arr:
        if i not in dird:
            dird[i] = 1

    ans = arr[0]
    for i in range(1, n):
        ans |= arr[i]
        if ans in dird:
            c = True
            break
        else:
            dird[ans] = 1
    if c:
        print("NO")
    else:
        print("YES")
