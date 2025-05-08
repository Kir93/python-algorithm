import sys
input = sys.stdin.readline

def updatefen(i):
  while i<=M:
    fen[i] += 1
    i += i&-i

def sumfen(i):
  SUM = 0
  while i:
    SUM += fen[i]
    i -= i&-i
  return SUM

for _ in range(int(input())):
  N = int(input()); M = 1<<17
  
  xlist = []; ylist = []
  for i in range(N):
    x,y = map(int,input().split())
    xlist.append([-x,0]); ylist.append((y,-x,i))
  ylist.sort()
  for i in range(N):
    xlist[ylist[i][2]][1] = i+1
  xlist.sort()
  
  fen = [0]*(M+1); result = 0
  for x,i in xlist:
    result += sumfen(i)
    updatefen(i)
  
  print(result)