import sys
import heapq
N, T = map(int, sys.stdin.readline().split())

M = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))
R = list(map(int, sys.stdin.readline().split()))

save = sorted(zip(M, P, R), key=lambda x: x[2] / x[1])

dp = [-1] * (T + 1)
dp[0] = 0

for idx in range(N):
    M_i, P_i, R_i = save[idx]
    for time in range(T, R_i - 1, -1):
        if dp[time - R_i] != -1:
            dp[time] = max(dp[time], dp[time - R_i] + M_i - time * P_i)

print(max(dp))