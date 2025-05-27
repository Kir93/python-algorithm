import sys

n,k=map(int,input().split())
L=list(map(int,input().split()))

psum = [0]
for i in range(n):psum.append(psum[-1]+L[i])

dp = [[0]*(n+1) for i in range(k+1)]

def C(i, j):
	return (j-i)*(psum[j]-psum[i])

def solve(i, start, end, l, r):
	if start>end:
		return
	m = (start+end)//2
	optimal=-1

	for j in range(l, min(m, r)):
		k = dp[i-1][j] + C(j, m)
		if optimal==-1 or dp[i][m]>k:
			optimal = j
			dp[i][m]=k
	
	solve(i, start, m-1, l, optimal+1)
	solve(i, m+1, end, optimal, r)

for i in range(n+1):
	dp[1][i] = psum[i]*i

for i in range(2, k+1):
	solve(i, 1, n, 0, n)

print(dp[k][n])