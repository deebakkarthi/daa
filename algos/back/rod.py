#!/usr/bin/env python3
from typing import Sequence, Tuple, List
from typing import Union
import logging
import sys


Number = Union[int, float]
PRUNED = "\033[1m\033[91m"
END = "\033[0m"
SEARCHED = "\033[1m\033[92m"


def rod(profit_arr: Sequence[Number]) -> Tuple[Number, List[int]]:
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
        logging.debug(f"{PRUNED}{tab}+-{path_curr+[i]}S{END}")
        return profit_curr, path_curr
    path_curr.append(i)
    if len_curr + i == len_max:
        logging.debug(f"{SEARCHED}{tab}+-{path_curr}"
                      f"{profit_curr + profit_arr[i-1]}{END}")
        return profit_curr + profit_arr[i-1], path_curr
    ub = profit_curr + (len_max - len_curr)*best_unit_profit
    if ub < currmax:
        logging.debug(f"{PRUNED}{tab}+-{path_curr}B{END}")
        return profit_curr, path_curr
    profit_curr += profit_arr[i-1]
    logging.debug(f"{SEARCHED}{tab}+-{path_curr}{END}")
    for j in range(1, len(profit_arr)+1):
        profit, path = rod_rec(len_max, len_curr+i, best_unit_profit,
                               profit_arr, profit_curr, currmax, j,
                               path_curr.copy(), path_max, tab+"| ")
        if profit > currmax:
            currmax, path_max = profit, path
    return currmax, path_max


def logging_init(level=logging.INFO) -> None:
    logging.basicConfig(level=level, format="%(message)s")
    return


def usage() -> None:
    print("Usage: rod [-v|-h]")
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
    profit_arr = [1, 5, 8, 9, 10, 17, 17, 20]
    logging.info(rod(profit_arr))


if __name__ == "__main__":
    main()
