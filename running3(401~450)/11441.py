from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
preSum = [0] * (n + 1)

for i in range(n): preSum[i] = preSum[i-1] + ls[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(preSum[j-1] - preSum[i-2])