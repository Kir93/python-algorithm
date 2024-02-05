import sys
def input(): return [*map(int,sys.stdin.readline().split())]

def DFS(i):
  if visited[i]:
    return 0
  visited[i] = 1
  for w in graph[i]:
    if work[w]<0:
      work[w] = i
      return 1
  for w in graph[i]:
    if DFS(work[w]):
      work[w] = i
      return 1
  return 0

N,M,K = input()
graph = [input()[1:] for i in range(N)]
work = [-1]*(M+1)
for i in range(N):
  visited = [0]*N
  DFS(i)
i = k = 0
while i<N and k<K:
  visited = [0]*N
  d = DFS(i)
  k += d; i += d^1
print(M+1-work.count(-1))