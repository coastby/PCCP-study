# [programmers] Level.3 가장 먼 노드

"""
1번 노드에서 가장 멀리 떨어진 노드가 몇 개인지

"""

from collections import deque


def make_graph(graph, edge):
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])


def solution(n, edge):
    answer = 0
    visited = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]

    make_graph(graph, edge)

    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        for node in graph[now]:
            order = visited[now] + 1
            if visited[node] > order or visited[node] == 0:
                visited[node] = order
                queue.append(node)

    return visited[2:].count(max(visited[2:]))