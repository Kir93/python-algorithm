import sys
import math
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
k = int(input())
r = [[(j*10**len(str(s[i]))+s[i])%k for j in range(k)] for i in range(n)]
dp = [[0]*k for _ in range(1<<n)]
dp[0][0]=1

for b in range(1<<n):
    for i in range(n):
        if b&(1<<i): continue
        for j in range(k):
            dp[b|(1<<i)][r[i][j]]+=dp[b][j]
p = dp[(1<<n)-1][0]
q = sum(dp[(1<<n)-1])
g = math.gcd(p,q)
print("%d/%d"%(p//g,q//g))