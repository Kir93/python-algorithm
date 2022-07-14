n = int(input())+1
w = [0] * n
dp = [0] * n
for i in range(1,n):
    w[i] = int(input())
    if i == 1 or i == 2: dp[i] = w[i] + w[i-1]
    else: dp[i] = max(w[i]+w[i-1]+dp[i-3], dp[i-1], dp[i-2]+w[i])
print(max(dp))