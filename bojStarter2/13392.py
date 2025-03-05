N = int(input())
d1 = [*map(int,input())]
d2 = [*map(int,input())]

DP = [[0]*10 for i in range(N+1)]

for n in range(N):
  n = N-1-n
  for i in range(10):
    d = (d2[n]-d1[n]-i)%10
    DP[n][i] = min(d+DP[n+1][(d+i)%10],10-d+DP[n+1][i])

print(DP[0][0])