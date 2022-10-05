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
    print("Usage: iheapsort FILE")

class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # To facilitate len()
    def __len__(self):
        return self.currentSize

    """ This method defines the upheap function when inserting an element
    """
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        global stat
        while (i * 2) <= self.currentSize:
            stat.comp += 1
            mc = self.minChild(i)
            stat.basic += 2
            if self.heapList[i] > self.heapList[mc]:
                stat.comp += 1
                self.heapList[i], self.heapList[mc] = \
                        self.heapList[mc], self.heapList[i]
                stat.swap += 1
            i = mc

    def minChild(self,i):
        global stat
        stat.comp += 1
        stat.basic += 2
        if i * 2 + 1 > self.currentSize:
            stat.basic += 1
            return i * 2
        else:
            stat.comp += 1
            stat.basic += 7
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):  #// \label{lst:bh:loop}
            self.percDown(i)
            i = i - 1


    #create a method to print the contents of the heap in level order 
    def printHeap(self):
        print(self.heapList)

def hsort(h):
    global stat
    n = len(h)
    stat.basic += 1
    for i in range(n, 0, -1):
        # Swap smallest with the last
        h.heapList[i], h.heapList[1] = h.heapList[1], h.heapList[i]
        # Smallest is in the right place
        # Consider that element as deleted
        h.currentSize -= 1
        # downheap() the new root to the right place
        h.percDown(1)
        stat.swap += 1
        stat.basic += 7
    # Remove the 0
    h.heapList.pop(0)
    # Reverse as we are using a minheap
    h.heapList.reverse()
    return h.heapList


if __name__ == "__main__":

    stat = stats()

    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]

if __name__ == "__main__":


    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    arr = list()
    with open(sys.argv[1], 'r') as f:
        i = f.readline().strip()
        arr = [float(x) for x in i.split()]

    tracemalloc.start()
    stat.time = perf_counter_ns()

    heap = BinHeap()
    heap.buildHeap(arr)
    arr = hsort(heap)

    stat.time = perf_counter_ns() - stat.time
    stat.mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(len(arr),stat)
