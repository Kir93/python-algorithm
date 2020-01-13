import sys
#sys.stdin = open("input.txt", "rt")
def DFS(x):
  if x == 0:
    return
  else:
    DFS(x//2)
    print(x%2)

if __name__ == '__main__':
  n = int(input())
  DFS(n)
