#!/usr/bin/env python3
from typing import Sequence, Tuple, List
from typing import Union


Number = Union[int, float]


def rod_bb(profit_arr: Sequence[Number]) -> Tuple[Number, List[int]]:
    best_unit_profit = max([v/(k+1) for k, v in enumerate(profit_arr)])
    len_max = len(profit_arr)
    currmax = 0
    path_max = []
    for i in range(1, len(profit_arr)+1):
        path_curr = []
        score, path = rod_rec(len_max, 0, best_unit_profit,
                              profit_arr, 0, currmax, i,
                              path_curr.copy(), path_max, "")
        if score > currmax:
            currmax, path_max = score, path
    return currmax, path_max


def rod_rec(len_max: int, len_curr: int, best_unit_profit: Number,
            profit_arr: Sequence[Number], profit_curr: Number,
            currmax: Number, i: int,
            path_curr: List[int],
            path_max: List[int],
            tab: str) -> Tuple[Number, List[int]]:
    if len_curr + i > len_max:
        return profit_curr, path_curr
    path_curr.append(i)
    if len_curr + i == len_max:
        return profit_curr + profit_arr[i-1], path_curr
    ub = profit_curr + (len_max - len_curr)*best_unit_profit
    if ub < currmax:
        return profit_curr, path_curr
    profit_curr += profit_arr[i-1]
    for j in range(1, len(profit_arr)+1):
        profit, path = rod_rec(len_max, len_curr+i, best_unit_profit,
                               profit_arr, profit_curr, currmax, j,
                               path_curr.copy(), path_max, tab+"| ")
        if profit > currmax:
            currmax, path_max = profit, path
    return currmax, path_max
