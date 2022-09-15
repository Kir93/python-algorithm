w = [int(input()) for _ in range(int(input()))]
dp = [0] * len(w)
if(len(w)==1):
    print(w[0])
    exit()
dp[0], dp[1] = w[0], w[0]+w[1]
for i in range(2, len(w)):
    dp[i] = max(w[i] + dp[i-2], w[i] + w[i-1] + dp[i-3], dp[i-1])
print(max(dp))