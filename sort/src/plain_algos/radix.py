#!/usr/bin/env python3
from math import log10
from itertools import chain


def radix(arr):
    buckets = [[] for _ in range(10)]
    arr_max = max(arr)
    # Number of digits of the maximum number
    d = int(log10(arr_max)) + 1
    for i in range(1, d+1):
        for j in arr:
            # Extract the ith digit and put it in the correct index
            # // by 10^(i - 1) removes the last i - 1 digits
            # % 10 gets the last from the remaining
            # for i = 3, last 2 digits are deleted by //
            # the third digit from the last is extracted by %
            ind = (j // (10**(i-1))) % 10
            buckets[ind].append(j)
        # Update the array
        arr = list(chain.from_iterable(buckets))
        # Clean the buckets
        buckets = [[] for _ in range(10)]
    return arr
