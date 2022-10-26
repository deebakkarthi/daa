#!/usr/bin/env python3
from insertionsort import isort
from math import floor, sqrt
from itertools import chain
import config


def bsort(a):
    k = int(sqrt(len(a)))
    # Don't use [[]]*k. Just points to the same list k times
    buckets = [[] for _ in range(k)]
    M = max(a)
    config.stat.basic += 2
    for i in range(0, len(a)):
        tmp = M * 0.01
        buckets[floor(k*a[i]/(M+tmp))].append(a[i])
        config.stat.basic += 6
    for i in range(0, k):
        isort(buckets[i])
        config.stat.basic += 1
    # Concatenate the buckets
    return list(chain.from_iterable(buckets))
