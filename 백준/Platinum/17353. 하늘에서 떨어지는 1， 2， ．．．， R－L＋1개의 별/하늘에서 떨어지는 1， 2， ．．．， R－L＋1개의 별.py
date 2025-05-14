import sys
input = sys.stdin.readline

def update(i,j,v,s,e,x):
  if i==s and j==e:
    seg[0][x] += v
    seg[1][x] += 1
    return
  mid = (s+e)//2
  if j<=mid:
    update(i,j,v,s,mid,x*2)
  elif i>mid:
    update(i,j,v,mid+1,e,x*2+1)
  else:
    update(i,mid,v,s,mid,x*2); update(mid+1,j,v+mid+1-i,mid+1,e,x*2+1)

def SUM(i,s,e,x):
  global S
  S += seg[0][x]+seg[1][x]*(i-s)
  if s==e:
    return
  mid = (s+e)//2
  if i<=mid:
    SUM(i,s,mid,x*2)
  else:
    SUM(i,mid+1,e,x*2+1)    

N = int(input())
data = [0,*map(int,input().split())]
seg = [[0]*4*N,[0]*4*N]
for _ in range(int(input())):
  q,*a = map(int,input().split())
  if q-1:
    S = data[a[0]]; SUM(*a,0,N,1)
    print(S)
  else:
    update(*a,1,0,N,1)