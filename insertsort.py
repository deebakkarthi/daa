#!/usr/bin/env python3
import sys


def usage():
    print("Usage: insertsort FILE")


def isort(a):
    for i in range(1, len(a)):
        j = i
        # Move the element leftward until a smaller element is encountered
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]
    isort(arr)
    print(arr == sorted(arr))
