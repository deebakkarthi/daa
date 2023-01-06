#!/usr/bin/env python3
from typing import Sequence, Tuple
import random


def max_sub_arr(arr: Sequence[int]) -> Tuple[float, Tuple[int, int]]:
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


def main() -> None:
    arr = [random.randint(-100,100) for _ in range(random.randint(10,20))]
    print([(k,v) for k,v in enumerate(arr)])
    print(max_sub_arr(arr))
    return


if __name__ == "__main__":
    main()
