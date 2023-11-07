from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    check = [[float('inf')] * W for _ in range(H)]
    check[sr][sc] = -1
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        if (r, c) == (gr, gc):
            return check[gr][gc]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            while True:
                if not (0 <= nr < H and 0 <= nc < W):
                    break
                if A[nr][nc] == "*":                 
                    break
                if check[nr][nc] < check[r][c] + 1:  
                    break
                Q.append((nr, nc))                   
                check[nr][nc] = check[r][c] + 1
                nr += dr[i]
                nc += dc[i]

W, H = map(int, input().split())
A, C = [], []
sr, sc, gr, gc = 0, 0, 0, 0
for i in range(H):
    A.append(list(input().strip()))
    for j in range(W):
        if A[i][j] == "C":
            C.append((i, j))
(sr, sc), (gr, gc) = C
print(bfs())