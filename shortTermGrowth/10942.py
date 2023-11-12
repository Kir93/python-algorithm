import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [[0]*n for i in range(n)]

for i in range(n):
    dp[i][i]=1
for i in range(n-1):
    if seq[i]==seq[i+1] : dp[i][i+1]=1
    else : dp[i][i+1]=0
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j = i+2+cnt
        if seq[i]==seq[j] and dp[i+1][j-1]==1 :
            dp[i][j]=1

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])