import math
import datetime
import collections
import statistics
import itertools


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


tc = int(input())
for _ in range(tc):
    s = list(input())
    o, e = 0, 1
    n = len(s)

    while e < n:
        if s in [["0", "1"], ["1", "0"]]:
            o += 1
            break
        elif s[e] != s[e - 1]:
            del s[e - 1]
            del s[e - 1]
            e = 1
            n = len(s)
            o += 1
        else:
            e += 1
    if o % 2 == 1:
        print("DA")
    else:
        print("NET")
