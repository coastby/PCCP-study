# [programmers] Level.3 N으로 표현
"""
1차 시도
테스트 1, 8을 실패한다

계산을 하다보면 100001보다 큰수도 나올 수 있을텐데 이를 담을 수 없어서 그런듯하다
"""

def solution(N, number):
    DP = [set() for _ in range(9)]
    pre = [N, N*11, N*111, N*1111, N*11111, N*111111, N*1111111]
    for i in range(len(pre)):
        if pre[i] == number:
            return i+1
        DP[i+1].add(pre[i])
    for i in range(2, 9):
        for j in range(1, i):
            for k in DP[i-j]:
                for h in DP[j]:
                    DP[i].add(k+h)
                    DP[i].add(k-h)
                    DP[i].add(k*h)
                    if h != 0:
                        DP[i].add(k//h)
        if number in DP[i]:
            return i
    return -1



"""
1트
from collections import deque


def solution(N, number):
    nums = [N, N*11, N*111, N*1111, N*11111]
    DP = [0] * (100001)
    for i in range(len(nums)):
        if nums[i] == number:
            return i+1
        DP[nums[i]] = i+1
    queue = deque(nums)
    while queue:
        now = queue.popleft()
        for i in range(len(nums)):
            order = DP[now]+i+1
            l = [now+nums[i], now-nums[i], now//nums[i], now*nums[i]]
            for j in l:
                if 0 <= j <= 100000:
                    if DP[j] == 0 or DP[j] > order:
                        DP[j] = order
                        queue.append(j)
    if DP[number] > 8 or DP[number] == 0:
        return -1
    else:
        return DP[number]"""