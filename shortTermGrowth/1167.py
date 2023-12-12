import sys
from collections import deque
input = sys.stdin.readline

V = int(input())

tree = [[] for _ in range(V+1)]

for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

visited = [-1]*(V+1)
visited[1] = 0

def DFS(node, dist):
    for v, d in tree[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            DFS(v, cal_dist)
    return
            
DFS(1, 0)
tmp = [0, 0]
for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1]*(V+1)
visited[tmp[0]] = 0
DFS(tmp[0], 0)

print(max(visited))