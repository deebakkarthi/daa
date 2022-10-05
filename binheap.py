#!/usr/bin/env python3
from stats import stats

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
            self.basic += 7
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
