##Problem Statement: Given a array of both positive and negative integers which are sorted. Task is to sort square of the numbers of the Array.
##Solution:
##    Time Complexity: O(n)
##    Space Complexity: O(n)
##

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


def square_sort(arr, n):
    find = 0
    for find in range(n):
        if arr[find] >= 0:
            break

    first_half = find - 1
    second_half = find
    final = [0] * n
    index = 0
    while first_half >= 0 and second_half < n:
        if arr[first_half] * arr[first_half] < arr[second_half] * arr[second_half]:
            final[index] = arr[first_half] * arr[first_half]
            first_half -= 1
        else:
            final[index] = arr[second_half] * arr[second_half]
            second_half += 1

        index += 1
    while first_half >= 0:
        final[index] = arr[first_half] * arr[first_half]
        first_half -= 1
        index += 1
    while second_half < n:
        final[index] = arr[second_half] * arr[second_half]
        second_half += 1
        index += 1
    return final


@time_calculation
def main():
    arr = input_list()
    print("Before Sort...")
    for element in arr:
        print(element, end=" ")
    print(" ")
    arr = square_sort(arr, len(arr))
    print("After Sort")
    for element in arr:
        print(element, end=" ")
    print(" ")


if __name__ == "__main__":
    main()
