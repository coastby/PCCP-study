# [programmers] Level.2 기능개발

"""
진도가 100%일 때 서비스에 반영
먼저 배포되어야 하는 순서대로

각 배포마다 몇개의 기능이 배포되는지

하나씩 빼서 100되는지 확인하기

1. 각 기능을 하나씩 가져와서 개발하는데 얼마나 걸리는 지 (wd) 구한다.
    1. 이전에 꺼냈던 것보다 작으면 같이 배포를 할 수 있으므로 cnt를 1올린다.
    2. 더 크면 다음 배포에 포함되므로 앞의 cnt를 answer에 추가하고, 작업 날짜를 초기화한다.
2. speed를 가져오기 위한 idx를 1 늘린다.
3. 사실 idx를 쓸거면 deque를 사용하지 않았어도 되었을 것 같다.
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
