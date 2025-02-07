import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    cost = 0
    edges = []
    for _ in range(n):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u, v, w = edge
        if find(u) != find(v):
            union(u, v)
        else:
            cost += w
    print(cost)