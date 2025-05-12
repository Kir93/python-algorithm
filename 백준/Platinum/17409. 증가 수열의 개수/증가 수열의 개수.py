import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * int(n + 2) for _ in range(m + 1)]

def q(p, k):
    s = 0
    while p:
        s = (s + dp[k][p]) % 1000000007
        p -= (p & -p)
    return s

def u(p, k, v):
    while p <= n + 1:
        dp[k][p] = (dp[k][p] + v) % 1000000007
        p += (p & -p)

u(1, 0, 1)
for i in arr:
    for j in range(1, m + 1):
        u(i + 1, j, q(i, j - 1))

print(q(n + 1, m))