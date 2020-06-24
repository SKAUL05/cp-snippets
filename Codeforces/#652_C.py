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
    num,fr = map(int,input().split())
    nlist = sorted(input_list(),reverse = True)
    frlist = sorted(input_list())
    
    su = 0
    for i in range(fr):
        su += nlist[i]
        if frlist[i] ==1:
            su += nlist[i]

    cc = fr
    for i in range(fr):
        frlist[i] -=1
        if frlist[i]>0:
            su += nlist[cc+frlist[i]-1]
            cc+=frlist[i]

    print(su)
