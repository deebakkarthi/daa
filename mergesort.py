#!/usr/bin/env python3
import sys
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
    print("Usage: mergesort FILE")


def msort(a):
    global stat
    stat.comp += 1
    if len(a) > 1:
        mid = len(a) // 2
        stat.basic += 2
        # split the og arr to left and right
        left = a[:mid]
        right = a[mid:]
        stat.basic += 4
        msort(left)
        msort(right)
        merge(left, right, a)
    return


def merge(left, right, a):
    global stat
    i = j = k = 0
    stat.basic += 3

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            # Here there is no "swaps"
            # When the right element is smaller we consider that a swap
            stat.swap += 1
        k += 1
        stat.basic += 9
        stat.comp += 3

    # Copying the rest of the larger arr to the main arr
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
        stat.comp += 1
        stat.basic += 7
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
        stat.comp += 1
        stat.basic += 7

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

    msort(arr)

    stat.time = perf_counter_ns() - stat.time
    stat.mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(len(arr),stat)
