import sys
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
task = [list(map(int,input().split()))[1:] for _ in range(n)]

visit= [-1]*(m+1)

def dfs(x):
  for i in task[x]:
    if not check[i]:
      check[i]=True
      if visit[i]==-1 or dfs(visit[i]):
        visit[i]=x
        return True
  return False

result=0

for i in range(n):
  check = [False] *(m+1)
  if dfs(i):
    result+=1
  

print(result)