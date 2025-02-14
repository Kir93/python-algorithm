import sys
input = sys.stdin.readline

N = int(input())
cost = [[*map(int, input().split())] for _ in range(N)]
dp=[10**6]*(1<<N)
dp[0]=0

for i in range(1<<N):
    k = 0
    for j in range(N):
        if i & (1<<j):
            k+=1
    for j in range(N):
        if i & (1 << j) == 0 and dp[i|(1<<j)] > dp[i]+cost[k][j]:
            dp[i|(1<<j)] = dp[i] + cost[k][j]

print(dp[-1])