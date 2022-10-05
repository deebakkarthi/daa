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
    print("Usage: iquicksort FILE")


def qsort(arr, start, end):
    global stat

    stat.comp += 1
    if start >= end:
        return

    left = start
    right = end - 1
    stat.basic += 3

    # Take the pivot as the rightmost element
    pivot = arr[end]
    pivot_i = end
    stat.basic += 3

    while left <= right:
        stat.comp += 1
        # Find the first element greater than pivot from the left
        while (left <= right) and (arr[left] <= pivot):
            left += 1
            stat.comp += 2
            stat.basic += 3

        # Find the first element smaller or equal to the pivot from the right
        while (left <= right) and (arr[right] > pivot):
            right -= 1
            stat.comp += 2
            stat.basic += 3

        # If they are on the wrong sides
        if left <= right:
            stat.comp += 1
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            stat.swap += 1
            stat.basic += 9

    # put the pivot in the correct place
    arr[pivot_i], arr[left] = arr[left], arr[pivot_i]
    stat.swap += 1
    stat.basic += 5

    qsort(arr, start, left - 1)
    qsort(arr, left+1, end)


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

    qsort(arr, 0, len(arr)-1)

    stat.time = perf_counter_ns() - stat.time
    stat.mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(len(arr),stat)
