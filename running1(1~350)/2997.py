dp = sorted(list(map(int, input().split())))
d = min(dp[1] - dp[0], dp[2] - dp[1])
for i in range(len(dp)):
    r = dp[i] + d
    if r not in dp:
        print(r)
        break