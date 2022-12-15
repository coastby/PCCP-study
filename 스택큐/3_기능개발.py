# [programmers] Level.2 기능개발

"""
진도가 100%일 때 서비스에 반영
먼저 배포되어야 하는 순서대로

각 배포마다 몇개의 기능이 배포되는지

하나씩 빼서 100되는지 확인하기
"""
from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    cnt = 0
    idx = 0
    day = math.ceil((100-progresses[0])/speeds[0])
    while queue:
        now = queue.popleft()
        wd = math.ceil((100-now)/speeds[idx])
        if wd <= day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = wd
        idx += 1
    answer.append(cnt)
    return answer
