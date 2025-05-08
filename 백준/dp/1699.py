n = int(input()) + 1
dp = [i for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if j*j > i: break
        if dp[i] > dp[i-j*j] + 1: dp[i] = dp[i-j*j] + 1
print(dp[-1])