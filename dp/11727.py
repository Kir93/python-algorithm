dp = [0,1,3]
for i in range(3, 1001): dp.append(2*dp[i-2] + dp[i-1])
print(dp[int(input())]%10007)