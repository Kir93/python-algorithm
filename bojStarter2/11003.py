import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int,input().split())
num = list(map(int, input().split()))
temp = deque([])

for i in range(N):
  if temp and temp[0][0] <= i-L:
    temp.popleft()

  while len(temp) >= 1 and num[i] < temp[-1][1]:
    temp.pop()

  temp.append((i,num[i]))
  
  print(temp[0][1], end = " ")