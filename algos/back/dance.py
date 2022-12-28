#!/usr/bin/env python3
from typing import Sequence, List, Tuple
from typing import Union
import random


Number = Union[int, float]


def unit_sort(score_arr: Sequence[Number]) -> Sequence[Number]:
    tmp = sorted([(k, v/(k+1)) for k, v in enumerate(score_arr)],
                 key=lambda x: x[1], reverse=True)
    unit_score = []
    i = j = 0
    while i < len(score_arr):
        if tmp[i][0] >= j:
            unit_score.append(tmp[i][1])
            j += 1
        else:
            i += 1
    return unit_score


def dance(score_arr: Sequence[Number]) -> Tuple[Number, List[Number]]:
    unit_score = unit_sort(score_arr)
    score_max = 0
    score_curr = 0
    currtime = 0
    path_max = []
    i = 0
    for i in range(len(score_arr)):
        path_curr = []
        score, path = dance_rec(unit_score, score_arr, score_max,
                                score_curr, currtime,
                                i, path_curr, path_max)
        if score > score_max:
            score_max, path_max = score, path
    return score_max, path_max


def dance_rec(unit_score: Sequence[Number], score_arr: Sequence[Number],
              score_max: Number, score_curr: Number, currtime: int, i: int,
              path_curr: List[Number],
              path_max: List[Number]) -> Tuple[Number, List[Number]]:
    n = len(score_arr)
    if i < currtime:
        return score_curr, path_curr
    path_curr.append(i)
    if i == n-1:
        return score_curr + score_arr[i], path_curr
    bound = score_curr + (2*n + 2 - currtime)*unit_score[i+1]
    if bound < score_max:
        return score_curr, path_curr
    for j in range(i+1, n):
        score, path = dance_rec(unit_score, score_arr, score_max,
                                score_curr+score_arr[i], currtime+2*i+2,
                                j, path_curr.copy(), path_max)
        if score > score_max:
            score_max, path_max = score, path
    return score_max, path_max


def main() -> None:
    score_arr = [random.randint(1, 100) for _ in range(random.randint(20, 20))]
    print(score_arr)
    print(*dance(score_arr))
    return


if __name__ == "__main__":
    main()
