import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = dict()

for _ in range(n):
  word = input()
  data[word] = 1

for _ in range(n-1):
  word = input()
  data[word] = 0

for key, val in data.items():
  if val == 1:
    print(key)
    break

#new mycode
import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n = int(input())
rd = []
sd = []
for i in range(n):
  rd.append(input())
for i in range(n-1):
  sd.append(input())
while rd:
  rd = deque(rd)
  if len(rd) == 1:
    print(rd[0])
    break
  c = rd.popleft() 
  for x in sd:
    if c != x:
      rd.append(c)
    else:
      break
  else:
    print(c)
    break
