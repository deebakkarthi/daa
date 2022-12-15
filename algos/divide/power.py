#!/usr/bin/env python3

def power(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        if n%2 == 1:
            return power(a, (n-1)//2) * power(a, n//2) * a
        else:
            tmp = power(a,n//2)
            return tmp * tmp
