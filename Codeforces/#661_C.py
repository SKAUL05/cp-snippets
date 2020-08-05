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
    mp = dict()
    if n == 1:
        print(0)
        continue
    for i in range(n):
        for j in range(i + 1, n):
            x = arr[i] + arr[j]
            if x in mp:
                if i not in mp[x][1] and j not in mp[x][1]:
                    mp[x][0] += 1
                    mp[x][1].append(i)
                    mp[x][1].append(j)
            else:
                mp[x] = [1, [i, j]]
    ll = -1
    for i, j in mp.items():
        ll = max(ll, j[0])
    print(ll)
