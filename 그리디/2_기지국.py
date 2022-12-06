# [programmers] Level.3 기지국
"""
12:55
최소로 설치하면서 모든 아파트에 전파 전달
증설해야 하는 기지국 개수 반환

N : 아파트 개수
W : 전파 도달 거리
00010000001

올림
"""

import math

def solution(n, stations, w):
    answer = 0
    start = 1
    while True:
        if stations:
            station = stations[0]
            stations.remove(station)
            answer += math.ceil((station - w - start)/(w*2+1))
            start = station + w + 1
        else:
            if start <= n:
                answer += math.ceil((n - start + 1)/(w*2+1))
            break
    return answer
