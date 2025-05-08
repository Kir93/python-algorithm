def DFS(x):
  if x > 7:
    return
  else:
    print(x, end=" ") #전위순회(자신 - 왼 - 우)
    DFS(x*2)
    #print(x, end=" ") #중위순회(왼 - 자신 - 우))
    DFS(x*2+1)
    #print(x, end=" ") #후위순회(왼 - 우 - 자신)


if __name__ == '__main__':
  DFS(1)
