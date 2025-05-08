from collections import deque

def BFS(x):
  parent = [-1]*K
  dq = deque([0])
  while dq:
    now = dq.popleft()
    for next in range(K):
      if (c:=graph[now][next])<0:
        c = x
      if parent[next]<0 and c-flow[now][next]:
        parent[next] = now
        if next==N+1:
          return parent
        dq.append(next)

def solve(x):
  global flow
  flow = [[0]*K for i in range(K)]
  s = 0
  while parent:=BFS(x):
    now = N+1; f = M
    while now:
      last = parent[now]
      if (c:=graph[last][now])<0:
        c = x
      f = min(f,c-flow[last][now])
      now = last
    now = N+1
    while now:
      last = parent[now]
      flow[last][now] += f; flow[now][last] -= f
      now = last
    s += f
  if S==s:
    return flow

N = int(input()); M = 1<<14; K = N*2+2
graph = [[0]*K for i in range(K)]
column,row = [[*map(int,input().split())] for i in range(2)]
S = sum(column)
for i in range(1,N+1):
  graph[0][i] = column[i-1]
  graph[-i][N+1] = row[i-1]
  for j in range(1,N+1):
    graph[i][-j] = -1

x,c = M,13
while c+1:
  if result:=solve(x):
    X,Flow = x,result
    x -= 1<<c
  else:
    x += 1<<c
  if not c:
    if result:=solve(x):
      X,Flow = x,result
  c -= 1    
print(X)
for i in range(1,N+1):
  print(*reversed(Flow[i][-N:]))