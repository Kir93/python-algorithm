import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0: 
                    q.append((nx, ny))
                elif cheeze[nx][ny] == 1: 
                    melt.append((nx, ny))
                    
    for x, y in melt:
        cheeze[x][y] = 0 
    return len(melt) 

n, m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i]) 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[0] * m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    if cnt == 0: 
        print(time, meltCnt, sep='\n') 
        break
    time += 1