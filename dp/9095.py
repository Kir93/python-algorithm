t = int(input())
dp = [0,1,2,4]

for _ in range(4,11):
    dp.append(sum(dp[-3:]))

for _ in range(t):
    print(dp[int(input())])