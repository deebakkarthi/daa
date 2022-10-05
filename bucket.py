#!/usr/bin/env python3
import sys
from math import floor
from itertools import chain
from dataclasses import dataclass
from time import perf_counter_ns
import tracemalloc


@dataclass
class stats:
    comp: int = 0
    swap: int = 0
    basic: int = 0
    time: float = 0
    mem: float = 0

    def __str__(self):
        return f"{self.comp} {self.swap} {self.basic} {self.time} {self.mem}"


def usage():
    print("Usage: bucket FILE")


def isort(a):
    global stat
    for i in range(1, len(a)):
        stat.basic += 1
        j = i
        # Move the element leftward until a smaller element is encountered
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
            stat.comp += 2
            stat.basic += 11
            stat.swap += 1


def bucket(a, k):
    global stat
    # Don't use [[]]*k. Just points to the same list k times
    buckets = [[] for _ in range(k)]
    M = max(a)
    stat.basic += 2
    for i in range(0, len(a)):
        buckets[floor(k*a[i]/(M+1))].append(a[i])
        stat.basic += 6
    for i in range(0, k):
        isort(buckets[i])
        stat.basic += 1
    # Concatenate the buckets
    return list(chain.from_iterable(buckets))

if __name__ == "__main__":
    stat = stats()
    if len(sys.argv) < 2:
        usage()
        sys.exit(0)
    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]

    tracemalloc.start()
    stat.time = perf_counter_ns()

    bucket(arr, 10)

    stat.time = perf_counter_ns() - stat.time
    stat.mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(len(arr),stat)
