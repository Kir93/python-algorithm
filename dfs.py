graph={
1:[2,3],
2:[1,4,5,7],
3:[1,5,9],
4:[2,6],
5:[2,3,7,8],
6:[4],
7:[5,2],
8:[5],
9:[3],
}
def DFS(graph,root):
  stack=[root]
  visited=[]
  while stack:
    n=stack.pop()
    for i in graph[n]:
      if i not in visited:
        stack.append(i)
      if n not in visited:
        visited.append(n)
      print('v',visited)
  return visited

print(DFS(graph,1))
