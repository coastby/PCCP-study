# [programmers] Level.2 위장
"""
12:19
매일 다른 옷을 조합하여 입는다
서로 다른 옷의 조합 수
하루에 최소 하나 이상

카테고리 카운트
M, N -> (M+1)(N+1) - 1
"""

def solution(clothes):
    category = {}
    for cloth in clothes:
        if cloth[1] not in category.keys():
            category[cloth[1]] = 1
        else:
            category[cloth[1]] += 1
    answer = 1
    for c in category:
        answer = answer*(category[c]+1)

    return answer-1