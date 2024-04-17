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
    arr.sort()
    k = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            k += 1
            break
    if k == 0:
        print("YES")
    else:
        print("NO")
