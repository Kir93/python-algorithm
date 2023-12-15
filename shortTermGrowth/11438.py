import sys
input = sys.stdin.readline

max_depth = 100000
LOG = 21
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


tree = [[0 for _ in range(LOG)] for _ in range(n+1)]

visit = [1]
level = [-1 for _ in range(n+1)]
level[1] = 0

while visit:
    now = visit.pop()

    for next_node in graph[now]:
        if level[next_node] != -1:
            continue

        level[next_node] = level[now] + 1
        tree[next_node][0] = now
        visit.append(next_node)


for i in range(1, LOG):
    for j in range(1, n+1):
        tree[j][i] = tree[tree[j][i - 1]][i - 1]

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    if level[a] < level[b]:
        a, b = b, a

    for i in range(LOG-1, -1, -1):
        if level[a] - level[b] >= 2 ** i:
            a = tree[a][i]

    if a == b:
        print(a)
        continue

    for i in range(LOG-1, -1, -1):
        if tree[a][i] != tree[b][i]:
            a = tree[a][i]
            b = tree[b][i]

    print(tree[a][0])