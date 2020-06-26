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
    s = list(input())
    o,e = 0,1
    n = len(s)

    while e < n:
        if s == ["0","1" ]or s == ["1","0"]:
            o +=1
            break
        elif s[e] != s[e-1]:
            del s[e-1]
            del s[e-1]
            e = 1
            n = len(s)
            o +=1
        else:
            e +=1
    if o % 2 == 1:
        print("DA")
    else:
        print("NET")
