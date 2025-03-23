import sys;
from collections import deque
from math import inf

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    
    # 시작은 0, 끝은 N + M + 1
    start = 0; end = N + M + 1; length = end + 1
    flow = [[0] * length for _ in range(length)]
    capacity = [[0] * length for _ in range(length)]
    cost = [[0] * length for _ in range(length)] # 월급을 비용으로 생각한다.
    connect = [[] for _ in range(length)]

    for i in range(1, N + 1):
        # 시작과 직원을 연결
        # 각 직원은 한 개의 일만 할 수 있으므로 용량은 1
        connect[start].append(i)
        connect[i].append(start)
        capacity[start][i] = 1

        n, *lst = map(int, input().split())
        for k in range(0, n * 2, 2):
            j = lst[k] + N; c = lst[k + 1] # 일의 번호는 직원 수만큼 더해줘야 한다.
            connect[i].append(j)
            connect[j].append(i)
            capacity[i][j] = 1
            cost[i][j] = c
            cost[j][i] = -c # 역방향 간선의 비용은 음의 비용으로 설정

    # 일과 끝을 연결
    # 각 일을 담당하는 사람은 1명이므로 용량은 1
    for i in range(N + 1, N + M + 1):
        connect[i].append(end)
        connect[end].append(i)
        capacity[i][end] = 1

    answer = [0, 0] # 일의 개수와 월급의 최솟값
    while True:
        # SPFA
        prev = [-1] * length
        distance = [inf] * length # 거리
        q = [False] * length # 큐에 원소가 있는지 판별할 배열
        queue = deque([start])
        distance[start] = 0
        q[start] = True
        while queue:
            here = queue.popleft()
            q[here] = False
            for there in connect[here]:
                if capacity[here][there] - flow[here][there] > 0 and distance[there] > distance[here] + cost[here][there]:
                    distance[there] = distance[here] + cost[here][there] # 거리 갱신
                    prev[there] = here # prev 갱신
                    if not q[there]: # 큐에 없다면 넣어준다.
                        queue.append(there)
                        q[there] = True

        # 끝 지점이 갱신이 되지 않았다면 경로가 없는 것이므로 break
        if prev[end] == -1:
            break
        # 유량은 어차피 1
        here = end
        while here != start:
            flow[prev[here]][here] += 1
            flow[here][prev[here]] -= 1
            answer[1] += cost[prev[here]][here] # 간선의 비용만큼 월급을 줘야 함
            here = prev[here]
        answer[0] += 1 # 유량이 처음에서 끝으로 흐른건 한 직원이 한 일을 할 수 있다는 것을 뜻함
    print(*answer, sep = '\n')

solve()