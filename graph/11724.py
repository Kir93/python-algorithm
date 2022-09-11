def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
c = 0
for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            c += 1
            visited[i] = True
        else:
            dfs(i)
            c += 1
print(c)
