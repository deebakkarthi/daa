#!/usr/bin/env python3
from math import inf


def cross(arr, low, high):
    mid = (low + high) // 2
    left_sum = -inf
    left_ind = mid
    tmp_sum = 0
    for i in range(mid,low-1,-1):
        tmp_sum += arr[i]
        if tmp_sum > left_sum:
            left_sum = tmp_sum
            left_ind = i
    right_sum = -inf
    right_ind = mid
    tmp_sum = 0
    for i in range(mid+1,high+1):
        tmp_sum += arr[i]
        if tmp_sum > right_sum:
            right_sum = tmp_sum
            right_ind = i
    return left_ind, right_ind, left_sum+right_sum


def max_sub_arr(arr, low, high):
    if low == high:
        return low, high, arr[low]
    else:
        mid = (low + high)// 2
        left_low, left_high, left_sum = max_sub_arr(arr, low, mid)
        right_low, right_high, right_sum = max_sub_arr(arr, mid+1, high)
        cross_low, cross_high, cross_sum = cross(arr, low, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
