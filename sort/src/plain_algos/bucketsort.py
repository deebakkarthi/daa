#!/usr/bin/env python3
from insertionsort import isort
from math import floor, sqrt
from itertools import chain


def bsort(a):
    # Setting #(buckets) to sqrt(n)
    k = int(sqrt(len(a)))
    # Don't use [[]]*k. Just points to the same list k times
    buckets = [[] for _ in range(k)]
    M = max(a)
    for i in range(0, len(a)):
        # tmp is used so that the largest element gets the last index
        # If tmp is not used a[i]/M will give 1 which inturn gives the index as
        # k but we want k-1. So setting the denominator to be always greater
        tmp = M * 0.01
        buckets[floor(k*a[i]/(M+tmp))].append(a[i])
    for i in range(0, k):
        isort(buckets[i])
    # Concatenate the buckets
    return list(chain.from_iterable(buckets))
