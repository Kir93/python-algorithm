from collections import deque
INF = 1 << 63
MAX = 1000

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    lattice = []
    for _ in range(n):
        lattice.append(list(map(int, input().split())))

    connect = [[] for _ in range(n * m + 2)]
    flow = [dict() for _ in range(n * m + 2)]
    capacity = [dict() for _ in range(n * m + 2)]


    def add_edge(u, v, cap):
        connect[u].append(v)
        flow[u][v] = 0
        capacity[u][v] = cap


    source, sink = n * m, n * m + 1

    for i in range(n):
        for j in range(m):
            if i + j & 1:
                cnt = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if ni in range(n) and nj in range(m):
                        cnt += 1
                        add_edge(i * m + j, ni * m + nj, MAX)
                        add_edge(ni * m + nj, i * m + j, 0)
                add_edge(source, i * m + j, cnt * MAX - lattice[i][j])
                add_edge(i * m + j, source, 0)
            else:
                cnt = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if ni in range(n) and nj in range(m):
                        cnt += 1
                add_edge(i * m + j, sink, cnt * MAX - lattice[i][j])
                add_edge(sink, i * m + j, 0)

    net_flow = 0


    def bfs():
        for i in range(n * m + 2):
            level[i] = -1
        level[source] = 0
        queue = deque([source])

        while queue:
            u = queue.popleft()
            for v in connect[u]:
                if capacity[u][v] - flow[u][v] > 0 > level[v]:
                    queue.append(v)
                    level[v] = level[u] + 1
        return level[sink] >= 0


    def dfs(u, dest, max_flow):
        if u == dest:
            return max_flow

        for i in range(pointer[u], len(connect[u])):
            v, pointer[u] = connect[u][i], i
            if level[v] == level[u] + 1 and capacity[u][v] > flow[u][v]:
                flow_change = dfs(v, dest, min(capacity[u][v] - flow[u][v], max_flow))
                if flow_change > 0:
                    flow[u][v] += flow_change
                    flow[v][u] -= flow_change
                    return flow_change
        return 0


    level = [-1] * (n * m + 2)
    while bfs():
        pointer = [0 for _ in range(n * m + 2)]
        while True:
            flow_change = dfs(source, sink, INF)
            if flow_change == 0:
                break
            net_flow += flow_change

    print(((m - 1) * n + (n - 1) * m) * MAX - net_flow)