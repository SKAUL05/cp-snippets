##Problem Statement: Golomb sequence is a non-decreasing integer sequence where n-th term is equal to number of times n appears in the sequence.

import math
import datetime
import collections
import statistics
import itertools
import time
from datetime import datetime


def input_list():
    return list(map(int, input().split(" ")))


def time_calculation(fn):
    def calculate(*args, **kwargs):
        start = datetime.now()
        output = fn(*args, **kwargs)
        print(f"Time Taken {datetime.now() - start}")
        return output

    return calculate


def golamb(num):
    arr = [0] * (num + 1)
    arr[1] = 1
    for r in range(2, num + 1):
        arr[r] = arr[r - arr[arr[r - 1]]] + 1

    return arr[1 : num + 1]


@time_calculation
def main():
    num = int(input())
    arr = golamb(num)
    print(arr)
    return


if __name__ == "__main__":
    main()
