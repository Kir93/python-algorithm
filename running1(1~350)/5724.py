dp = [0, 1, 5]
for i in range(3, 101): dp.append(i**2 + dp[i-1])
while True:
    n = int(input())
    if n == 0: break
    print(dp[n])