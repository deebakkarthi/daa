#!/usr/bin/env python3

def knapsack_bottom_up(max_weight, benefit_arr, weight_arr):
    n = len(benefit_arr)
    b = table_gen(max_weight, n)
    for i in range(1, n):
        for w in range(max_weight+1):
            if weight_arr[i] <= w:
                if benefit_arr[i] + b[i-1][w-weight_arr[i]] > b[i-1][w]:
                    b[i][w] = benefit_arr[i] + b[i-1][w-weight_arr[i]]
                else:
                    b[i][w] = b[i-1][w]
            else:
                b[i][w] = b[i-1][w]
    return b[-1][-1]

def knapsack_top_down( max_weight, benefit_arr, weight_arr,):
    n = len(benefit_arr)
    b = table_gen(max_weight, n)
    knapsack_rec(benefit_arr, weight_arr, b, n-1, max_weight)
    print(b)
    return b[-1][-1]

def knapsack_rec(benefit_arr, weight_arr, b, k, w):
    if b[k][w] != -1:
        return b[k][w]
    if weight_arr[k] > w:
        b[k][w] = knapsack_rec(benefit_arr, weight_arr, b, k-1, w)
    else:
        benefit_without_k = knapsack_rec(benefit_arr, weight_arr, b, k-1, w)
        benefit_with_k = knapsack_rec(benefit_arr, weight_arr, b, k-1, w-weight_arr[k]) + benefit_arr[k]
        b[k][w] = max(benefit_with_k, benefit_without_k)
    return b[k][w]

def table_gen(max_weight, n):
    b = [[-1 for _ in range(max_weight+1)] for _ in range(n)]
    b[0] = [0 for _ in range(max_weight+1)]
    for k,_ in enumerate(b):
        b[k][0] = 0
    return b

if __name__ == "__main__":
    weight_arr = [0, 95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    benefit_arr = [0, 55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    max_weight = 269
    print(knapsack_top_down(max_weight, benefit_arr, weight_arr))
