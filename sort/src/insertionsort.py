#!/usr/bin/env python3
import config


def isort(a):
    for i in range(1, len(a)):
        config.stat.basic += 1
        j = i
        # Move the element leftward until a smaller element is encountered
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
            config.stat.comp += 2
            config.stat.basic += 11
            config.stat.swap += 1
