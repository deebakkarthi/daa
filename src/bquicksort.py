#!/usr/bin/env python3
import config

def isort(a, start, end):
    for i in range(start+1, end):
        j = i
        while j > start and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

def bqsort(arr, start, end):
    # Ugly solution for setting default args
    if end is None:
        end = len(arr) - 1
    config.stat.comp += 1
    if start >= end:
        return

    left = start
    right = end - 1
    config.stat.basic += 3

    # Take the pivot as median of mid, left and end
    mid = (left + right) // 2
    if arr[mid] < arr[left]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[end] < arr[left]:
        arr[left], arr[end] = arr[end], arr[left]
    if arr[mid] < arr[end]:
        arr[end], arr[mid] = arr[mid], arr[end]
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
    if (left -1 - start) <= 10:
        isort(arr, start, left-1)
    else:
        bqsort(arr, start, left - 1)
    if (end - left+1) <= 10:
        isort(arr, left+1, end)
    else:
        bqsort(arr, left+1, end)
