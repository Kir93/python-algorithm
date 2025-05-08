#my code
import sys
sys.stdin=open("input.txt","rt")
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.insert(0,[0]*n)
data.append([0]*n)
for x in data:
  x.insert(0,0)
  x.append(0)
cnt=0
for i in range(1,n+1):
  for j in range(1,n+1):
    if data[i][j] > data[i][j-1] and data[i][j] > data[i][j+1] and data[i][j] > data[i-1][j] and data[i][j] > data[i+1][j]:
      cnt+=1

print(cnt)

#best code
import sys
#sys.stdin = open("input.txt", 'r')
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
