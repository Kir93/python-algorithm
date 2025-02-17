import sys
input = sys.stdin.readline

def DFS(now):
  global id,s
  visited[now] = nowid = id
  stack.append(now)
  for next in graph[now]:
    if scc[next]:
      continue
    if not visited[next]:
      id += 1
      DFS(next)
    visited[now] = min(visited[now],visited[next])
  if visited[now]==nowid:
    s += 1
    while stack:
      x = stack.pop()
      scc[x] = s
      if x==now:
        break

def check():
  for i in range(1,N+1):
    if scc[i]==scc[-i]:
      return "no"
  return "yes"

while 1:
  try:
    N,M = map(int,input().split())
  except:
    break
  graph = [[] for i in range(2*N+1)]
  graph[-1] = [1]
  for _ in range(M):
    a,b = map(int,input().split())
    graph[-a].append(b)
    graph[-b].append(a)
  visited = [0]*(2*N+1); scc = [0]*(2*N+1); stack = []; s = 0
  for i in range(1,N+1):
    if not visited[i]:
      id = 1
      DFS(i)
      
  print(check())