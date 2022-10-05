# 점화식 생각보다 간단
# 어렵지 않게 생각하면 간단하게 해결 됨
# dp, ls 앞에 0 추가
# 이중 for문

n = int(input())
ls = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + ls[j], ls[i])
print(dp[-1])