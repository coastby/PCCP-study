# [programmers] Level.2 프린터
"""
5:40

내가 요청한 문서가 언제 인쇄되는지
큐
119111
19111l
9111l1
111l1 9
11l1 91
1l1 911
l1 9111


"""
import heapq
from collections import deque


def solution(priorities, location):
    queue = deque()
    for idx, val in enumerate(priorities):
        queue.append((val, idx))
    cnt = 0
    while True:
        now = queue.popleft()
        if now[0] == max(priorities):
            cnt += 1
            priorities[now[1]] = 0
            if now[1] == location:
                break
        else:
            queue.append(now)
    return cnt

arr = [2, 1, 3, 2]
print(solution(arr, 2))

"""
def solution(priorities, location):
    queue = deque()
    for idx, val in enumerate(priorities):
        queue.append((val, idx))
    cnt = 0
    maxVal = max(priorities)
    while True:
        now = queue.popleft()
        if now[0] == maxVal:
            cnt += 1
            if now[1] == location:
                break
            priorities.remove(maxVal)
            maxVal = max(priorities)
        else:
            queue.append(now)
    return cnt
"""



"""
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1   
    return answer
"""