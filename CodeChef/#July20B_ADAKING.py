import math
import datetime
import collections
import statistics
import itertools


def is_prime(num):
    return all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))


def input_list():
    return list(map(int, input().split(" ")))


def find_sum(x):
    return sum(int(i) for i in x)


tc = int(input())
for _ in range(tc):
    xy = int(input())
    l = 1
    arr = [["O", "X", "X", "X", "X", "X", "X", "X"]]
    for _ in range(7):
        x = ["X" for _ in range(8)]
        arr.append(x)

    for item in arr:
        if l == xy:
            break
        for j in range(len(item)):
            if item[j] != "0" and l < xy:
                item[j] = "."
                l += 1
            if l == xy:
                break

    for i in arr:
        for j in i:
            print(j, end="")
        print("")
