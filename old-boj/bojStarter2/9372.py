import sys
input = sys.stdin.readline

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    check = [0]*(N+1)
    check[1] = 0
    cnt = dfs(1, 0)
    print(cnt)