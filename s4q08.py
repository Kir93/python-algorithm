import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
data = dict()

for _ in range(n):
  word = input()
  data[word] = 1

for _ in range(n-1):
  word = input()
  data[word] = 0

for key, val in data.items():
  if val == 1:
    print(key)
    break
