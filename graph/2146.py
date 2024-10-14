from collections import deque
import sys
input = sys.stdin.readline
 
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    maps[x][y] = mark
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
 
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = mark
                    visited[nx][ny] = True
 
def bfs2(island):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            if maps[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != island and maps[nx][ny] != 0:
                    return dist[x][y]
                if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
 
mark = 1
for x in range(n):
    for y in range(n):
        if maps[x][y] == 1 and not visited[x][y]:
            island_cnt = bfs(x, y)
            mark += 1
 
result = sys.maxsize
for island in range(1, mark):
    result = min(result, bfs2(island))
 
print(result)