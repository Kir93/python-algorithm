int(input())
ls = list(map(int, input().split()))
dp = [1] * len(ls)
for i in range(1, len(ls)):
    for j in range(i):
        if ls[i] < ls[j]: dp[i] = max(dp[i], dp[j]+1)
print(max(dp))