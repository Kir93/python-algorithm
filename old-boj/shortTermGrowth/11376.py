import sys
input = sys.stdin.readline

def DFS(i):
  if visited[i]:
    return
  visited[i] = 1
  for w in graph[i//2]:
    if work[w]<0:
      work[w] = i
      return 1
  for w in graph[i//2]:
    if DFS(work[w]):
      work[w] = i
      return 1

N,M = map(int,input().split())
graph = [[*map(int,input().split())][1:] for i in range(N)]
work = [-1]*(M+1)
for i in range(2*N):
  visited = [0]*2*N
  DFS(i)
print(M+1-work.count(-1))