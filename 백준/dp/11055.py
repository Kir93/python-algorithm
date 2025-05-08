int(input())
ls = list(map(int, input().split()))
dp = [0] * len(ls)
dp[0] = ls[0]
for i in range(1, len(ls)):
    for j in range(i):
        if ls[i] > ls[j]: dp[i] = max(dp[i], dp[j]+ls[i])
        else: dp[i] = max(dp[i], ls[i])
print(max(dp))