#!/usr/bin/env python3
from typing import Sequence, Union, Tuple, List

Number = Union[int, float]


def unit_sort(benefit_arr: Sequence[Number],
              weight_arr: Sequence[Number]) -> List[Tuple[Number]]:
    return list(zip(*sorted(zip(benefit_arr, weight_arr),
                       key=lambda x: x[0]/x[1],
                       reverse=True)))


def knapsack(max_weight: Number, benefit_arr: Sequence[Number],
             weight_arr: Sequence[Number]) -> Number:
    benefit_arr, weight_arr = unit_sort(benefit_arr, weight_arr)
    w = 0
    v = 0
    i = 0
    currmax = -1
    currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                                        w+weight_arr[i], v+benefit_arr[i], i,
                                        currmax, "", [i]))
    currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                                        w, v, i, currmax, "", []))
    return currmax


def knapsack_rec(max_weight: Number, benefit_arr: Sequence[Number],
                 weight_arr: Sequence[Number], w: Number, v: Number, i: int,
                 currmax: Number, tab: str, path: List[int]) -> Number:
    if w > max_weight:
        return currmax
    if i == len(weight_arr)-1:
        return v
    else:
        b = v + (max_weight-w)*(benefit_arr[i+1]/weight_arr[i+1])
        if b < currmax:
            return currmax
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr,
                                            weight_arr, w+weight_arr[i+1],
                                            v+benefit_arr[i+1], i+1, currmax,
                                            tab+"| ", path.copy()+[i+1]))
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr,
                                            weight_arr, w, v, i+1, currmax,
                                            tab+"| ", path.copy()))
    return currmax
