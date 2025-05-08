import sys
sys.setrecursionlimit(150000)

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

n, m, r = map(int, sys.stdin.readline().split())
line = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)

dfs(r)

for i in range(1, n+1):
    print(visited[i])