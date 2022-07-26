ls = []
for _ in range(int(input())):
    ls.append(int(input()))
if len(ls) != 0:
    dp = [0] * len(ls)
    for i in range(len(ls)):
        if i == 0: dp[i] = ls[0]
        elif i == 1: dp[i] = ls[0] + ls[1]
        else: dp[i] = max(ls[i]+ls[i-1]+dp[i-3], ls[i]+dp[i-2])
    print(dp[-1])
