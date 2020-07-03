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
    xy = int(input())
    l = 1
    arr = [[0,"X","X","X","X","X","X","X"]]
    for i in range(7):
        x = []
        for j in range(8):
            x.append("X")
        arr.append(x)

    for i in range(len(arr)):
        if l == xy:
            break
        for j in range(len(arr[i])):
            if arr[i][j] != 0 and l < xy:
                arr[i][j] = "."
                l +=1
            if l == xy:
                break
                
    for i in arr:
        for j in i:
            print(j,end="")
        print("")
            
