import sys
from collections import defaultdict
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().rstrip().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(dist[end])

path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))