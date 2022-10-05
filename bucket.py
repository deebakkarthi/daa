#!/usr/bin/env python3
import sys
from math import floor
from itertools import chain


def usage():
    print("Usage: bucket FILE")


def isort(a):
    for i in range(1, len(a)):
        j = i
        # Move the element leftward until a smaller element is encountered
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def bucket(a, k):
    # Don't use [[]]*k. Just points to the same list k times
    buckets = [[] for _ in range(k)]
    M = max(a)
    for i in range(0, len(a)):
        buckets[floor(k*a[i]/(M+1))].append(a[i])
    for i in range(0, k):
        isort(buckets[i])
    # Concatenate the buckets
    return list(chain.from_iterable(buckets))


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]
    arr = bucket(arr, 10)
