import sys
input = sys.stdin.readline

def update(y,x,v):
  while y<=K:
    x1 = x
    while x1<=K:
      fen[y][x1] += v
      x1 += x1&-x1
    y += y&-y

def cal(y,x):
  s = 0
  while y:
    x1 = x
    while x1:
      s += fen[y][x1]
      x1 -= x1&-x1
    y -= y&-y
  return s

def solve(y1,x1,y2,x2):
  return cal(y2,x2)-cal(y1-1,x2)-cal(y2,x1-1)+cal(y1-1,x1-1)

N,M = map(int,input().split()); K = 1<<10
board = [[]]+[[0,*map(int,input().split())] for i in range(N)]

fen = [[0]*(K+1) for i in range(K+1)]
for i in range(1,N+1):
  for j in range(1,N+1):
    update(i,j,board[i][j])
for _ in range(M):
  q,*a = map(int,input().split())
  if q:
    print(solve(*a))
  else:
    y,x,v = a
    d = v-board[y][x]; board[y][x] = v
    update(y,x,d)