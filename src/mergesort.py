#!/usr/bin/env python3
import config


def msort(a):
    config.stat.comp += 1
    if len(a) > 1:
        mid = len(a) // 2
        config.stat.basic += 2
        # split the og arr to left and right
        left = a[:mid]
        right = a[mid:]
        config.stat.basic += 4
        msort(left)
        msort(right)
        merge(left, right, a)
    return


def merge(left, right, a):
    i = j = k = 0
    config.stat.basic += 3

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            # Here there is no "swaps"
            # When the right element is smaller we consider that a swap
            config.stat.swap += 1
        k += 1
        config.stat.basic += 9
        config.stat.comp += 3

    # Copying the rest of the larger arr to the main arr
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
        config.stat.comp += 1
        config.stat.basic += 7
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
        config.stat.comp += 1
        config.stat.basic += 7
