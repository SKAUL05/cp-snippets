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
    n,r = map(int, input().split())
    if r>=n:
        ans = (n * (n-1)//2) + 1
    else:
        ans = (r*(r+1))//2
    print(ans)
