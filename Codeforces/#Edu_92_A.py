import math
import datetime
import collections
import statistics
import itertools


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


tc = int(input())
for _ in range(tc):
    x, y = map(int, input().split())
    if x * 2 > y:
        print(-1, -1)
    else:
        print(x, 2 * x)
