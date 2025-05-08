dp = [1] * 101
for _ in range(int(input())):
    n = int(input())
    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n-1])