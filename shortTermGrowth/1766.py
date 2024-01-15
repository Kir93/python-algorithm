import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    in_degree[b] += 1
    graph[a].append(b)

queue = []

for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    current = heapq.heappop(queue)
    print(current, end=" ")

    for g in graph[current]:
        in_degree[g] -= 1

        if in_degree[g] == 0:
            heapq.heappush(queue, g)