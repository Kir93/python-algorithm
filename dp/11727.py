n = int(input())
m = 1001
if n < 1001: m = n
dp = [0] * (m+1)

if m == 1: print(1)
elif m == 2: print(3)
else:
    for i in range(1, m+1):
        if i==1: dp[i] = 1
        elif i==2: dp[i] = 3
        else:
            dp[i] = 2*dp[i-2] + dp[i-1]

    print(dp[m]%10007)