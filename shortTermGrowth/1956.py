import sys
INF = int(1e9)

v, e = map(int, sys.stdin.readline().split()) # v개의 마을, e개의 도로

# 2차원 그래프, 모든 값을 무한으로 초기화
graph = [[INF] * (v + 1) for _ in range(v + 1)]   # 거리를 담는 테이블

# a -> b 마을 가는 도로 길이를 c로 넣기
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 1. 모든 정점에서 모든 정점으로 가는 최소 거리 구하기
for k in range(1, v + 1):
    for a in range(1, v + 1):   # 출발 노드
        for b in range(1, v + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 2. 자기자신 -> 자기자신 마을로 돌아오는 거리 중 최소값 구하기
result = INF
for i in range(1, v + 1):
    result = min(result, graph[i][i])

if result == INF:
    print(-1)
else:
    print(result)