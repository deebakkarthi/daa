#!/usr/bin/env python3
import config


def qsort(arr, start, end):
    # Ugly solution for setting default args
    if end is None:
        end = len(arr) - 1
    config.stat.comp += 1
    if start >= end:
        return

    left = start
    right = end - 1
    config.stat.basic += 3

    # Take the pivot as the rightmost element
    pivot = arr[end]
    pivot_i = end
    config.stat.basic += 3

    while left <= right:
        config.stat.comp += 1
        # Find the first element greater than pivot from the left
        while (left <= right) and (arr[left] <= pivot):
            left += 1
            config.stat.comp += 2
            config.stat.basic += 3

        # Find the first element smaller or equal to the pivot from the right
        while (left <= right) and (arr[right] > pivot):
            right -= 1
            config.stat.comp += 2
            config.stat.basic += 3

        # If they are on the wrong sides
        if left <= right:
            config.stat.comp += 1
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            config.stat.swap += 1
            config.stat.basic += 9

    # put the pivot in the correct place
    arr[pivot_i], arr[left] = arr[left], arr[pivot_i]
    config.stat.swap += 1
    config.stat.basic += 5

    qsort(arr, start, left - 1)
    qsort(arr, left+1, end)
