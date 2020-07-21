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
    s = input()

    x = {}
    for i in s:
        if i not in x:
            x[i] = 1
        else:
            x[i] +=1
    c = False
    for i,j in x.items():
        if j % 2!=0:
            c = True
            break
    if c:
        print("NO")
    else:
        print("YES")
