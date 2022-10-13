ls = [int(input()) for _ in range(int(input()))]
dp = [0] * len(ls)
if len(ls) == 1: exit(print(ls[0]))
dp[0], dp[1] = ls[0], ls[0] + ls[1]
for i in range(2, len(ls)):
    dp[i] = max(dp[i-3]+ls[i-1]+ls[i], dp[i-1], dp[i-2]+ls[i])
print(dp[-1])