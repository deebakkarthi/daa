#!/usr/bin/env python3
from typing import Sequence, Tuple
import random


def max_sub_arr_bb(arr: Sequence[int]) -> Tuple[float, Tuple[int, int]]:
    currmax = -float("inf")
    maxind = (0,0)
    for i in range(0, len(arr)):
        for j in  range(i, len(arr)):
            if max_sub_arr_rec(arr, i, j) > currmax:
                currmax = max_sub_arr_rec(arr, i, j)
                maxind = i,j
    return currmax, maxind


def max_sub_arr_rec(arr: Sequence[int], i: int, j: int) -> int:
    return sum(arr[i:j])
