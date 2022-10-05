#!/usr/bin/env python3
import sys


def usage():
    print("Usage: mergesort FILE")


def msort(a):
    if len(a) > 1:
        mid = len(a) // 2
        # split the og arr to left and right
        left = a[:mid]
        right = a[mid:]
        msort(left)
        msort(right)
        merge(left, right, a)
    return


def merge(left, right, a):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # Copying the rest of the larger arr to the main arr
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]
    msort(arr)
