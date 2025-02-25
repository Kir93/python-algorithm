import sys
input = sys.stdin.readline

N,M = map(int,input().split())

taxi = []
for i in range(N):
  x,y = map(int,input().split())
  if y>x:
    continue
  taxi.append((M-x,M-y))
taxi.sort()
t = len(taxi)

SUM = 0
x = 0
while x < t:
  start,end = taxi[x]
  next = x
  while next+1<t and taxi[next+1][0]<end:
    next += 1
    end = max(taxi[next][1],end)
  SUM += end-start
  x = next+1

print(M+SUM*2)