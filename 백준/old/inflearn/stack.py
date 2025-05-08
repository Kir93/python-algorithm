import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):
  stack.append(int(sys.stdin.readline().strip()))

while stack:
  data = stack.pop()
  print(data, end=' ')
