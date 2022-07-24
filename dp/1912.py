int(input())
ls = list(map(int, input().split()))
dp = [-1001] * len(ls)
dp[0] = ls[0]
for i in range(1, len(ls)):
    dp[i] = max(ls[i], dp[i-1]+ls[i])
print(max(dp))