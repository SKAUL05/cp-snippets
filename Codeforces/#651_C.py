import math
import datetime
import collections
import statistics
import itertools
from functools import reduce

def find_divisor(n):
    l = n//2 if n//2 > 3 else n
    for i in range(3,l+ 1,2):
        if n% i == 0 and i % 2 !=0:
            return i
    return None

    
def input_list():
    ll = list(map(int, input().split()))
    return ll



tc = int(input())
for _ in range(tc):
    n = int(input())
    cnt = 1
    if n == 1:
        continue
    elif n==2:
        continue
        
    while n > 1:
        lll = find_divisor(n)
        if lll:
            n= n//lll
            cnt+=1
        else:
            n -=1
            cnt+=1
    if cnt%2 != 0:
        print("FastestFinger")
    else:
        print("Ashishgup")
    
    

    
