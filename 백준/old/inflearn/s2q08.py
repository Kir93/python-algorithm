import sys
#sys.stdin=open("input.txt","rt")
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
  a,b,c = map(int,input().split())
  if b==0:
    for _ in range(c):
      data[a-1].append(data[a-1].pop(0))
  else:
    for _ in range(c):
      data[a-1].insert(0, data[a-1].pop())

s=0
e=n-1
cnt = 0
for i in range(n):
  for j in range(s,e+1):
    cnt+= data[i][j]
  if i<n//2:
    s+=1
    e-=1
  else:
    s-=1
    e+=1
print(cnt)
