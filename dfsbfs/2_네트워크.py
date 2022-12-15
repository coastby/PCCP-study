# [programmers] Level.3 네트워크

"""
서로소집합을 생각했다가 BFS와 짬뽕이 되었다.
"""

from collections import deque

def bfs(n, computers, par):
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        for i in range(len(computers[now])):
            if computers[now][i] == 1 and i != now and par[i] == i:
                queue.append(i)
                par[i] = now


def solution(n, computers):
    par = [i for i in range(len(computers))]
    cnt = 0
    for i in par:
        if par[i] == i:
            bfs(i, computers, par)
            cnt += 1
    return cnt