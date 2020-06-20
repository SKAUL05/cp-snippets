import math
import datetime
import collections
import statistics
import itertools


def input_list():
    ll = list(map(int, input().split(" ")))
    return ll

### Start of Main Code


def find_maxi_gcd(x) : 
    if x%2 == 0:
        return x//2
    else:
        return (x-1)//2

t = int(input())
while t:
    x = int(input())
    print(find_maxi_gcd(x))
    
    t-=1
