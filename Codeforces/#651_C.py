import math
import datetime
import collections
import statistics
import itertools
from functools import reduce

def ip(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True


def input_list():
    ll = list(map(int, input().split()))
    return ll


tc = int(input())
ash, faf = "Ashishgup","FastestFinger"
for _ in range(tc):
    n = int(input())
    if n == 1:
        print(faf)
        
    elif n==2:
        print(ash)
    elif n%2==1:
        print(ash)
    elif not n&(n-1):
        print(faf)        
    elif ip(n//2):
        print(faf)
    else:
        print(ash)
    
