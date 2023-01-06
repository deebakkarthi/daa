#!/usr/bin/env python3
from typing import Sequence, Union, Tuple
import random
Number = Union[int, float]


def max_sub_arr(arr: Sequence[Number]) -> Tuple[Number, int, int]:
    sum_max = -float("inf")
    start = end = 0
    start_curr = 0
    sum_curr = 0
    for end_curr, i in enumerate(arr):
        # The subarray seen till now is 0. No use in keeping it
        if sum_curr <= 0:
            start_curr = end_curr
            sum_curr = i
        else:
            sum_curr += i
        # Updating global max
        if sum_curr > sum_max:
            sum_max = sum_curr
            start = start_curr
            end = end_curr
    return sum_max, start, end


def main() -> None:
    arr = [2, -1, 2, 3, 4, -5]
    print(arr)
    print(max_sub_arr(arr))
    arr = [random.randint(-100, 100) for _ in range(random.randint(10,20))]
    print(arr)
    print(max_sub_arr(arr))
    arr = [random.randint(-100, -1) for _ in range(random.randint(10,20))]
    print(arr)
    print(max_sub_arr(arr))
    arr = [random.randint(1, 100) for _ in range(random.randint(10,20))]
    print(arr)
    print(max_sub_arr(arr))
    return


if __name__ == "__main__":
    main()
