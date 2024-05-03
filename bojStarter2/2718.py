T = int(input())
dp = [1, 1, 5]
cnt = [0, 1, 4]

for _ in range(T):
    N = int(input())

    if N < len(dp):
        print(dp[N])
        continue

    idx = len(dp)

    while N >= idx:
        cnt.append(2 if idx % 2 else 3)
        temp = 0

        for i in range(idx):
            temp += dp[i] * cnt[-i-1]

        dp.append(temp)
        idx += 1

    print(dp[N])