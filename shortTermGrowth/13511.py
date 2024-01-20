import sys
from collections import deque
from math import log2
input = sys.stdin.readline

# tree 입력, 정렬, 부모노드, depth 계산 부분 
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
    
parent = [[0, 0] for _ in range(N + 1)]
depth = [0] * (N + 1)
visit = [False] * (N + 1)
que = deque([1])
visit[1] = True

while que:
    now = que.popleft()
    for b, c in tree[now]:
        if not visit[b]:
            que.append(b)
            parent[b][0] = now
            parent[b][1] = c
            depth[b] = depth[now] + 1
            visit[b] = True

# 희소 테이블
logN = int(log2(N) + 1)
dp = [[[0, 0] for _ in range(logN)] for __ in range(N + 1)]

for i in range(N + 1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]

for j in range(1, logN):
    for i in range(1, N + 1):
        dp[i][j][0] = dp[dp[i][j - 1][0]][j - 1][0]
        dp[i][j][1] = dp[i][j - 1][1] + dp[dp[i][j - 1][0]][j - 1][1] 

# 쿼리문 입력, 처리 
M = int(sys.stdin.readline())
for _ in range(M):
    Query = list(map(int, input().split()))
    u, v = Query[1], Query[2]
    u2, v2 = u, v
    # 공통 조상 탐색 
    if depth[u2] < depth[v2]:
        u2, v2 = v2, u2
    diff = depth[u2] - depth[v2]
    for i in range(logN):
        if diff & 1 << i:
            u2 = dp[u2][i][0]
    if u2 == v2:
        lca = u2
    else:
        for i in range(logN - 1, -1, -1):
            if dp[u2][i][0] != dp[v2][i][0]:
                u2 = dp[u2][i][0]
                v2 = dp[v2][i][0]
        lca = dp[u2][0][0]
    if Query[0] == 1:
        cost = 0
        diff_u = depth[u] - depth[lca]
        diff_v = depth[v] - depth[lca]
        for i in range(logN):
            if diff_u & 1 << i:
                cost += dp[u][i][1]
                u = dp[u][i][0]
            if diff_v & 1 << i:
                cost += dp[v][i][1]
                v = dp[v][i][0]
        print(cost)
    else: 
        k = Query[3]
        # u 의 k - 1 조상을 계산
        if k <= depth[u] - depth[lca]: 
            diff = k - 1
            for i in range(logN):
                if diff & 1 << i:
                    u = dp[u][i][0]
            print(u)
        else: # 남은 거리를 v부터 계산
            diff = depth[v] + depth[u] - 2 * depth[lca] - k + 1
            for i in range(logN - 1, -1, -1):
                if diff & 1 << i:
                    v = dp[v][i][0]
            print(v)