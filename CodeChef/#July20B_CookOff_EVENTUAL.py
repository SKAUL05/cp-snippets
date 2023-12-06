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
    s = input()

    x = {}
    for i in s:
        if i not in x:
            x[i] = 1
        else:
            x[i] += 1
    c = any(j % 2 != 0 for j in x.values())
    if c:
        print("NO")
    else:
        print("YES")
