#!/usr/bin/env python3
import rod_bb 
import rod_dp
import random
import seaborn as sns
import matplotlib.pyplot as plt
from time import perf_counter_ns


def main():
    bb = list()
    dp = list()
    for i in range(10, 100):
        print(i)
        price_arr = sorted([random.randint(10, 200) for _ in range(i)])

        start = perf_counter_ns()
        rod_bb.rod_bb(price_arr)
        end = perf_counter_ns()
        bb.append(end-start)

        start = perf_counter_ns()
        rod_dp.rod_bottom_up(price_arr, len(price_arr) - 1)
        end = perf_counter_ns()
        dp.append(end-start)

    _, ax = plt.subplots()
    ax.set(yscale="log")
    sns.lineplot(ax=ax, data=bb, label="Branch and Bound")
    sns.lineplot(ax=ax, data=dp, label="Dynamic Programming")
    plt.legend()
    plt.savefig('analysis.png')
    plt.show()
    return

if __name__ == "__main__":
    main()
