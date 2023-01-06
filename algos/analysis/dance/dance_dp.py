#!/usr/bin/env python3

def dance_dp(score_arr):
    n = len(score_arr)
    max_score = [-1 for _ in range(n)]
    songs_to_dance = [[i] for i in range(n)]
    max_score[(n-4)//2:] = score_arr[(n-4)//2:]
    for i in range((n-4)//2,-1,-1):
        tmp = -1
        tmp_ind = 2*i+2
        for k,v in tuple(enumerate(max_score))[2*i+2:]:
            if v >= tmp:
                tmp = v
                tmp_ind = k
        max_score[i] = score_arr[i] + tmp
        songs_to_dance[i].extend(songs_to_dance[tmp_ind])
    tmp = tuple(enumerate(max_score))
    tmp = sorted(tmp, key=lambda x:x[1], reverse=True)
    return max_score[tmp[0][0]], songs_to_dance[tmp[0][0]]
