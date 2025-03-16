def DFS(y,x):
  if visited[y][x]:
    return 0
  visited[y][x] = 1
  for y1,x1 in graph[y][x]:
    if not match[y1][x1]:
      match[y1][x1] = y,x
      return 1
  for y1,x1 in graph[y][x]:
    if DFS(*match[y1][x1]):
      match[y1][x1] = y,x
      return 1
  return 0

for _ in range(int(input())):
  N,M = map(int,input().split())
  board = [[*map(lambda x:int(x=="."),input())] for i in range(N)]
  graph = [[[] for x in range(M)] for y in range(N)]
  for x in range(M//2):
    x = x*2+1
    for y in range(N):
      if board[y][x]:
        for i in [-1,0,1]:
          for j in [-1,1]:
            if N>y+i>=0 and M>x+j>=0 and board[y+i][x+j]:
              graph[y][x].append((y+i,x+j))
  match = [[0]*M for i in range(N)]
  m = 0
  for x in range(M//2):
    x = x*2+1
    for y in range(N):
      if board[y][x]:
        visited = [[0]*M for i in range(N)]
        m += DFS(y,x)
  print(sum(map(sum,board))-m)