import sys
from collections import *
def input(): return [*map(int,sys.stdin.readline().split())]

def SPFA():
  DP = [1e9]*K; DP[0] = 0
  parent = [0]*K
  dq = deque([0]); inq = [0]*K
  while dq:
    now = dq.popleft()
    inq[now] = 0
    for next,w,c in graph[now]:
      if c-flow[now][next] and (w1:=DP[now]+w)<DP[next]:
        DP[next] = w1; parent[next] = now
        if not inq[next]:
          dq.append(next); inq[next] = 1
  if DP[N+1]<1e9:
    return DP[N+1],parent

def solve():
  cnt = cost = 0
  while spfa:=SPFA():
    c,parent = spfa
    now = N+1
    while now:
      last = parent[now]
      flow[last][now] += 1; flow[now][last] -= 1
      now = last
    cnt += 1; cost += c
  print(cnt); print(-cost)

N,M = input(); K = N+M+2
graph = [[(i,0,1) for i in range(1,N+1)]]+[[(0,0,0)] for i in range(N)]+[[(-i,0,0) for i in range(1,M+1)]]+[[(N+1,0,1)] for i in range(M)]
for i in range(1,N+1):
  n,*data = input()
  for j in range(n):
    j,w = -data[j*2],-data[j*2+1]
    graph[i].append((j,w,1)); graph[j].append((i,-w,0))
flow = [[0]*K for i in range(K)]
solve()