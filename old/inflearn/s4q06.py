#my code
import sys
from collections import deque
#sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
data = list(map(int, input().split()))
dng = []
cnt = 0
for i in range(len(data)):
    dng.append((i, data[i]))
dng = deque(dng)
x = 0
while dng:
    for y in range(len(dng)):
        if dng[x][1] < dng[y][1]:
            dng.append(dng.popleft())
            break
    else:
        if dng[x][0] == m:
            cnt += 1
            print(cnt)
            break
        else:
            cnt += 1
            dng.popleft()

#best code
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break

#new mycode
import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
data = [(p, v) for p, v in enumerate(list(map(int, input().split())))]
data = deque(data)
cnt = 0
while True:
  maxx=max(data, key=lambda x:x[1])
  c = data.popleft()
  if c[1] < maxx[1]:
    data.append(c)
  else:
    cnt += 1
    if c[0] == m:
      print(cnt)
      break
    
