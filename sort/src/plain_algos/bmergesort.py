#!/usr/bin/env python3

# Better mergesort
# only creates one subarray per merge
# end here is last index + 1. This makes the slicing pretty but the
# calculations ugly
def bmsort(a, start, end):
    # Default arg
    if end is None:
        end = len(a)
    if (end - start) > 1:
        mid = (end - start + 1) // 2

        lstart = start
        lend = start + mid
        rstart = lend
        rend = end
        # Instead of sending subarrays
        # we send indices along with the original array
        bmsort(a, lstart, lend)
        bmsort(a, rstart, rend)
        merge(a, lstart, lend, rstart, rend)
    return


def merge(a, lstart, lend, rstart, rend):
    k = rend - 1
    i = lend - 1
    # This is the only subarray created
    # The right side is always smaller
    b = a[rstart:rend]
    j = len(b) - 1
    # Just like the regular merge but reversed
    # we go from right to left placing the largest of the two arrays
    while i >= lstart and j >= 0:
        if b[j] > a[i]:
            a[k] = b[j]
            j -= 1
        else:
            a[k] = a[i]
            i -= 1
        k -= 1
    # Copying the rest of the larger array
    while i >= lstart:
        a[k] = a[i]
        k -= 1
        i -= 1
    while j >= 0:
        a[k] = b[j]
        k -= 1
        j -= 1
    return
