import heapq
INF = int(1e9)

N, K = map(int, input().split())
distance = [INF] * 100001

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for n in (now+1, now-1, now*2):
            if n < 0 or n > 100000:
                continue

            cost = dist
            if n != now*2:
                cost = dist + 1

            if cost < distance[n]:
                distance[n] = cost
                q.append((cost, n))

dijkstra(N)
print(distance[K])