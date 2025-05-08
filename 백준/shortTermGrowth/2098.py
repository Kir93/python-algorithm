import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (1 << N - 1) for _ in range(N)]

def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        if W[i][0]:
            return W[i][0]
        else:
            return float('inf')
            
    min_dist = float('inf')
    for j in range(1, N):
        if not W[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist
    
    return min_dist

print(solution(0, 0))