import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

val = max(arr)

check = [-1] * (val + 1)
for i in range(n):
    check[arr[i]] = i
    
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        diff = abs(arr[i] - arr[j])
    
        if arr[j] + diff <= val and check[arr[j] + diff] != -1:
            dp[i][j] = arr[i] + arr[j]

for i in range(n - 1):
    for j in range(n):
    
        if dp[i][j]:
            diff = abs(arr[i] - arr[j])
        
            if arr[j] + diff <= val and check[arr[j] + diff] != -1:
                dp[j][check[arr[j] + diff]] = max(dp[j][check[arr[j] + diff]], dp[i][j] + arr[check[arr[j] + diff]])

ans = 0
for i in dp:
    ans = max(ans, max(i))

print(ans)