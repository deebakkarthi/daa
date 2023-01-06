#!/usr/bin/env python3
import max_sub_arr_greed
import max_sub_arr_dp
import max_sub_arr_bb
import max_sub_arr_div
import random
import seaborn as sns
import matplotlib.pyplot as plt
from time import perf_counter_ns


def main():
    bb = list()
    dp = list()
    div = list()
    greed = list()
    for i in range(10, 100):
        print(i)
        arr = [random.randint(10, 200) for _ in range(i)]

        start = perf_counter_ns()
        max_sub_arr_bb.max_sub_arr_bb(arr)
        end = perf_counter_ns()
        bb.append(end-start)

        start = perf_counter_ns()
        max_sub_arr_dp.max_sub_arr_dp(arr)
        end = perf_counter_ns()
        dp.append(end-start)

        start = perf_counter_ns()
        max_sub_arr_div.max_sub_arr_div(arr, 0, len(arr)-1)
        end = perf_counter_ns()
        div.append(end-start)

        start = perf_counter_ns()
        max_sub_arr_greed.max_sub_arr_greed(arr)
        end = perf_counter_ns()
        greed.append(end-start)

    _, ax = plt.subplots()
    ax.set(yscale="log")
    sns.lineplot(ax=ax, data=bb, label="Branch and Bound")
    sns.lineplot(ax=ax, data=dp, label="Dynamic Programming")
    sns.lineplot(ax=ax, data=div, label="Divide and Conquer")
    sns.lineplot(ax=ax, data=greed, label="Kadane")
    plt.legend()
    plt.savefig('analysis.png')
    plt.show()
    return

if __name__ == "__main__":
    main()
