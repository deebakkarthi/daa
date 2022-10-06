#!/usr/bin/env python3
import config


class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # To facilitate len()
    def __len__(self):
        return self.currentSize

    """ This method defines the upheap function when inserting an element
    """
    def percUp(self, i):
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
        while (i * 2) <= self.currentSize:
            config.stat.comp += 1
            mc = self.minChild(i)
            config.stat.basic += 2
            if self.heapList[i] > self.heapList[mc]:
                config.stat.comp += 1
                self.heapList[i], self.heapList[mc] = \
                        self.heapList[mc], self.heapList[i]
                config.stat.swap += 1
            i = mc

    def minChild(self,i):
        config.stat.comp += 1
        config.stat.basic += 2
        if i * 2 + 1 > self.currentSize:
            config.stat.basic += 1
            return i * 2
        else:
            config.stat.comp += 1
            config.stat.basic += 7
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

def hsort(a):
    # Creating a heap
    h = BinHeap()
    h.buildHeap(a)

    n = len(h)
    config.stat.basic += 1
    for i in range(n, 0, -1):
        # Swap smallest with the last
        h.heapList[i], h.heapList[1] = h.heapList[1], h.heapList[i]
        # Smallest is in the right place
        # Consider that element as deleted
        h.currentSize -= 1
        # downheap() the new root to the right place
        h.percDown(1)
        config.stat.swap += 1
        config.stat.basic += 7
    # Remove the 0
    h.heapList.pop(0)
    # Reverse as we are using a minheap
    h.heapList.reverse()
    a = h.heapList
