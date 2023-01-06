#!/usr/bin/env python3

def knapsack_bottom_up(max_weight, benefit_arr, weight_arr):
    ITER = 0
    n = len(benefit_arr)
    b = table_gen(max_weight, n)
    for i in range(n+1):
        for w in range(max_weight+1):
            ITER += 1
            if i == 0 or w == 0:
                b[i][w] = 0
            elif weight_arr[i-1] <= w:
                b[i][w] = max(benefit_arr[i-1]+b[i-1][w-weight_arr[i-1]],
                              b[i-1][w])
            else:
                b[i][w] = b[i][w]
    tmp = knapsack_place(b, weight_arr, max_weight)
    print(f"Weight:{sum([weight_arr[i-1] for i in tmp])},Benefit:{sum([benefit_arr[i-1] for i in tmp])}")
    print(f"PROJ:{len(weight_arr)*max_weight}")
    print(f"ITER:{ITER}")
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

def main():
    weight_arr = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    benefit_arr = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    max_weight = 269
    print(f"weights:{weight_arr}")
    print(f"benefits:{benefit_arr}")
    print(knapsack_top_down(max_weight, benefit_arr, weight_arr))
    print(knapsack_bottom_up(max_weight, benefit_arr, weight_arr))

    weight_arr = [92,4,43,83,84,68,92,82,6,44,32,18,56,83,25,96,70,48,14,58]
    benefit_arr = [44,46,90,72,91,40,75,35,8,54,78,40,77,15,61,17,75,29,75,63]
    max_weight = 878
    print(f"weights:{weight_arr}")
    print(f"benefits:{benefit_arr}")
    print(knapsack_top_down(max_weight, benefit_arr, weight_arr))
    print(knapsack_bottom_up(max_weight, benefit_arr, weight_arr))

    weight_arr = [80, 82, 85, 70, 72, 70, 66, 50, 55, 25, 50, 55, 40, 48, 59, 32, 22,
                  60, 30, 32, 40, 38, 35, 32, 25, 28, 30, 22, 50, 30, 45, 30, 60, 50, 20,
                  65, 20, 25, 30, 10, 20, 25, 15, 10, 10, 10, 4, 4, 2, 1]
    benefit_arr = [220, 208, 198, 192, 180, 180, 165, 162, 160, 158, 155, 130, 125,
                   122, 120, 118, 115, 110, 105, 101, 100, 100, 98, 96, 95, 90, 88, 82,
                   80, 77, 75, 73, 72, 70, 69, 66, 65, 63, 60, 58, 56, 50, 30, 20, 15, 10, 8,
                   5, 3, 1]
    max_weight = 1000
    print(f"weights:{weight_arr}")
    print(f"benefits:{benefit_arr}")
    print(knapsack_top_down(max_weight, benefit_arr, weight_arr))
    print(knapsack_bottom_up(max_weight, benefit_arr, weight_arr))

    weight_arr = [40, 27, 5, 21, 51, 16, 42, 18, 52, 28, 57, 34, 44, 43, 52, 55, 53,
                  42, 47, 56, 57, 44, 16, 2, 12, 9, 40, 23, 56, 3, 39,16, 54, 36, 52, 5, 53,
                  48, 23, 47, 41, 49, 22, 42, 10, 16, 53, 58, 40, 1, 43, 56, 40, 32, 44, 35,
                  37, 45, 52, 56, 40, 2, 23,49, 50, 26, 11, 35, 32, 34, 58, 6, 52, 26, 31,
                  23, 4, 52, 53, 19]
    benefit_arr = [199, 194, 193, 191, 189, 178, 174, 169, 164, 164, 161, 158, 157,
                   154, 152, 152, 149, 142, 131, 125, 124, 124, 124, 122, 119, 116, 114,
                   113, 111, 110, 109, 100, 97, 94, 91, 82, 82, 81, 80, 80, 80, 79, 77, 76,
                   74, 72, 71, 70, 69,68, 65, 65, 61, 56, 55, 54, 53, 47, 47, 46, 41, 36, 34,
                   32, 32,30, 29, 29, 26, 25, 23, 22, 20, 11, 10, 9, 5, 4, 3, 1]
    max_weight = 1173
    print(f"weights:{weight_arr}")
    print(f"benefits:{benefit_arr}")
    print(knapsack_top_down(max_weight, benefit_arr, weight_arr))
    print(knapsack_bottom_up(max_weight, benefit_arr, weight_arr))

    weight_arr = [54, 95, 36, 18, 4, 71, 83, 16, 27, 84, 88, 45, 94, 64, 14, 80, 4, 23,
                  75, 36, 90, 20, 77, 32, 58, 6, 14, 86, 84, 59, 71, 21, 30, 22, 96, 49, 81,
                  48, 37, 28, 6, 84, 19, 55, 88, 38, 51, 52, 79, 55, 70, 53, 64, 99, 61, 86,
                  1, 64, 32, 60, 42, 45, 34, 22, 49, 37, 33, 1, 78, 43, 85, 24, 96, 32, 99,
                  57, 23, 8, 10, 74, 59, 89, 95, 40, 46, 65, 6, 89, 84, 83, 6, 19, 45, 59,
                  26, 13, 8, 26, 5, 9]
    benefit_arr = [297, 295, 293, 292, 291, 289, 284, 284, 283, 283, 281, 280, 279,
                   277, 276, 275, 273,264, 260, 257, 250, 236, 236, 235, 235, 233, 232,
                   232, 228, 218, 217, 214, 211, 208, 205, 204, 203, 201, 196, 194, 193,
                   193, 192, 191, 190, 187, 187, 184, 184, 184, 181, 179, 176, 173, 172,
                   171, 160, 128, 123, 114, 113, 107, 105, 101, 100, 100, 99, 98, 97, 94,
                   94, 93, 91, 80, 74, 73, 72, 63, 63, 62, 61, 60, 56, 53, 52, 50, 48, 46,
                   40, 40, 35, 28, 22, 22, 18, 15, 12, 11, 6, 5]
    max_weight = 3818
    print(f"weights:{weight_arr}")
    print(f"benefits:{benefit_arr}")
    print(knapsack_bottom_up(max_weight, benefit_arr, weight_arr))

if __name__ == "__main__":
    main()
