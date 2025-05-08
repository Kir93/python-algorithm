from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cost = [int(input()) for _ in range(N)]
total_cost = sum(cost)

dp_arr = [0] * (N + 1)

dq = deque()
dq.append(0)

for i in range(1, N + 1):
    while dq and dq[0] < i - K - 1:
        dq.popleft()
    
    dp_arr[i] = cost[i - 1] + dp_arr[dq[0]]
    
    while dq and dp_arr[dq[-1]] >= dp_arr[i]:
        dq.pop()
    dq.append(i)

ans = min(dp_arr[N - K:])
print(total_cost - ans)