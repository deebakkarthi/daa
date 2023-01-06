#!/usr/bin/env python3
import knapsack_bb
import knapsack_dp
import random
import seaborn as sns
import matplotlib.pyplot as plt
from time import perf_counter_ns


def main():
    bb = list()
    dp = list()
    for i in range(1, 40):
        print(i)
        weight_arr = [random.randint(1,100) for _ in range(i)]
        benefit_arr = [random.randint(1,100) for _ in range(i)]
        max_weight = int(0.75*sum(weight_arr))

        start = perf_counter_ns()
        knapsack_bb.knapsack(max_weight, benefit_arr, weight_arr)
        end = perf_counter_ns()
        bb.append(end-start)

        start = perf_counter_ns()
        knapsack_dp.knapsack_bottom_up(max_weight, benefit_arr, weight_arr)
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
