#!/usr/bin/env python3
import dance_bb
import dance_dp
import random
import seaborn as sns
import matplotlib.pyplot as plt
from time import perf_counter_ns


def main():
    bb = list()
    dp = list()
    for i in range(10, 100):
        score_arr = [random.randint(10, 200) for _ in range(i)]
        start = perf_counter_ns()
        dance_bb.dance_bb(score_arr)
        end = perf_counter_ns()
        bb.append(end-start)
        start = perf_counter_ns()
        dance_dp.dance_dp(score_arr)
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
