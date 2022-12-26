#!/usr/bin/env python3
from typing import Sequence
from typing import Union
Number = Union[int, float]


def rod(profit_arr: Sequence[Number]) -> Number:
    best_unit_profit = max([v/(k+1) for k, v in enumerate(profit_arr)])
    len_max = len(profit_arr)
    profit = 0
    for i in range(1, len(profit_arr)+1):
        profit = max(profit, rod_rec(len_max, 0, best_unit_profit,
                                     profit_arr, 0, profit, i))
    return profit


def rod_rec(len_max: int, len_curr: int, best_unit_profit: Number,
            profit_arr: Sequence[Number], profit_curr: Number,
            currmax: Number, i: int) -> Number:
    if len_curr + i > len_max:
        return profit_curr
    if len_curr + i == len_max:
        return profit_curr + profit_arr[i-1]
    ub = profit_curr + (len_max - len_curr)*best_unit_profit
    if ub < currmax:
        return profit_curr
    profit_curr += profit_arr[i-1]
    for j in range(1, len(profit_arr)+1):
        currmax = max(currmax, rod_rec(len_max, len_curr+i, best_unit_profit,
                                       profit_arr, profit_curr, currmax, j))
    return currmax


def main() -> None:
    profit_arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print(rod(profit_arr))


if __name__ == "__main__":
    main()
