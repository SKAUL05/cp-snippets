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
    a,b,n,m = map(int,input().split())
    if n<=a and m<=b and not (n==0 and a==0):
        print("Yes")
    else:
        print("No")
