import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

ladders = {}
for _ in range(N):
  x, y = map(int, sys.stdin.readline().strip().split())
  ladders[x] = y

snakes = {}
for _ in range(M):
  x, y = map(int, sys.stdin.readline().strip().split())
  snakes[x] = y

ch = [0] * 101
Q = deque()
Q.append(1)
ch[1] = 0

cnt = 0
flag = True

while flag:
  length = len(Q)
  for _ in range(length):
    x = Q.popleft()

    if x == 100:
      print(cnt)
      flag = False
      break

    for i in range(1, 7):
      nx = x + i
    
      if nx <= 100 and ch[nx] == 0:
    
        ch[nx] = 1
    
        if nx in ladders.keys():
          ch[ladders[nx]] = 1
          Q.append(ladders[nx])

        elif nx in snakes.keys():
          ch[snakes[nx]] = 1
          Q.append(snakes[nx])
        
        else:
          Q.append(nx)

  cnt += 1