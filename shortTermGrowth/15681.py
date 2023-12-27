import sys
from array import array
input = sys.stdin.buffer.readline
N, R, Q = map(int, input().split())
tree = [array('I') for _ in range(N)]
for _ in range(1, N):
    u, v = map(int, input().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

sizes = array('I', [1]) * N
dfs = [(R - 1, 0)]
visited = bytearray(N)
visited[R - 1] = 1
while True:
    u, j = dfs[-1]
    if j < len(tree[u]):
        dfs[-1] = (u, j + 1)
        v = tree[u][j]
        if visited[v]:
            continue
        visited[v] = 1
        dfs.append((v, 0))
    else:
        v, _ = dfs.pop()
        if dfs:
            u, j = dfs[-1]
            sizes[u] += sizes[v]
        else:
            break

ans = array('I')
for _ in range(Q):
    u = int(input())
    ans.append(sizes[u - 1])

print('\n'.join(map(str, ans)))