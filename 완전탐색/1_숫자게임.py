# [Programmers] Level.3 숫자 게임

"""
B팀이 얻을 수 있는 최대 승점
팀원 1 ~ 100,000
숫자 1 ~ 1,000,000,000

5 1 3 7 -> 7 5 3 1
2 2 6 8 -> 8 6 2 2
---
10 8 4 4 2 2 2 2 2 1 1 1
11 6 6 6 4 3 3 3 3 1 1 1

10 8 4 4 2 2 2 2 2 1 1 1
11 1 6 6 4 3 3 3 3 1 1 6
---
10 8 7 6
6  8 7 9
---
전략) 둘 다 순서대로 정렬 후 가장 큰 수를 대보고 안 되면 가장 작은 수 넣기
같으면..?
"""
from collections import deque

def solution (A, B):
    A = sorted(A, reverse=True)
    B = deque(sorted(B, reverse=True))
    print(sorted(B))
    answer = 0

    for i in range(len(A)):
        if A[i] >= B[0]:
            B.pop()
        else:
            B.popleft()
            answer += 1
    return answer


A = [5,1,3,7]
B = [2,2,6,8]
print(solution(A, B))