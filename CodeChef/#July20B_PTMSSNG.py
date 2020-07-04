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
    n = int(input())
    v = (4*n)-1
    v1,v2 = map(int,input().split())
    xx,yy = v1,v2
    for i in range(1,v):
        x,y = map(int,input().split())
        xx = xx ^ x
        yy = yy ^ y

    print(xx,yy)
