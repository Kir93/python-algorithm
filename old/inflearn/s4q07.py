import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
need = input()
n = int(input())
for i in range(n):
  data = input()
  dq = deque(need)
  for x in data:
    if x in dq:
      if x != dq.popleft():
        print('#%d NO' %(i+1))
        break
  else:
    if len(dq)==0:
      print("#%d YES" %(i+1))
    else:
      print('#%d NO' %(i+1))
