"""
다익스트라

"""
import heapq

INF = int(1e9)


def dijkstra(start, d, graph):
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    d = [INF] * (N+1)
    for m in road:
        graph[m[0]].append((m[1], m[2]))
        graph[m[1]].append((m[0], m[2]))

    dijkstra(1, d, graph)
    result = [1]
    for i in range(2, N+1):
        if d[i] <= K:
            result.append(i)
    return len(result)

