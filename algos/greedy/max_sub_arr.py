#!/usr/bin/env python3
from typing import Sequence, Union, Tuple
Number = Union[int, float]


def max_sub_arr(arr: Sequence[Number]) -> Tuple[Number, int, int]:
    sum_max = -float("inf")
    start = end = 0
    start_curr = 0
    sum_curr = 0
    for end_curr, i in enumerate(arr):
        if sum_curr <= 0:
            start_curr = end_curr
            sum_curr = i
        else:
            sum_curr += i
        if sum_curr > sum_max:
            sum_max = sum_curr
            start = start_curr
            end = end_curr
    return sum_max, start, end


def main() -> None:
    arr = [2, -1, 2, 3, 4, -5]
    print(max_sub_arr(arr))
    return


if __name__ == "__main__":
    main()
