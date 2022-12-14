#!/usr/bin/env python3
import random

def dance(score_arr):
    ITER = 0
    n = len(score_arr)
    max_score = [-1 for _ in range(n)]
    songs_to_dance = [[i] for i in range(n)]
    # Latter Half to be the original scores
    max_score[(n-4)//2:] = score_arr[(n-4)//2:]
    for i in range((n-4)//2,-1,-1):
        tmp = -1
        tmp_ind = 2*i+2
        # Finding the next song to dance from 2*k+2 to n
        # Recurrence relation
        # m[k] = s[k] + max(m[2k+2:end])
        for k,v in tuple(enumerate(max_score))[2*i+2:]:
            ITER += 1
            if v >= tmp:
                tmp = v
                tmp_ind = k
        max_score[i] = score_arr[i] + tmp
        songs_to_dance[i].extend(songs_to_dance[tmp_ind])
    tmp = tuple(enumerate(max_score))
    tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
    print(f"PROJ:{len(score_arr)**2//4}")
    print(f"ITER:{ITER}")
    return max_score[tmp[0][0]], songs_to_dance[tmp[0][0]]

    
if __name__ == "__main__":
    score_arr = [random.randint(1,100) for _ in range(random.randint(10,100))]
    print(score_arr)
    print(*dance(score_arr))
