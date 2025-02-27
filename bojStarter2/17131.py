import sys
input = sys.stdin.readline

def update(i):
  while i<=M:
    fen[i] += 1
    i += i&-i

def sumfen(i):
  SUM = 0
  while i:
    SUM += fen[i]
    i -= i&-i
  return SUM

N = int(input()); M = 1<<19
co = [[] for i in range(M)]
for _ in range(N):
  x,y = map(int,input().split())
  co[-y+(1<<18)].append(x+(1<<18))

result = 0; fen = [0]*(M+1)
for y in range(M):
  for x in co[y]:
    result += sumfen(x-1)*(sumfen(M)-sumfen(x))
    result %= 10**9+7
  for x in co[y]:
    update(x)
print(result)