#!/usr/bin/env python3
import sys
from time import perf_counter_ns
import tracemalloc
from functools import partial
from random import random

import config

from iquicksort import qsort
from mergesort import msort
from bmergesort import bmsort
from bquicksort import bqsort
from iheapsort import hsort
from insertionsort import isort
from bucketsort import bsort

def usage():
    print("Usage: analysis SORT\nSORT:\nq - Quick Sort\nm - Merge Sort\n"\
          "h - Heap Sort\ni - Insertion Sort\nb - Bucket Sort\nbm - Better"\
          "Merge Sort\nbq - Better Quick Sort")

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
            sys.stdout = open("../res/csv/quicksort.csv", 'w')
        case "m":
            func = msort
            sys.stdout = open("../res/csv/mergesort.csv", 'w')
        case "h":
            func = hsort
            sys.stdout = open("../res/csv/heapsort.csv", 'w')
        case "i":
            func = isort
            sys.stdout = open("../res/csv/insertionsort.csv", 'w')
        case "b":
            func = partial(bsort)
            sys.stdout = open("../res/csv/bucketsort.csv", 'w')
        case "bm":
            func = partial(bmsort, start=0, end=None)
            sys.stdout = open("../res/csv/bmergesort.csv", 'w')
        case "bq":
            func = partial(bqsort, start=0, end=None)
            sys.stdout = open("../res/csv/bquicksort.csv", 'w')
        case _:
            usage()
            exit(0)
    # headers for csv files
    print("input_size,comp,swap,basic,time,mem")
    for i in range(10, 1000, 10):
        del arr
        arr = [random() for _ in range(i)]
        arr = sorted(arr,reverse=True)
        measure(arr)
        del config.stat
        config.init()
