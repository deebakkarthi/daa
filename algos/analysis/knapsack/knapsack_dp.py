#!/usr/bin/env python3

def knapsack_bottom_up(max_weight, benefit_arr, weight_arr):
    n = len(benefit_arr)
    b = table_gen(max_weight, n)
    for i in range(n+1):
        for w in range(max_weight+1):
            if i == 0 or w == 0:
                b[i][w] = 0
            elif weight_arr[i-1] <= w:
                b[i][w] = max(benefit_arr[i-1]+b[i-1][w-weight_arr[i-1]],
                              b[i-1][w])
            else:
                b[i][w] = b[i][w]
    return b[n][max_weight]

def knapsack_top_down( max_weight, benefit_arr, weight_arr,):
    n = len(benefit_arr)
    b = table_gen(max_weight, n)
    knapsack_rec(benefit_arr, weight_arr, b, n, max_weight)
    tmp = knapsack_place(b, weight_arr, max_weight)
    print(tmp)
    print(f"Weight:{sum([weight_arr[i-1] for i in tmp])},Benefit:{sum([benefit_arr[i-1] for i in tmp])}")
    return b[n][max_weight]

def knapsack_rec(benefit_arr, weight_arr, b, k, w):
    if k == 0 or w == 0:
        return b[k][w]
    if b[k][w] == 0:
        if weight_arr[k-1] > w:
            b[k][w] = knapsack_rec(benefit_arr, weight_arr, b, k-1, w)
        else:
            benefit_without_k = knapsack_rec(benefit_arr, weight_arr, b, k-1, w)
            benefit_with_k = knapsack_rec(benefit_arr, weight_arr, b, k-1,
                                          w-weight_arr[k-1]) + benefit_arr[k-1]
            if benefit_with_k > benefit_without_k:
                b[k][w] = benefit_with_k
            else:
                b[k][w] = benefit_without_k
    return b[k][w]

def knapsack_place(b, weight_arr, max_weight):
    i = len(weight_arr)
    k = max_weight
    item_arr = []
    for i in range(i,0,-1):
        if b[i][k] != b[i-1][k] and b[i][k] != 0:
            item_arr.append(i)
            k -= weight_arr[i-1]
    return item_arr


def table_gen(max_weight, n):
    b = [[0 for _ in range(max_weight+1)] for _ in range(n+1)]
    return b
