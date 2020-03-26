import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n, m =map(int,input().split())
data = list(map(int,input().split()))
data.sort()
data = deque(data)
cnt=0
while data:
  if len(data) == 1:
    cnt+=1
    break
  if data[0] + data[-1] > m:
    data.pop()
    cnt+=1
  else:
    data.pop()
    data.popleft()
    cnt+=1
print(cnt)

#new mycode
import sys
#sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
cnt = 0
while data:
    if len(data) == 1:
        cnt += 1
        break
    if data[-1] + data[0] > m:
        cnt += 1
        data.pop()
    elif data[-1] + data[0] <= m:
        cnt += 1
        data.pop(0)
        data.pop()
print(cnt)
