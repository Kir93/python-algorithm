from sys import stdin
input = stdin.readline
from collections import deque

# 동 서 남 북
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
change_dir = ((2, 3), (2, 3), (0, 1), (0, 1))

def bfs():
    visited = [[[0] * 4 for _ in range(C)] for _ in range(R)]
    visited[sr-1][sc-1][sd-1] = 1
    Q = deque([(sr-1, sc-1, sd-1, 0)])
    while Q:
        r, c, d, cnt = Q.popleft()
        if (r, c, d) == (gr-1, gc-1, gd-1):     # (목표위치와 방향)에 도착하면 cnt 리턴
            return cnt

        # 1, 2, 3칸 직진
        for dis in range(1, 4):
            nr = r + dr[d] * dis
            nc = c + dc[d] * dis
            nd = d
            # 맵 벗어나거나 벽 만나면 break
            if not (0 <= nr < R and 0 <= nc < C) or A[nr][nc]:
                break
            if visited[nr][nc][nd]:
                continue
            Q.append((nr, nc, nd, cnt+1))
            visited[nr][nc][nd] = 1

        # 방향 바꾸기
        for nd in change_dir[d]:
            if visited[r][c][nd]:
                continue
            Q.append((r, c, nd, cnt+1))
            visited[r][c][nd] = 1

# main
R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sd = map(int, input().split())
gr, gc, gd = map(int, input().split())

print(bfs())
