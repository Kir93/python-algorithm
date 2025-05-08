import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
  data.append(int(sys.stdin.readline().strip()))

for i in sorted(data):
  print(i)
