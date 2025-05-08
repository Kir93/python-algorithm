import sys

m = int(sys.stdin.readline())
f = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[f[i]] for i in range(m + 1)]
for j in range(1, 19):
    for i in range(1, m + 1):
        dp[i].append(dp[dp[i][j - 1]][j - 1])
q = int(sys.stdin.readline())
for _ in range(q):
    n, x = map(int, sys.stdin.readline().split())
    for j in range(18, -1, -1):
        if n >= 1 << j:
            n -= 1 << j
            x = dp[x][j]
    print(x)