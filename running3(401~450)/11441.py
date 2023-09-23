from sys import stdin
input = stdin.readline

n = int(input())
ls = list(map(int, input().split()))
preSum = [0] * (n + 1)

for i in range(n): preSum[i] = preSum[i-1] + ls[i]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(preSum[j-1] - preSum[i-2])