#!/usr/bin/env python3
import random


def max_sub_arr_dp(arr):
    n = len(arr)
    dp_table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    max_x = 0
    max_y = 0
    curr_max = -float("inf")
    for i in range(1,n+1):
        for j in range(i, n+1):
            dp_table[i][j] = dp_table[i][j-1] + arr[j-1]
            if dp_table[i][j] > curr_max:
                max_x = i-1
                max_y = j-1
                curr_max = dp_table[i][j]
    return curr_max, max_x, max_y
