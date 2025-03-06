N = int(input())
data1 = [*map(int,input())]
data2 = [*map(int,input())]

DP = [[0]*10 for i in range(N+1)]
path = [[0]*10 for i in range(N+1)]

for n in range(N):
  n = N-1-n
  for i in range(10):
    d = (data2[n]-data1[n]-i)%10
    l,r = d+DP[n+1][(d+i)%10],10-d+DP[n+1][i]
    if l<r:
      DP[n][i],path[n][i] = l,d
    else:
      DP[n][i],path[n][i] = r,d-10

print(DP[0][0])
i = 0
for n in range(N):
  c = path[n][i]
  print(n+1,c)
  if c>0:
    i = (c+i)%10