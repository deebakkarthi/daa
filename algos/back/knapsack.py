#!/usr/bin/env python3

def unit_sort(benefit_arr, weight_arr):
    return zip(*sorted(zip(benefit_arr, weight_arr),
                       key=lambda x: x[0]/x[1],
                       reverse=True))


def knapsack(max_weight, benefit_arr, weight_arr):
    benefit_arr, weight_arr = unit_sort(benefit_arr, weight_arr)
    w = 0
    v = 0
    i = 0
    currmax = -1
    currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                                        w+weight_arr[i], v+benefit_arr[i], i, currmax))
    currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                 w, v, i, currmax))
    return currmax


def knapsack_rec(max_weight, benefit_arr, weight_arr, w, v, i, currmax):
    if w > max_weight:
        return currmax
    if i == len(weight_arr)-1:
        return v
    else:
        b = v + (max_weight-w)*(benefit_arr[i+1]/weight_arr[i+1])
        if b < currmax:
            return currmax
        if i == len(weight_arr)-1:
            return b
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                     w+weight_arr[i+1], v+benefit_arr[i+1], i+1, currmax))
        currmax = max(currmax, knapsack_rec(max_weight, benefit_arr, weight_arr,
                     w, v, i+1, currmax))
    return currmax


if __name__ == "__main__":
    weight_arr = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    benefit_arr = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    max_weight = 269
    print(knapsack(max_weight, benefit_arr, weight_arr))

    weight_arr = [92,4,43,83,84,68,92,82,6,44,32,18,56,83,25,96,70,48,14,58]
    benefit_arr = [44,46,90,72,91,40,75,35,8,54,78,40,77,15,61,17,75,29,75,63]
    max_weight = 878
    print(knapsack(max_weight, benefit_arr, weight_arr))

    weight_arr = [80, 82, 85, 70, 72, 70, 66, 50, 55, 25, 50, 55, 40, 48, 59, 32, 22,
                  60, 30, 32, 40, 38, 35, 32, 25, 28, 30, 22, 50, 30, 45, 30, 60, 50, 20,
                  65, 20, 25, 30, 10, 20, 25, 15, 10, 10, 10, 4, 4, 2, 1]
    benefit_arr = [220, 208, 198, 192, 180, 180, 165, 162, 160, 158, 155, 130, 125,
                   122, 120, 118, 115, 110, 105, 101, 100, 100, 98, 96, 95, 90, 88, 82,
                   80, 77, 75, 73, 72, 70, 69, 66, 65, 63, 60, 58, 56, 50, 30, 20, 15, 10, 8,
                   5, 3, 1]
    max_weight = 1000
    print(knapsack(max_weight, benefit_arr, weight_arr))
