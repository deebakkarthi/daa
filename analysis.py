#!/usr/bin/env python3
import sys
from time import perf_counter_ns
import tracemalloc
from functools import partial
from random import random

import config

from iquicksort import qsort
from mergesort import msort
from iheapsort import hsort
from insertionsort import isort
from bucketsort import bsort

def usage():
    print("Usage: analysis SORT\nSORT:\nq - Quick Sort\nm - Merge Sort\n"\
          "h - Heap Sort\ni - Insertion Sort\nb - Bucket Sort")

def measure(arr):
    tracemalloc.start()
    config.stat.time = perf_counter_ns()
    func(arr)
    config.stat.time = perf_counter_ns() - config.stat.time
    config.stat.mem = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    print(len(arr),config.stat,sep=",")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(0)

    config.init()
    arr = list()

    # New switch case equivalent in python 3.10
    match sys.argv[1]:
        case "q":
            func = partial(qsort, start=0, end=None)
            sys.stdout = open("data/quicksort", 'w')
        case "m":
            func = msort
            sys.stdout = open("data/mergesort", 'w')
        case "h":
            func = hsort
            sys.stdout = open("data/heapsort", 'w')
        case "i":
            func = isort
            sys.stdout = open("data/insertionsort", 'w')
        case "b":
            func = partial(bsort,k=10)
            sys.stdout = open("data/bucketsort", 'w')
        case _:
            usage()
            exit(0)

    for i in range(100,10000):
        del arr
        arr = [random() for _ in range(i)]
        measure(arr)
        del config.stat
        config.init()
