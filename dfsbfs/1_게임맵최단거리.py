# [prograrmmers] Level.2 게임 맵 최단거리
"""
9:45
"""
from collections import deque


move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solution(maps):
    n = len(maps[0])
    k = len(maps)
    visited = [[1]*n for _ in range(k)]
    queue = deque()
    queue.append([0, 0])
    while queue:
        now = queue.popleft()
        for m in move:
            x = m[0]+now[0]
            y = m[1]+now[1]
            if 0 <= x < n and 0 <= y < k and visited[y][x] == 1 and maps[y][x] == 1:
                visited[y][x] = visited[now[1]][now[0]] + 1
                queue.append([x, y])
    if visited[k-1][n-1] > 1:
        return visited[k-1][n-1]
    else:
        return -1





a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
b= [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(a))
print(solution(b))