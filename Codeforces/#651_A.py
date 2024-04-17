import math
import datetime
import collections
import statistics
import itertools


def input_list():
    return list(map(int, input().split(" ")))


### Start of Main Code


def find_maxi_gcd(x):
    return x // 2 if x % 2 == 0 else (x - 1) // 2


t = int(input())
while t:
    x = int(input())
    print(find_maxi_gcd(x))

    t -= 1
