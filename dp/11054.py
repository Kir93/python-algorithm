int(input())
ls = list(map(int, input().split()))
rls = list(reversed(ls))
dp = [1] * len(ls)
rdp = [1] * len(ls)
for i in range(1, len(ls)):
    for j in range(i):
        if ls[i] > ls[j]: dp[i] = max(dp[i], dp[j]+1)
        if rls[i] > rls[j]: rdp[i] = max(rdp[i], rdp[j]+1)
rdp = rdp[::-1]
for i in range(len(ls)):
    dp[i] += rdp[i] - 1
print(max(dp))