# [programmers] Level.2 주식가격

"""
가격이 떨어지지 않은 기간

price를 인덱스로 하는 배열
10:30
82
""연속적이다"" -> stack/queue 사용 가능하다
"""

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx, price in enumerate(prices):
        while stack:
            if stack[-1][1] > price:
                node = stack.pop()
                answer[node[0]] = idx - node[0]
            else:
                break
        stack.append((idx, price))
    for node in stack:
        answer[node[0]] = len(prices) - 1 - node[0]
    return answer


a = [1, 2, 3, 2, 3]
b = [3, 4, 5, 6, 4, 2, 3, 4] # [5,4,2,1,1,2,1,0]
print(solution(a))
print(solution(b))

"""
import heapq


def solution(prices):
    hq = []
    answer = [0] * (len(prices))
    for idx, p in enumerate(prices):
        while hq:
            node = heapq.heappop(hq)
            if -node[0] <= p:
                heapq.heappush(hq, node)
                break
            else:
                answer[node[1]] = idx - node[1]
        heapq.heappush(hq, (-p, idx))
    while hq:
        node = heapq.heappop(hq)
        answer[node[1]] = len(prices) - 1 - node[1]
    return answer
"""


