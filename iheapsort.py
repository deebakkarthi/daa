#!/usr/bin/env python3
import sys
from binheap import BinHeap


def usage():
    print("Usage: iheapsort FILE")


def hsort(h):
    n = len(h)
    for i in range(n, 0, -1):
        # Swap smallest with the last
        h.heapList[i], h.heapList[1] = h.heapList[1], h.heapList[i]
        # Smallest is in the right place
        # Consider that element as deleted
        h.currentSize -= 1
        # downheap() the new root to the right place
        h.percDown(1)
    # Remove the 0
    h.heapList.pop(0)
    # Reverse as we are using a minheap
    h.heapList.reverse()
    return h.heapList


if __name__ == "__main__":

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]
    heap = BinHeap()
    heap.buildHeap(arr)
    arr = hsort(heap)
