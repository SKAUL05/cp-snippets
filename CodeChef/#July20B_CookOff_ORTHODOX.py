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
    import copy
    arr = input_list()
    dird = {}
    c = False
    for i in arr:
        if i not in dird:
            dird[i] = 1
        
    ans = arr[0]
    for i in range(1,n):
        ans|= arr[i]
        if ans in dird:
            c = True
            break
        else:
            dird[ans] =1
    if c:
        print("NO")
    else:
        print("YES")
  
    
