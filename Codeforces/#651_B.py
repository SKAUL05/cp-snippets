import math
import datetime
import collections
import statistics
import itertools


def input_list():
    ll = list(map(int, input().split(" ")))
    return ll


tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = input_list()
    e,o = [],[]
    for i in range(0,len(arr)):
        if arr[i]%2 == 0:
            e.append(i+1)
        else:
            o.append(i+1)
    r_dict = {}
    for i in range(0,len(o),2):
        if i+1 <len(o):
            r_dict.update({o[i]:o[i+1]})
    for i in range(0,len(e),2):
        if i+1 < len(e):
            r_dict.update({e[i]:e[i+1]})
    cc = 0
    for i,j in r_dict.items():
        if cc < n - 1:
            print(i,j)
            cc +=1
        else:
            break
        
