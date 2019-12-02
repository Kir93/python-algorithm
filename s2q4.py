#my code
import sys
sys.stdin=open("input.txt","rt")
n = int(input())
data1 = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))
data = []
p1, p2 = 0, 0
while(True):
  if p1==n:
    for i in range(p2,len(data2)):
      data.append(data2[i])
    break
  elif p2==m:
    for i in range(p1,len(data1)):
      data.append(data1[i])
    break
  if data1[p1]<=data2[p2]:
    data.append(data1[p1])
    p1+=1
  else:
    data.append(data2[p2])
    p2+=1

for x in data:
  print(x, end=' ')
  
#best code
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')
