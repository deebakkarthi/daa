#!/usr/bin/env python3
from typing import Sequence, Union, Tuple, List
import logging
import sys


Number = Union[int, float]
PRUNED = "\033[1m\033[91m"
END = "\033[0m"
SEARCHED = "\033[1m\033[92m"


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
        logging.debug(f"{PRUNED}{tab}+-{path}Overweight{END}")
        return currmax
    if i == len(weight_arr)-1:
        logging.debug(f"{SEARCHED}{tab}+-{path}{v}{END}")
        return v
    else:
        b = v + (max_weight-w)*(benefit_arr[i+1]/weight_arr[i+1])
        if b < currmax:
            logging.debug(f"{PRUNED}{tab}+-{path}{b:.2f}<{currmax}{END}")
            return currmax
        logging.debug(f"{SEARCHED}{tab}+-{path}{v}")
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr,
                                            weight_arr, w+weight_arr[i+1],
                                            v+benefit_arr[i+1], i+1, currmax,
                                            tab+"| ", path.copy()+[i+1]))
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr,
                                            weight_arr, w, v, i+1, currmax,
                                            tab+"| ", path.copy()))
    return currmax

def logging_init(level=logging.INFO) -> None:
    logging.basicConfig(level=level, format="%(message)s")
    return


def usage() -> None:
    print("Usage: knapsack [-v|-h]")
    exit()

def main() -> None:
    level = logging.INFO
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "-v":
                level = logging.DEBUG
            case "-h":
                usage()
            case _:
                usage()
    logging_init(level)

    weight_arr = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    benefit_arr = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    max_weight = 269
    logging.info(unit_sort(benefit_arr, weight_arr))
    logging.info(knapsack(max_weight, benefit_arr, weight_arr))

    weight_arr = [92,4,43,83,84,68,92,82,6,44,32,18,56,83,25,96,70,48,14,58]
    benefit_arr = [44,46,90,72,91,40,75,35,8,54,78,40,77,15,61,17,75,29,75,63]
    max_weight = 878
    logging.info(unit_sort(benefit_arr, weight_arr))
    logging.info(knapsack(max_weight, benefit_arr, weight_arr))

    weight_arr = [80, 82, 85, 70, 72, 70, 66, 50, 55, 25, 50, 55, 40, 48, 59,
                  32, 22, 60, 30, 32, 40, 38, 35, 32, 25, 28, 30, 22, 50, 30,
                  45, 30, 60, 50, 20, 65, 20, 25, 30, 10, 20, 25, 15, 10, 10,
                  10, 4, 4, 2, 1]
    benefit_arr = [220, 208, 198, 192, 180, 180, 165, 162, 160, 158, 155, 130,
                   125, 122, 120, 118, 115, 110, 105, 101, 100, 100, 98, 96,
                   95, 90, 88, 82, 80, 77, 75, 73, 72, 70, 69, 66, 65, 63, 60,
                   58, 56, 50, 30, 20, 15, 10, 8, 5, 3, 1]
    max_weight = 1000
    logging.info(unit_sort(benefit_arr, weight_arr))
    logging.info(knapsack(max_weight, benefit_arr, weight_arr))

    return

if __name__ == "__main__":
    main()
