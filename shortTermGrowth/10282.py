import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start, dp, graph):
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        w, n = heappop(heap)
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

t = int(input())
for _ in range(t):
    n, d, c = map(int ,input().split())
    graph = [[] for _ in range(n + 1)]
    dp = [inf] * (n + 1)
    heap = []
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dijkstra(c, dp, graph)

    cnt = 0
    ans = 0
    for i in dp:
        if i != inf:
            cnt += 1
            ans = max(ans, i)

    print(f"{cnt} {ans}")