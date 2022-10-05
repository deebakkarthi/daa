#!/usr/bin/env python3
import sys


def usage():
    print("Usage: iquicksort FILE")


def qsort(arr, start, end):
    if start >= end:
        return
    left = start
    right = end - 1
    # Take the pivot as the rightmost element
    pivot = arr[end]
    pivot_i = end
    while left <= right:
        # Find the first element greater than pivot from the left
        while (left <= right) and (arr[left] <= pivot):
            left += 1
        # Find the first element smaller or equal to the pivot from the right
        while (left <= right) and (arr[right] > pivot):
            right -= 1
        # If they are on the wrong sides
        if left <= right:
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    # put the pivot in the correct place
    arr[pivot_i], arr[left] = arr[left], arr[pivot_i]
    qsort(arr, start, left - 1)
    qsort(arr, left+1, end)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]
    qsort(arr, 0, len(arr)-1)
