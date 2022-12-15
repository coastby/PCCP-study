# [programmers] Level.2 더 맵게

"""
모든 음식의 지수가 K이상
섞어야 하는 최소 횟수
"""

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        now = heapq.heappop(scoville)
        if now < K:
            if scoville:
                second = heapq.heappop(scoville)
                heapq.heappush(scoville, now + 2*second)
                answer += 1
            else:
                break
        else:
            return answer
    return -1