import sys
sys.setrecursionlimit(10**4+1)
input = sys.stdin.readline

N = int(input())
w = [0] + list(map(int, input().split()))

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N+1)
dp = [[w[i], 0] for i in range(N+1)]

def dfs(n):
    visited[n] = True

    for nn in tree[n]:
        if visited[nn]:
            continue

        dfs(nn)
        dp[n][0] += dp[nn][1]
        dp[n][1] += max(dp[nn][0], dp[nn][1])

dfs(1)
print(max(dp[1][0], dp[1][1]))