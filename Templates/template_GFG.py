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


@time_calculation
def main():
    print(" ")


if __name__ == "__main__":
    main()
