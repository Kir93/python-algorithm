import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
inlst = [input().rstrip() for _ in range(N)]

B_prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]
W_prefix = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if (i + j) % 2:
            if inlst[i][j] == 'B':
                B_prefix[i][j] = 1 + B_prefix[i-1][j] + B_prefix[i][j-1] - B_prefix[i-1][j-1]
                W_prefix[i][j] = 0 + W_prefix[i-1][j] + W_prefix[i][j-1] - W_prefix[i-1][j-1]
            else:
                B_prefix[i][j] = 0 + B_prefix[i-1][j] + B_prefix[i][j-1] - B_prefix[i-1][j-1]
                W_prefix[i][j] = 1 + W_prefix[i-1][j] + W_prefix[i][j-1] - W_prefix[i-1][j-1]
        else:
            if inlst[i][j] == 'B':
                B_prefix[i][j] = 0 + B_prefix[i-1][j] + B_prefix[i][j-1] - B_prefix[i-1][j-1]
                W_prefix[i][j] = 1 + W_prefix[i-1][j] + W_prefix[i][j-1] - W_prefix[i-1][j-1]
            else:
                B_prefix[i][j] = 1 + B_prefix[i-1][j] + B_prefix[i][j-1] - B_prefix[i-1][j-1]
                W_prefix[i][j] = 0 + W_prefix[i-1][j] + W_prefix[i][j-1] - W_prefix[i-1][j-1]

ans = 2000000
for i in range(N - K + 1):
    for j in range(M - K + 1):
        B_sub_sum = B_prefix[i+K-1][j+K-1] - B_prefix[i-1][j+K-1] - B_prefix[i+K-1][j-1] + B_prefix[i-1][j-1]
        W_sub_sum = W_prefix[i+K-1][j+K-1] - W_prefix[i-1][j+K-1] - W_prefix[i+K-1][j-1] + W_prefix[i-1][j-1]
        ans = min(ans, B_sub_sum, W_sub_sum)

print(ans)