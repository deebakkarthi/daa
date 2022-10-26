#!/usr/bin/env python3

def isort(a):
    for i in range(1, len(a)):
        j = i
        # Move the element leftward until a smaller element is encountered
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
