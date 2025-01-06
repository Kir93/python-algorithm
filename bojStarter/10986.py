import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

r = [0] * m
prefixSum = 0

for i in range(n):
    prefixSum += a[i]
    r[prefixSum % m] += 1

ans = r[0]

for i in range(m): 
    ans += r[i] * (r[i]-1) // 2

print(ans)