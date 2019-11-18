import queue

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

def BFS(graph,root):
  visited=[]
  queue=[root]
  while queue:#while queue is not empty
    n = queue.pop(0)
    if n not in visited:#if n is not in visited list.
      visited.append(n)#put the n to the visited list.
    for i in graph[n]:#the numbers i connected with n
      if i not in visited:#i is not in visited list.
        queue.append(i)#put the i to the queue.
  return visited

print(BFS(graph,1))
