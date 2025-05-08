import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

N = int(input())
camp = list(map(int,input().split()))
capa = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(N+2)]
flow = [[0]*(N+2) for _ in range(N+2)]
work = [0]*(N+2)
level = [-1]*(N+2)

for i in range(N):
    if camp[i] == 1: capa[0][i+1] = inf
    elif camp[i] == 2: capa[i+1][N+1] = inf

result = 0
while True:
    # 레벨 그래프 생성
    level = [-1]*(N+2)
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next in range(N+2):
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                level[next] = level[now]+1
                bfs.append(next)
    if level[-1] == -1: break

    # 유량 생성
    work = [0]*(N+2)
    stack = [(0,inf)]
    while stack:
        now,cut = stack[-1]
        if now == N+1:
            for _ in range(level[N+1]):
                next,res = stack.pop()
                work[stack[-1][0]] -= 1
                flow[stack[-1][0]][next] += cut
                flow[next][stack[-1][0]] -= cut
            result += cut
        else:
            for next in range(work[now],N+2):
                work[now] += 1
                residual = capa[now][next]-flow[now][next]
                if residual > 0 and level[now]+1 == level[next]:
                    if cut > residual: cut = residual
                    stack.append((next,cut))
                    break
            else:
                stack.pop()

print(result)

visited = [False]*(N+2)
visited[0] = True
bfs = deque([0])
while bfs:
    now = bfs.popleft()
    for next in range(1,N+1):
        if not(visited[next]) and capa[now][next]-flow[now][next] > 0:
            visited[next] = True
            bfs.append(next)
A = []
B = []
for i in range(1,N+1):
    if visited[i]: A.append(i)
    else: B.append(i)
print(*A)
print(*B)