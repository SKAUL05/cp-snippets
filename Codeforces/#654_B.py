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
    if n == 1:
        print(0)
    elif n == 2:
        print(-1)
    else:
        c = 0
        x = 0
        while n>1 and x < 6:
            if n%6 == 0:
                n = n//6
                x = 0
            else:
                n = n*2
                x +=1
            c +=1
        if n == 1:
            print(c)
        else:
            print(-1)
                
