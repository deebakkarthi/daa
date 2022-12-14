#!/usr/bin/env python3
import random


def rod_top_down(price_arr, n):
    revenue_arr = [-1 for _ in range(n+1)]
    revenue_arr[0] = 0
    return rod_rec(price_arr, n, revenue_arr)


def rod_rec(price_arr, n, revenue_arr):
    if revenue_arr[n] == -1:
        tmp = -1
        # Recurrence relation
        # r[k] = max(p[i] + r[k-i])
        # i = [1,k]
        for i in range(1, n+1):
            tmp = max(tmp, price_arr[i] + rod_rec(price_arr, n-i, revenue_arr))
        revenue_arr[n] = tmp
    return revenue_arr[n]


def rod_bottom_up(price_arr, n):
    revenue_arr = [-1 for _ in range(n+1)]
    revenue_arr[0] = 0
    for i in range(1, n+1):
        tmp = -1
        for j in range(1, i+1):
            tmp = max(tmp, price_arr[j] + revenue_arr[i-j])
        revenue_arr[i] = tmp
    return revenue_arr[n]


if __name__ == "__main__":
    price_arr = [0,1,5,8,9,10,17,17,20]
    print(price_arr)
    print(rod_top_down(price_arr, 8))
    price_arr = sorted([random.randint(1,100)
                        for _ in range(random.randint(10,50))])
    price_arr[0] = 0
    print(price_arr)
    print(rod_top_down(price_arr, len(price_arr)-1))
