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
    arr = input_list()
    x = arr[::-1]
    
    c = 0
    l = n
    for i in range(1,n):
        if c == 0:
            if x[i] < x[i-1]:
                c+=1
        if c == 1:
            if x[i] > x[i-1]:
                break
        l -=1
        
    print(l-1)
    
