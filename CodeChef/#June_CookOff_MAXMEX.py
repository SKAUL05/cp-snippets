import math
import datetime
import collections
import statistics
import itertools
from collections import Counter 



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
    n,m = map(int,input().split())
    ar = input_list()
    x = Counter(ar)
    c = False
    for i in range(1,m):
        if i not in x:
            print (-1)
            c = True
            break
    if not c:
        print (n - x[m])
        

