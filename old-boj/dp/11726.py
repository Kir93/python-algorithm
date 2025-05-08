n = int(input())
m = 0
if n > 1001: m = 1001
else: m = n   
dp = [0] * 1001

for i in range(1, m+1):
    if i==1: dp[i] = 1
    elif i==2: dp[i] = 2
    else:
        dp[i] = dp[i-2] + dp[i-1]
    
print(dp[m]%10007)