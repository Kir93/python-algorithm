import sys
from collections import deque

def BFS(x, y):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    cnt = 1

    while q:
        current_x, current_y = q.pop()
        zeros[current_x][current_y] = group 
        for dx, dy in dir:
            next_x, next_y = current_x + dx, current_y + dy
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M: continue
            if visited[next_x][next_y]: continue
            if not board[next_x][next_y]: 
                q.append([next_x, next_y])
                visited[next_x][next_y] = 1
                cnt += 1
    return cnt

def countMoves(x, y):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    candidates = set()
    for dx, dy in dir:
        next_x, next_y = x + dx, y + dy
        if next_x < 0 or next_y < 0 or next_x >= N or next_y >= M: continue
        if not zeros[next_x][next_y]: continue
        candidates.add(zeros[next_x][next_y])
    cnt = 1
    for c in candidates:
        cnt += info[c]
        cnt = cnt % 10
    return cnt

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
zeros = [[0 for _ in range(M)] for _ in range(N)]
group = 1
info = {}
for i in range(N):
    for j in range(M):
        if not board[i][j] and not visited[i][j]: 
            cnt = BFS(i, j)
            info[group] = cnt
            group += 1

answer = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]:
            answer[i][j] = countMoves(i, j)

for i in range(N):
    print(''.join(map(str, answer[i])))