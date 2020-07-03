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

def find_sum(x):
    ss = 0
    for i in x:
        ss += int(i)
    return ss

tc = int(input())
for _ in range(tc):
    rounds = int(input())
    cp,dp = 0,0
    for __ in range(rounds):
        chef,dorthy = map(int,input().split())
        c_s, d_s = find_sum(str(chef)),find_sum(str(dorthy))
        if c_s > d_s:
            cp +=1
        elif c_s < d_s:
            dp+=1
        else:
            cp +=1
            dp+=1
    if cp>dp:
        print(0,cp)
    elif cp<dp:
        print(1,dp)
    else:
        print(2,cp)
        
        
