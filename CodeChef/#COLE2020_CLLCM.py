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
    lll = list(map(int, input().split(" ")))
    return lll

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = input_list()
    arr.sort()
    k = 0
    for i in range(n):
        if arr[i] % 2 ==0:
            k+=1
            break
    if k == 0:
        print("YES")
    else:
        print("NO")
        
        




    
            
