import sys
input = sys.stdin.readline
 
INF = 10**9 * 3
dp = [[[-1 for _ in range(2)] for _ in range(1001)] for _ in range(1001)]
pre = [0 for _ in range(1001)]
 
def f(l, r, p):
    if l==1 and r==n:
        return 0
    if dp[l][r][p] != -1:
        return dp[l][r][p]
    minus = s - (pre[r] - pre[l-1])
    dp[l][r][p] = INF
    if l>1:
        dp[l][r][p] = f(l-1, r, 0) + minus * ((idx[r] if p else idx[l]) - idx[l-1])
    if r<n:
        dp[l][r][p] = min(dp[l][r][p], f(l, r+1, 1) + minus * (idx[r+1] - (idx[r] if p else idx[l])))
    return dp[l][r][p]
 
idx = [0]
cost = [0]
n, m = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    idx.append(x)
    cost.append(y)
for i in range(1, n+1):
    pre[i] = pre[i-1] + cost[i]
 
s = pre[n]
print(f(m,m,0))