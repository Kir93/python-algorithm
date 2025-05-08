from heapq import heappop, heappush

def deijkstra(start):
    dist = [INF for _ in range(N+1)]
    dist[start]=0
    heap =[]
    heappush(heap, [0,start])
    while heap:
        weight,node = heappop(heap)
        
        if dist[node] < weight:
            continue
        
        for next, cost in G[node]:
            if dist[next]>weight+cost:
                dist[next] = weight + cost
                heappush(heap,[dist[next],next])
    
    return dist
    
INF = int(1e9)
T= int(input())
for _ in range(T):
    # global N,G
    N,M,K = map(int, input().split())
    s,g,h = map(int, input().split())
    
    G=[[]for _ in range(N+1)]
    
    for _ in range(M):
        u,v,w = map(int, input().split())
        G[u].append([v,w])
        G[v].append([u,w])
        
    candidate = {}
    for _ in range(K):
        candidate[int(input())]=1

    distFromS = deijkstra(s)
    if distFromS[g] > distFromS[h]:
        newStart = g
    elif distFromS[g] < distFromS[h]:
        newStart = h
        
    distFromNewS = deijkstra(newStart)
    answer = []
    for i in candidate:
        if distFromS[newStart] + distFromNewS[i] == distFromS[i]:
            answer.append(i)
    answer.sort()
    print(*answer)