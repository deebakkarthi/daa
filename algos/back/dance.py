#!/usr/bin/env python3
import random

def dance(score_arr):
    for i in range(len(score_arr)):
        print(dance_rec(score_arr, i))
    return

def dance_rec(score_arr, start):
    if 2*(start+1)+1 < len(score_arr):
        return score_arr[start] +\
                max(dance_rec(score_arr, i)
                    for i in range(2*(start+1)+1, len(score_arr)))
    else:
        return score_arr[start]


if __name__ == "__main__":
    score_arr = [random.randint(10,30) for _ in range(random.randint(10,100))]
    max_score = dance(score_arr)
