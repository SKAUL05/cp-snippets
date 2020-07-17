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
    x, y, z = map(int, input().split())
    a, b, c = -1, -1, -1
    fl = False
    if x == y == z:
        print("YES")
        a, b, c = x, y, z
        fl = True
    elif x == y and x > z:
        print("YES")
        a, b, c = x, z, 1
        fl = True
    elif x == z and x > y:
        print("YES")
        a, b, c = x, y, 1
        fl = True
    elif y == z and y > x:
        print("YES")
        a, b, c = y, x, 1
        fl = True
    if fl:
        print(a, b, c)
    else:
        print("NO")
